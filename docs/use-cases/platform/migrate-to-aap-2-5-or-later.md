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

## Prerequisites

1. The assessment output from [Assess the current automation estate](assess-automation-estate.md): object counts, custom virtual environments, integrations and users.
2. A new Automation Platform 2.5+ deployment, installed with [Install Automation Platform on RHEL](install-aap-on-rhel.md) or [Install Automation Platform on OpenShift](install-aap-on-openshift.md).
3. Administrator access to the source and target, and a recent backup of the source (see [Back up, restore and design HA and DR](back-up-restore-and-ha-dr.md)).
4. A list of external systems that call the platform API, webhooks, notification endpoints and credential sources, with their owners.
5. A freeze window for configuration changes on the source during the final sync.

## Steps

1. Back up the source with `infra.aap_utilities.aap_backup` so there is a way back.
2. Export the source configuration with `infra.aap_configuration_extended.filetree_create` (one file per object type, secrets as variables) or with `ansible.controller.export` for a single document.
3. Convert 2.4 style LDAP and SAML settings and the configuration files to the 2.5+ format with `infra.aap_configuration_extended.upgrade_config`, which writes gateway authenticators and authenticator maps.
4. For custom Python virtual environments, derive requirements with `infra.ee_utilities.virtualenv_migrate` (it reads the virtualenvs from a Tower / AAP 1.2 node) and build execution environments (see [Build and manage execution environments](build-execution-environments.md)).
5. Fill the secret variables from the secret store, review the files in a pull request, and apply them to the target with `infra.aap_configuration.dispatch`. Create authenticators (`ansible.platform.authenticator`) and organizations first. `ansible.controller.import` can load a single exported document where that is simpler.
6. Sync projects and inventory sources, and re-create anything that is not exportable, such as secrets entered in the UI and host-specific SSH trust.
7. Run the same representative job templates on both platforms and compare results, durations and notifications.
8. Cut over: point API clients, webhooks and pipelines to the new gateway URLs, move schedules, and disable the schedules on the source.
9. Keep the source read-only for an agreed period, then decommission it.

## Success Criteria

1. All in-scope organizations, teams, credentials, projects, inventories, templates and workflows exist on the target and match the export.
2. Users sign in through gateway authenticators with the same group mappings as before.
3. Every job template that is in scope completes on the new platform with the same result as on the source.
4. No job depends on a custom virtual environment.
5. API clients, notifications and webhooks work against the new URLs.
6. Schedules run on one platform only.

## Notes

- API paths change with the gateway: controller endpoints are served under the gateway URL (for example `/api/controller/v2/`). Update scripts and external tools.
- Secrets in credentials are not exported in clear text. Plan to re-supply them from the vault or external secret manager, and consider moving them to credential input sources.
- If the source is already on a containerized or operator-based 2.6 deployment and only the platform changes, use [Move Automation Platform between installation types](move-aap-between-installation-types.md).
- Managing the target as code from day one avoids repeating the migration for the next upgrade: [Manage Automation Platform as code](manage-aap-as-code.md).
- Event-Driven Ansible rulebook activations and decision environments are recreated on the target; review rulebook sources and credentials after the move.
