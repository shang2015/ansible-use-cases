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

## Prerequisites

1. Read-only (auditor) or administrator access to every existing controller or platform gateway, stored as credentials in the assessment instance.
2. A list of instances in scope, with versions, install types (RPM, containerized, operator) and whether each uses an external database.
3. SSH access to legacy Tower nodes if custom Python virtual environments must be inspected.
4. A Git repository to store the exported configuration and assessment output.

## Steps

1. Build an inventory of the instances in scope and record version, install type, node roles and Receptor topology.
2. Run `infra.aap_configuration.get_stats` against each instance to capture object totals, license usage and users from the controller metrics endpoint.
3. Export all objects to files with the `infra.aap_configuration_extended.filetree_create` role, or with `ansible.controller.export` for a single JSON document, filtered by organization where needed.
4. Pull job history with `ansible.controller.job_list` or the `ansible.controller.controller_api` lookup to find unused templates, failing templates, peak concurrency and the most active teams.
5. On Tower or AAP 1.x nodes, run `infra.ee_utilities.virtualenv_migrate` to list custom virtual environments and their Python requirements, so they can be rebuilt as execution environments.
6. List the external dependencies found in the export: credential types, inventory sources, projects and their Git hosts, collections and execution environment images.
7. Summarise the findings in a short report: target architecture, objects to migrate, objects to retire, and risks.

## Success Criteria

1. Every in-scope instance has a recorded version, install type, node count and object totals.
2. A Git repository holds a full export of each instance, with secrets replaced by variables.
3. Unused and failing job templates are listed with their last run date.
4. Every custom virtual environment is mapped to a planned execution environment.
5. The customer has signed off a scope list for the migration or consolidation.

## Notes

- Use the output as input for [Migrate from Ansible Tower or AAP 2.4 to AAP 2.5 and later](migrate-to-aap-2-5-or-later.md) and [Manage Automation Platform as code](manage-aap-as-code.md).
- Exports hold encrypted secret placeholders only. Re-enter or re-source credential secrets in the target; do not assume the export carries them.
- Review the usage figures with the owning teams before retiring anything. Low job counts can indicate quarterly or on-demand processes.
