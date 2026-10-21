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

## Notes

- Pair with [Onboard teams with RBAC and single sign-on](onboard-teams-with-rbac-and-sso.md) for the access model and [Build and manage execution environments](build-execution-environments.md) for the images the code refers to.
- `object_diff` can remove objects that are not in Git. Run it in report mode first and use `protect_not_empty_orgs` while the model is being adopted.
- Use Event-Driven Ansible to trigger the configuration job when a Git push event arrives, instead of polling.
- For releases earlier than 2.5, `infra.controller_configuration` holds the previous format; see [Migrate from Ansible Tower or AAP 2.4 to AAP 2.5 and later](migrate-to-aap-2-5-or-later.md).
