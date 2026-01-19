# Feedback Management – User Guide (Draft)

This guide explains how to use the Feedback Management system in EspoCRM as an end user.  
It focuses on day-to-day tasks such as viewing feedback, classifying it, and supporting analysis.

This guide does **not** cover system setup, technical configuration, or administration.

---

## Who This Guide Is For

This guide is intended for users who:

- Review and manage incoming community feedback
- Classify feedback using administrative or coding frameworks
- Support programme teams with qualitative insights
- Work with feedback as part of CEA or analysis processes

If you are responsible for configuring the system, integrations, or user permissions, refer to the [**Admin Guide**](/guides/admin.md) instead.

---

## Getting Started

### Accessing the System
1. Log in to EspoCRM using the credentials provided to you
2. Navigate to the **Feedback Data** section

Your access and available actions depend on your assigned role and team.

---

## Viewing Feedback

### Feedback Records
Each feedback record represents a single piece of feedback received from a community member.

A feedback record may include:
- The feedback message or description
- Channel or source (e.g. phone, form, messaging)
- Location or administrative information
- Demographic information
- Contact details of the community member
- Coding or classification fields
- Status or follow-up information

You can:
- Open a feedback record to see full details
- Use list views to browse recent or assigned feedback
- Apply filters to narrow down what you see

---

## Using Administrative Levels

Some feedback records include **administrative levels** (e.g. Province, District, Branch).

These fields use **cascading selects**:
- You first select a higher-level location
- Available options for lower levels are filtered automatically

This helps ensure locations are selected consistently.

If a dropdown appears empty, it usually means:
- A higher-level value has not been selected yet
- The relevant locations have not been created in the system

---

## Classifying Feedback (Coding Frameworks)

Feedback can be classified using a **coding framework** to support qualitative analysis.

Typical structure:
- Coding Level 1 → Type
- Coding Level 2 → Category
- Coding Level 3 → Code

These fields also use cascading selects:
- Categories depend on the selected Type
- Codes depend on the selected Category (and Type)

You do not need to memorise codes; only valid options will be shown.

---

## Updating Feedback Records

Depending on your role, you may be able to:

- Add or update classifications
- Add internal notes or comments
- Update status or follow-up fields
- Assign feedback to another user or team

Changes are saved directly on the feedback record and may be visible to other users.

---

## Searching and Filtering

You can use filters to:
- View feedback from a specific location
- Focus on certain feedback types or categories
- See feedback assigned to you or your team
- Explore patterns across multiple records

Filters can usually be combined to narrow results further.

---

## Supporting Analysis and Learning

Your work contributes to:
- Identifying recurring issues or concerns
- Informing programme improvements
- Supporting accountability and learning processes

Consistent classification and careful review help ensure that feedback can be analysed meaningfully over time.

---

## Common Tips

- Select higher-level fields first (e.g. location or type) to unlock dependent fields
- Use existing categories and codes rather than free text where possible
- Add internal notes if context is needed for interpretation
- Ask an administrator if expected options are missing

---

## Getting Help

If you encounter issues such as:
- Missing dropdown options
- Inability to edit records
- Unclear classifications

Contact your system administrator or team lead for support.

For technical or configuration-related questions, refer to the [**Admin Guide**](/guides/admin.md).
