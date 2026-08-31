#!/usr/bin/env python3
"""Fail the build if the extension tree references files it does not ship.

EspoCRM resolves client-side references like `"selectHandler": "custom:handlers/foo"`
at runtime. A missing target does not stop the extension installing -- it installs
cleanly and the behaviour is simply absent, which is easy to ship without noticing.

Entity Manager > Export is the usual source of this: it packages only
`custom/Espo/Custom/Resources` (with metadata filtered to a whitelist), so client JS,
Jobs and `metadata/app` are dropped while the metadata that references them is kept.

Usage: validate-extension.py [extension-dir]
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

# Metadata keys whose values point at a client-side JS module.
CLIENT_REF_KEYS = {
    "selectHandler", "handler", "view", "recordViews", "dynamicHandler",
    "initHandler", "editView", "detailView", "listView", "modalView",
    "createHandler", "saveHandler", "colorField", "layoutDefaultSidePanelView",
}

PREFIXED_REF = re.compile(r"^[a-z][a-z0-9-]*:[A-Za-z0-9/_.-]+$")


def iter_strings(node, path=""):
    if isinstance(node, dict):
        for key, value in node.items():
            yield from iter_strings(value, f"{path}.{key}" if path else key)
    elif isinstance(node, list):
        for index, value in enumerate(node):
            yield from iter_strings(value, f"{path}[{index}]")
    elif isinstance(node, str):
        yield path, node


def resolve_client_ref(root: Path, ref: str) -> Path:
    prefix, _, name = ref.partition(":")
    if prefix == "custom":
        # loader.js hardcodes the `custom:` prefix to client/custom/src/ and
        # short-circuits before module resolution.
        return root / "files" / "client" / "custom" / "src" / f"{name}.js"
    return root / "files" / "client" / "custom" / "modules" / prefix / "src" / f"{name}.js"


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else "extension").resolve()
    if not root.is_dir():
        print(f"::error::no such directory: {root}")
        return 1

    errors: list[str] = []

    manifest_path = root / "manifest.json"
    if not manifest_path.is_file():
        errors.append("manifest.json is missing")
    else:
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            for key in ("name", "version", "acceptableVersions"):
                if key not in manifest:
                    errors.append(f"manifest.json: missing '{key}'")
            version = manifest.get("version", "")
            if not re.fullmatch(r"\d+\.\d+\.\d+", str(version)):
                errors.append(f"manifest.json: version '{version}' is not semver")
        except json.JSONDecodeError as exc:
            errors.append(f"manifest.json: invalid JSON ({exc})")

    php_classes = {
        f"Espo\\Modules\\{php.relative_to(root / 'files' / 'custom' / 'Espo' / 'Modules').parts[0]}"
        f"\\{'\\'.join(php.relative_to(root / 'files' / 'custom' / 'Espo' / 'Modules').parts[1:-1])}"
        f"\\{php.stem}"
        for php in (root / "files" / "custom" / "Espo" / "Modules").rglob("*.php")
    }

    checked = 0
    for json_file in sorted(root.rglob("*.json")):
        try:
            data = json.loads(json_file.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{json_file.relative_to(root)}: invalid JSON ({exc})")
            continue

        rel = json_file.relative_to(root)
        for key_path, value in iter_strings(data):
            leaf = key_path.split(".")[-1].split("[")[0]

            if leaf == "jobClassName":
                checked += 1
                if value not in php_classes:
                    errors.append(f"{rel}: jobClassName has no shipped class: {value}")
                continue

            if leaf in CLIENT_REF_KEYS and PREFIXED_REF.match(value):
                checked += 1
                if not resolve_client_ref(root, value).is_file():
                    errors.append(f"{rel}: {leaf} -> {value} (file not in extension)")

    if errors:
        print(f"Validation FAILED -- {len(errors)} problem(s):")
        for error in errors:
            print(f"::error::{error}")
        print("\nThe extension would install cleanly and then misbehave at runtime.")
        return 1

    print(f"Validation passed: {checked} reference(s) resolve, manifest is well-formed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
