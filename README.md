# Feedback Management 

## Introduction

**Feedback Management** is a data management solution based on EspoCRM for humanitarian organizations to manage feedback data of community members.

#### Why Feedback Management Template?
Management of feedback is a critical aspect of humanitarian work. It is essential to have a system that is **secure**, **easy to use**, **fast to set up**, and **customizable** to the needs of your organization. This Feedback Management Template is designed to meet these requirements by offering:
* A generic data model defining basic data tables and their relationships​
* A simple layout for ease of use​
* Standard user roles to control access down to individual records and fields​
* Workflows that automate operational processes​
* Integrations with other tools, such as Kobo
* Can work with other Templates for humanitarian use cases, such as the [People Affected Management (PAM) Template](https://github.com/rodekruis/espocrm-template-pam).

#### Why EspoCRM?
[EspoCRM](https://www.espocrm.com/) is an open-source data management system. It is highly customizable, directly from the user interface. It is free to use, lightweight, and has a large, supportive user community. For more information, visit the [EspoCRM Documentation](https://docs.espocrm.com/) and [510's EspoCRM knowledge base](https://github.com/rodekruis/EspoCRM-knowledge-base/wiki).


## Description

The Feedback Management Template consists of _Entities_, _Roles_ and _Teams_. 
* Entities are data structures that hold information (about feedback, people, programs, etc.).
* Roles are sets of permissions that define what each user can do in the system.
* Teams are groups of users 

#### Entities and their relationships:
* **Feedback Form**: can  
* **Report**: 
* **Dashboard**: 
* **Flowchart**: 

#### Roles:
* **CEA Focal Point/Officer**: can create, read, edit and delete all Feedback Forms; can create, read, edit, delete Reports
* **Branch Manager**: can create, read and edit all Feedback Forms related to the specific Branch; can read Reports related to the specific Branch
* **Director/Manager/Officer of Programs/Services**: ???
* **PMER**: can create, read, edit and delete Reports; can create, read, edit and delete Dashboards (collection of Reports)
* **Admin/IT/IM**: can create, read, edit and delete (almost) everything in the system
* **KoboConnect API**: automatic system role to be able to send Feedback Forms from KoboToolbox to EspoCRM; this will not be assigned to a user 

#### Teams (Default):
* **Sensitive Feedback**: are the only one that can see Feedback Forms that have been marked as sensitive. They can manage sensitive Feedback Forms and mark them as non-sensitive so that others can see these too. 
* **Branch XXX**: can see only the forms related to that branch location.

## Installation

> [!IMPORTANT]  
> Make sure to back up your EspoCRM instance before installing this extension.

1. If not done already, [install EspoCRM](https://docs.espocrm.com/administration/installation/).
2. Download the .zip file with the extension: [extension.zip](link).
2. Install the extension
    * Log in EspoCRM as an administrator.
    * Go to `Administration` > `Extensions`.
    * Select the .zip file with the extension.
    * Click `Install`.

> [!WARNING]  
> If you already have entities with the same names, the installation will overwrite them.
 
3. Make the entities visible in the `Navbar`:
    * Go to `Administration` > `User Interface`.
    * Under `Navbar` > `Tab List`, add the entities `Feedback Forms`, `Reports`, `Teams`, and `Users`.
4. For every file in the [import](/import) folder, import it in EspoCRM:
    * Go to `Administration` > `Import`.
    * Under `What to Import?` > `Entity Type`, select the entity corresponding to the file name; e.g. if the file name is `Roles.csv`, select `Roles`.
    * Click `Next`.
    * Click `Run Import`.

> [!WARNING]  
> If you already have records with the same names, the import will overwrite them.

## Terms of Use
* This extension is developed by [the Netherlands Red Cross' 510](https://www.510.global/) and is not officially supported by EspoCRM.
* It is free to use and modify, as specified in the [GNU AGPLv3 License](/LICENSE.md).
* It is provided as-is, without any warranty. Please ensure it works as intended before using it in a real humanitarian program.
* It is meant to be used as a starting point for organizations to build their own data management system. It is recommended to customize it to the specific needs of your organization.
* If you have any questions, please [contact us](https://www.510.global/contact/). We cannot guarantee support, but we will do our best to help you.


