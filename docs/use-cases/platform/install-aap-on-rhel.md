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

## Prerequisites

1. RHEL hosts that meet the sizing and port requirements for the chosen topology (single node growth or multi-node enterprise), with a service account that can use `become`.
2. A Red Hat subscription for Automation Platform and an offline API token to download the installer from the Customer Portal.
3. DNS names and TLS certificates and keys for the gateway, controller, hub and Event-Driven Ansible, plus a load balancer if more than one gateway node is used.
4. A PostgreSQL decision: installer-managed database, or an external PostgreSQL that is provisioned and reachable.
5. A bastion or control node with Ansible, from which the installation is run, and a Git repository for the inventory variables (secrets in Ansible Vault).

## Steps

1. Describe the topology in a variables file: which hosts take the gateway, controller, hub, Event-Driven Ansible, database and execution roles, and the passwords as vaulted variables.
2. Download the containerized installer, or setup bundle for disconnected sites, with `infra.aap_utilities.aap_setup_download`.
3. Prepare the installer directory and render the installation inventory with `infra.aap_utilities.aap_setup_prepare`.
4. Start the installation with `infra.aap_utilities.aap_setup_install` and keep the output as evidence.
5. Replace the self-signed certificates with the corporate ones using `infra.aap_utilities.aap_certs`, or set them in the inventory at install time.
6. Check that all services are running with `infra.aap_utilities.aap_manage_containerized_services` and `svc_action: status`.
7. Apply the subscription, then configure organizations, authentication, credentials and projects as code (see the related use case).
8. Optional: wrap steps 2-4 in `infra.automation_development_office.install_aap` with `install_aap_target: rhel` when the same install must be reused in several environments.

## Success Criteria

1. The gateway URL loads over HTTPS with a trusted certificate and an administrator can log in.
2. Controller, hub and Event-Driven Ansible are reachable through the gateway and report healthy.
3. All services report running on every node, including the database and Receptor.
4. The installation inventory and variables are in Git, with secrets encrypted.
5. A test job template runs successfully on an execution node.

## Notes

- Follow with [Manage Automation Platform as code](manage-aap-as-code.md), [Onboard teams with RBAC and single sign-on](onboard-teams-with-rbac-and-sso.md) and [Back up, restore and design HA and DR](back-up-restore-and-ha-dr.md).
- Execution and hop nodes for remote sites belong in the installation inventory; see [Scale and tune with automation mesh](scale-with-automation-mesh.md).
- The download and prepare roles also handle the RPM-based installer; check which installer the target release supports before choosing it.
- Keep the installer, inventory and `aap_manage_containerized_services` playbooks in one Git repository so that start, stop and restart for patch windows are also automated.
