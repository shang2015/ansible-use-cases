---
title: Assess the current automation estate
summary: Inventory existing Tower or Automation Platform instances, their objects, usage and dependencies before a migration, upgrade or consolidation.
order: 10
personas: [Solution architect, Automation lead, Platform owner]
collections: [ansible.controller, ansible.platform, infra.aap_configuration, infra.aap_configuration_extended, infra.ee_utilities]
key_content:
  - infra.aap_configuration.get_stats
  - ansible.controller.export
  - infra.aap_configuration_extended.filetree_create
  - ansible.controller.job_list
  - ansible.controller.controller_api
  - infra.ee_utilities.virtualenv_migrate
---

# Assess the current automation estate

## Description

Before moving, consolidating or scaling an Ansible deployment, the team needs facts instead of estimates: how many controllers exist, which version they run, what objects they hold, who uses them and what the jobs depend on. Ansible collects these facts from the platform APIs and produces a baseline that drives sizing, migration scope and clean-up.

## Notes

- Use the output as input for [Migrate from Ansible Tower or AAP 2.4 to AAP 2.5 and later](migrate-to-aap-2-5-or-later.md) and [Manage Automation Platform as code](manage-aap-as-code.md).
- Exports hold encrypted secret placeholders only. Re-enter or re-source credential secrets in the target; do not assume the export carries them.
- Review the usage figures with the owning teams before retiring anything. Low job counts can indicate quarterly or on-demand processes.
