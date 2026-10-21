---
title: Migrate from Ansible Tower or AAP 2.4 to AAP 2.5 and later
summary: Move configuration, authentication, execution environments and integrations from Tower or AAP 2.4 to a new platform gateway based deployment.
order: 90
personas: [Platform engineer, Solution architect, Automation lead]
collections: [ansible.controller, ansible.platform, infra.aap_configuration, infra.aap_configuration_extended, infra.ee_utilities, infra.aap_utilities]
key_content:
  - ansible.controller.export
  - ansible.controller.import
  - infra.aap_configuration_extended.filetree_create
  - infra.aap_configuration_extended.upgrade_config
  - infra.aap_configuration.dispatch
  - infra.ee_utilities.virtualenv_migrate
  - ansible.platform.authenticator
  - infra.aap_utilities.aap_backup
examples:
  - title: infra.aap_configuration_extended validated collection
    url: https://github.com/redhat-cop/aap_configuration_extended/
    note: filetree_create and upgrade_config roles for exporting and converting configuration
---

# Migrate from Ansible Tower or AAP 2.4 to AAP 2.5 and later

## Description

Move an existing Ansible Tower or Automation Platform 2.4 deployment to Automation Platform 2.5 or later, where the platform gateway fronts the controller, hub and Event-Driven Ansible. Ansible exports the objects, converts the authentication settings to gateway authenticators, rebuilds custom environments as execution environments and applies everything to a clean target, so the old and new platforms can run side by side until cut-over.

## Notes

- API paths change with the gateway: controller endpoints are served under the gateway URL (for example `/api/controller/v2/`). Update scripts and external tools.
- Secrets in credentials are not exported in clear text. Plan to re-supply them from the vault or external secret manager, and consider moving them to credential input sources.
- If the source is already on a containerized or operator-based 2.6 deployment and only the platform changes, use [Move Automation Platform between installation types](move-aap-between-installation-types.md).
- Managing the target as code from day one avoids repeating the migration for the next upgrade: [Manage Automation Platform as code](manage-aap-as-code.md).
- Event-Driven Ansible rulebook activations and decision environments are recreated on the target; review rulebook sources and credentials after the move.
