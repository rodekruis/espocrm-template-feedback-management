# Cascading Selects (Administrative Levels & Coding Frameworks)

This document explains how cascading selects are implemented in the Feedback Management template, and how to use or extend them safely.

Cascading selects are used when the available options of one field depend on the value selected in another field.

---

## Supported Hierarchies

The template supports two independent hierarchical structures:

### 1. Administrative hierarchy
Used for geography or organisational structures.

Example:
- Admin Level 1 → Province
- Admin Level 2 → District
- Admin Level 3 → Branch

### 2. Coding framework hierarchy
Used for qualitative feedback analysis.

Example:
- Coding Level 1 → Type
- Coding Level 2 → Category
- Coding Level 3 → Code

The same technical pattern is used for both hierarchies.

---
## Creating or Importing Hierarchy Records (Required)

While the **structure and relationships** are provided by the template, the **actual hierarchy values** (e.g. provinces, categories, codes) must still be created or imported before they can be selected in feedback records.

If no records exist, the cascading selects will appear empty.

### Option 1: Manual creation (small datasets)

Use this approach for:
- small hierarchies
- initial testing
- quick adjustments

Steps:
1. Go to the entity list (e.g. *Admin Level 1* or *Coding Level 1*)
2. Create records for all Level 1 values
3. Create Level 2 records and link each to the correct Level 1
4. Create Level 3 records and link them to:
   - the correct Level 2
   - and (where applicable) the corresponding Level 1

This ensures cascading filters work correctly.

---

### Option 2: CSV import (recommended for real deployments)

For larger hierarchies, importing via CSV is strongly recommended.

Steps:
1. Navigate to the relevant entity (e.g. `CAdminLevel2`, `CCodingLevel3`)
2. Export existing records (or an empty list) to CSV  
   This provides a ready-made **CSV template** with correct column names.
3. Populate the CSV with your hierarchy data:
   - Include parent link columns (e.g. `adminLevel1Id`, `codingLevel2Id`)
4. Import the CSV back into EspoCRM
5. Repeat per hierarchy level if needed

Tip:
- Always import **Level 1 first**, then Level 2, then Level 3
- Parent records must exist before child records can reference them

---

## Required Relationships (Already Included)

For cascading selects to work, specific entity relationships are required.

**These relationships are already included as part of the Feedback Management template and extension.  
You do not need to create or configure these relationships manually.**

They are documented here to clarify how the cascading behaviour works internally.

### Administrative levels

| Entity | Field | Type | Points to |
|------|------|------|-----------|
| CAdminLevel2 | adminLevel1 | belongsTo | CAdminLevel1 |
| CAdminLevel3 | adminLevel2 | belongsTo | CAdminLevel2 |
| CAdminLevel3 | adminLevel1 | belongsTo | CAdminLevel1 |

The direct Level 1 → Level 3 relationship is required to support combined filtering.

### Coding framework levels

| Entity | Field | Type | Points to |
|------|------|------|-----------|
| CCodingLevel2 | codingLevel1 | belongsTo | CCodingLevel1 |
| CCodingLevel3 | codingLevel2 | belongsTo | CCodingLevel2 |
| CCodingLevel3 | codingLevel1 | belongsTo | CCodingLevel1 |

---



## Handler Architecture

Cascading behaviour is implemented using **select handlers**.

The pattern is:

- One handler per selection step
- Level 2 filtered by Level 1
- Level 3 filtered by Level 1 and further narrowed by Level 2

### Handler naming conventions

- `*-by-*`  
  Used for simple one-level dependencies  
  Example: `adminLevel2-by-adminLevel1`

- `*-filtered`  
  Used when multiple parent fields are applied  
  Example: `adminLevel3-filtered`

This naming keeps handlers readable and future-proof.

---

## Troubleshooting

### Error: `Not existing attribute <field>Id in where`
Cause:
- Missing or incorrect `belongsTo` relationship
- Incorrect field name or casing

Fix:
- Verify the parent link exists on the target entity
- Check exact casing in Entity Manager

---

### Error: HTTP 500 after rebuild
Cause:
- Invalid JSON in `clientDefs`

Fix:
- Validate JSON before rebuilding
- Check for missing commas or trailing commas

---

### Cascading filter not applied
Cause:
- Metadata cache not rebuilt
- Browser cache not refreshed

Fix:
- Run rebuild
- Hard refresh browser (Ctrl + F5)

---

## Extending the Pattern

This pattern can be reused for:
- Thematic hierarchies
- Taxonomies
- Sector / sub-sector classifications
- Any ordered classification with 2–3 levels

Follow the same naming and relationship rules to avoid issues.
