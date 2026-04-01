# EspoCRM Feedback Management Template

The EspoCRM Feedback Management Template is created by the [510 Data & Digital team](https://510.global/) of the Netherlands Red Cross.
It is designed to help humanitarian teams strengthen trust with communities by making it easy to listen and respond to community feedback in a structured way.

---

## Table of Contents

- [About](#about)  
- [Features](#features)  
- [Requirements](#requirements)  
- [Installation](#installation)  
- [How to Use](#how-to-use)  
- [Terms of Use](#terms-of-use)  

---

## About

This template enables you to easily record, track, and manage feedback from staff, volunteers or community members, all within EspoCRM with the possibility to integrate with KoboToolbox. It provides simple forms, clear status tracking, and visual dashboards to help humanitarian teams improve feedback handling.

**Flexibility and simplicity are at the heart of this template:**
- It provides many example questions and feedback types, so organisations can easily adapt it to their own needs and contexts.
- The data model is kept as simple as possible. This makes the system easy to understand, maintain, and use, even as teams make their own custom changes.

This template is designed so anyone, no matter their digital skills, can collect and act on feedback in a clear and organised way.


---

## Features

- 📝 **User-friendly feedback forms** for easy data entry  
- 🔄 **Clear status tracking** (open, in progress, closed)  
- 📊 **Visual dashboards and reports** to see feedback at a glance  
- ❓ **Pre-built examples** of questions and answer options to help you get started 
- 👤 **Role-based permissions:** control who can view, edit, or manage feedback according to their role and team in EspoCRM
- 🧭 **Cascading hierarchical classification** for both administrative levels and  coding frameworks (e.g. Province → District → Branch, Type → Category → Code)
- 🛠 **Customization**: Add your own fields, layouts, dashboards and automatic flowcharts without coding  
- 🔗 **Integrates** with:
    - 📱 **[KoboToolbox:](/guides/kobo-integration.md)** collect feedback offline and sync with EspoCRM when back online  
    - 📈 **[Power BI:](https://github.com/rodekruis/EspoCRM-knowledge-base/wiki/Third-party-integration#integrate-espocrm-with-powerbi-via-api)** connect EspoCRM data to PowerBI for advanced visualisations and reports  
    - 🤖 **[AI:](/guides/qfa.md)** for analyzing qualitative feedback using Artificial Intelligence


---

## Requirements

### Hard Requirements
These are needed to install and use the template:
- Installed EspoCRM **v7.2 or higher** ([docs](https://github.com/rodekruis/EspoCRM-knowledge-base/wiki/Installation#install-a-virtual-machine-for-espocrm-in-azure)) 
- **Admin user** access to install the template
- Already procured and installed **[EspoCRM Advanced Pack extension](https://www.espocrm.com/extensions/advanced-pack/)**  

### Recommendations:
These are not required, but will improve your experience:

- **Backup of your EspoCRM data**  
  (Recommended before installation.)
- **Email notifications configured**  
  (So your team can receive alerts about new feedback.)
- **Single Sign-On (SSO) configured**  
  (If your organisation uses SSO, this makes it easier and safer for team members to log in.)
- **Up-to-date web browser**  
  (For best performance and security.)

---

## Installation
The following steps will install the template itself and recommends the installation of additions and changes to the UI. See [INSTALL.md](INSTALL.md) for a more detailed guide with screenshots, also for integration of KoboToolbox with template.

1. Download the [latest release ZIP](extension.zip) from this repository.  
2. Log in as **Admin** in your EspoCRM instance.  
3. Go to **Administration ▸ Extensions ▸ Import**.  
4. Upload the ZIP file and Click `Install`
6. **Import data files:**  
   For every file in the [import folder](/import) of this repository, import it into EspoCRM:
   1. Go to **Administration ▸ Import**.
   2. Under **What to Import? > Entity Type**, select the entity that matches the file name.  
      - For example: if the file is `Roles.csv`, select `Roles`.
      - `koboconnect.csv` can be imported in the `Roles` entity, if Kobo is being used to collect data
   4. Click **Next**.
   5. Click **Run Import**.
7. **Make entities visible in the Navbar:**
   1. Go to **Administration ▸ User Interface ▸ General**.
   2. Change **Theme** to `Light` and `Top Navbar` 
   2. Go to **Administration ▸ User Interface ▸ Navbar**.
   4. Under **Tab List**, remove all entities listed and add the following in this order: `Feedback Data`, `...` and `Reports` 
   5. Save your changes. Now, you have adjusted the layout, you will see these entities in your Navbar and can access them easily at any time.
8. **Adjust general Settings:**
   1. Go to **Administration ▸ Settings ▸ Locale**
   2. Add your preferred timezones and date format
   3. Go to **Administration ▸ Settings ▸ General**
   4. Add `Feedback Data` and `Insight` to the 'Global Search Entity List'

---

## How to Use
At a high level, using the Feedback Management template typically involves the following steps:

1. Open the **Feedback Data** entity in EspoCRM.  
2. Click **Create Feedback** and fill in the form.  
   - Add feedback description, fill in fields and choose a status.  
   - Optionally assign to a team member.  
3. Feedback is now added and visible in a list view.  
4. Change feedback status as work progresses.  
5. Use the **Dashboard** to get an overview of all feedback (counts, status).  
6. For more examples and explanations, see [User Guide](/guides/user.md).

For more in-depth guides for specific roles, see the [Guides]() section.
- [**Admin Guide**](/guides/admin.md) -  Explains core administrative setup, including system configuration, basic entities, and initial settings required to operate the template.
- [**Cascading Selects Guide**](/guides/cascading-select.md) - Describes how hierarchical selections (e.g. administrative levels and coding frameworks) are structured, populated, and kept consistent using cascading selects.
- [**Kobo Integration Guide**](/guides/kobo-integration.md) - Covers how to integrate KoboToolbox forms with EspoCRM to ingest feedback data, including mapping fields and handling structured submissions.
- [**Qualitative Feedback Analysis (QFA) Guide**](/guides/qfa.md) - 
  Provides guidance on organising, coding, and analysing qualitative feedback, including the use of coding frameworks and analysis workflows.
- [**Roles and Teams Guide**](/guides/roles-and-teams.md) - 
  Explains how to configure user roles, teams, and permissions to support safe collaboration and separation of responsibilities.


---
## Terms of Use
* This extension is developed by [the Netherlands Red Cross' 510](https://www.510.global/) and is not officially supported by EspoCRM.
* It is free to use and modify, as specified in the [GNU AGPLv3 License](/LICENSE.md).
* It is provided as-is, without any warranty. Please ensure it works as intended before using it in a real humanitarian program.
* It is meant to be used as a starting point for organizations to build their own data management system. It is recommended to customize it to the specific needs of your organization.
* Suggestion for improvements? [Open an issue](https://github.com/rodekruis/espocrm-template-feedbackmanagement/issues) in GitHub.
* Need support or have any questions? Please [contact us](https://www.510.global/contact/). We cannot guarantee support, but we will do our best to help you.
