---
title: Manage Automation Platform as code
summary: Hold the configuration of the gateway, controller, hub and Event-Driven Ansible controller in Git and apply, audit and promote it through pipelines.
order: 40
personas: [Platform engineer, Automation lead, DevOps engineer]
collections: [infra.aap_configuration, infra.aap_configuration_extended, ansible.platform, ansible.controller, ansible.hub, ansible.eda]
key_content:
  - infra.aap_configuration.dispatch
  - infra.aap_configuration_extended.filetree_create
  - infra.aap_configuration_extended.aap_config_vars
  - infra.aap_configuration_extended.aap_rules_validation
  - infra.aap_configuration_extended.object_diff
  - infra.aap_configuration.eda_rulebook_activations
  - ansible.platform.organization
  - ansible.controller.job_template
examples:
  - title: infra.aap_configuration validated collection
    url: https://github.com/redhat-cop/infra.aap_configuration/
    note: dispatch role and per-object roles for gateway, controller, hub and EDA
  - title: AAP configuration template
    url: https://github.com/redhat-cop/aap_configuration_template
    note: repository layout for per-environment configuration
---

# Manage Automation Platform as code

## Description

Describe organizations, teams, credentials, projects, inventories, job templates, hub content and Event-Driven Ansible rulebook activations as YAML in Git, and let Ansible create and update them. Changes then follow pull requests, review and promotion from test to production, and the live platform can be compared with Git to find manual changes.

## Prerequisites

1. A running Automation Platform 2.5+ instance and an administrator or token-based service account for the configuration jobs.
2. A Git repository with a layout for shared and per-environment configuration, and a place for secrets (Ansible Vault or an external secret manager through credential input sources).
3. An execution environment that contains `infra.aap_configuration`, `ansible.platform`, `ansible.controller`, `ansible.hub` and `ansible.eda`.
4. Agreement on ownership: which objects the platform team manages in code and which teams may still create in the UI.

## Steps

1. If the instance already has content, export it to files with `infra.aap_configuration_extended.filetree_create` to use as the starting point.
2. Structure the repository by object type and environment, and load the shared and environment folders with `infra.aap_configuration_extended.aap_config_vars`.
3. Apply the files with the `infra.aap_configuration.dispatch` role, which calls the gateway (for example `ansible.platform.organization`), controller (`ansible.controller.job_template`), hub and Event-Driven Ansible roles in dependency order. Use `infra.aap_configuration.eda_rulebook_activations` for decision environments, projects and rulebook activations.
4. Create a job template in the platform that runs the configuration playbook from the Git project, and trigger it from the pull request merge.
5. Validate configuration before applying with `infra.aap_configuration_extended.aap_rules_validation` and user-defined rules, for example that every organization sets a host limit or that default execution environments are not used.
6. Schedule `infra.aap_configuration_extended.object_diff` or the `controller_export_diff` module to report objects that exist in the platform but not in Git.
7. Promote the same code to production by changing only the environment folder and the credentials.

## Success Criteria

1. A new organization, team or job template is created by merging a pull request, with no UI step.
2. Re-running the configuration job reports no changes when nothing was edited.
3. The drift report lists no unmanaged objects, or each one has an owner and a decision.
4. Secrets are not stored in clear text in the repository.
5. A second environment is built from the same repository by switching the environment folder.

## Notes

- Pair with [Onboard teams with RBAC and single sign-on](onboard-teams-with-rbac-and-sso.md) for the access model and [Build and manage execution environments](build-execution-environments.md) for the images the code refers to.
- `object_diff` can remove objects that are not in Git. Run it in report mode first and use `protect_not_empty_orgs` while the model is being adopted.
- Use Event-Driven Ansible to trigger the configuration job when a Git push event arrives, instead of polling.
- For releases earlier than 2.5, `infra.controller_configuration` holds the previous format; see [Migrate from Ansible Tower or AAP 2.4 to AAP 2.5 and later](migrate-to-aap-2-5-or-later.md).
