---
title: Install Automation Platform on RHEL
summary: Deploy a containerized Ansible Automation Platform on RHEL hosts with the platform gateway, controller, hub and Event-Driven Ansible, driven by an inventory kept in Git.
order: 20
personas: [Platform engineer, Solution architect, Linux administrator]
collections: [infra.aap_utilities, infra.automation_development_office]
key_content:
  - infra.aap_utilities.aap_setup_download
  - infra.aap_utilities.aap_setup_prepare
  - infra.aap_utilities.aap_setup_install
  - infra.aap_utilities.aap_certs
  - infra.aap_utilities.aap_manage_containerized_services
  - infra.automation_development_office.install_aap
examples:
  - title: infra.aap_utilities validated collection
    url: https://github.com/redhat-cop/aap_utilities/
    note: installer download, prepare, install, backup and service management roles
---

# Install Automation Platform on RHEL

## Description

Install Ansible Automation Platform on RHEL with the containerized installer, so the platform gateway, automation controller, automation hub and Event-Driven Ansible controller run as containers on the target hosts. Ansible downloads the installer, generates the installation inventory from variables kept in Git and runs the installation, which makes every environment repeatable.

## Notes

- Follow with [Manage Automation Platform as code](manage-aap-as-code.md), [Onboard teams with RBAC and single sign-on](onboard-teams-with-rbac-and-sso.md) and [Back up, restore and design HA and DR](back-up-restore-and-ha-dr.md).
- Execution and hop nodes for remote sites belong in the installation inventory; see [Scale and tune with automation mesh](scale-with-automation-mesh.md).
- The download and prepare roles also handle the RPM-based installer; check which installer the target release supports before choosing it.
- Keep the installer, inventory and `aap_manage_containerized_services` playbooks in one Git repository so that start, stop and restart for patch windows are also automated.
