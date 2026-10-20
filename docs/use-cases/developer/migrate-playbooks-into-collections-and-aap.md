---
title: Migrate existing playbooks into collections and AAP
summary: Move scripts, ad hoc playbooks and other tools' automation into structured roles, collections and controller job templates.
order: 50
personas: [Automation developer, Solution architect, Operations engineer]
collections: [ansible.controller, ansible.scm, infra.aap_configuration_extended, redhat.rhel_system_roles]
key_content:
  - ansible.controller.project
  - ansible.controller.inventory
  - ansible.controller.credential
  - ansible.controller.job_template
  - ansible.controller.workflow_job_template
  - infra.aap_configuration_extended.export_job_template_related
---

# Migrate existing playbooks into collections and AAP

## Description

Bring the automation that runs from laptops, cron jobs and shared servers into one governed place. Scripts and playbooks are cleaned up, split into roles and collections, stored in Git and run from Automation Platform as job templates with credentials, inventories, surveys and role-based access. The same approach applies to the logic held in other tools, such as Puppet, Chef or Salt.

## Prerequisites

1. An inventory of what exists: scripts, playbooks, cron entries, pipelines, and for other tools the manifests, cookbooks or states, with owners and run frequency.
2. A target Git repository layout and naming standards for roles and collections.
3. An Automation Platform with organizations, teams and an execution environment that meets the needs of the content.
4. Test systems on which each migrated item can be run and compared with the old behaviour.
5. Agreement on which items are retired instead of migrated.

## Steps

1. Triage the list: retire, migrate as-is, or rewrite. Start with the items that run most often or carry the most risk.
2. Put each item in Git and make it run unchanged under `ansible-playbook`, with variables and secrets separated from the code.
3. Refactor in small steps: replace shell commands with modules, move repeated logic into roles, use RHEL System Roles where one exists for the task, and move shared roles into a collection.
4. For logic coming from Puppet, Chef or Salt, describe the desired state of each managed object as a role with tests, rather than translating line by line; run both tools in parallel until results match.
5. Create the controller objects with `ansible.controller.project`, `ansible.controller.inventory` and `ansible.controller.credential`, then the run definitions with `ansible.controller.job_template` and chain related steps with `ansible.controller.workflow_job_template`.
6. Add surveys for the inputs that people used to type on the command line, and limit who can launch what with team roles.
7. To copy a template and its dependencies between instances, export it with `infra.aap_configuration_extended.export_job_template_related`.
8. Run old and new side by side on a test system, compare the result, then switch the cron job or ticket process to the job template and remove the old trigger.

## Success Criteria

1. Each migrated item runs from a job template, with the version of the code visible in the job.
2. Output and effect match the legacy method on the test systems.
3. No secrets remain in scripts or repositories.
4. The old trigger (cron, manual process, other tool) is disabled.
5. The owners can change the automation through a pull request.

## Notes

- Combine with [Build CI/CD for automation content](build-cicd-for-automation-content.md) and [Test automation content](test-automation-content.md) so that migrated content stays maintainable.
- Use [Publish collections to automation hub](publish-collections-to-automation-hub.md) once shared roles exist.
- No Ansible collection converts Puppet, Chef or Salt code automatically; treat the old code as documentation of intent and verify with tests.
- Migrating from Tower or an older platform version is a different task: [Migrate from Ansible Tower or AAP 2.4 to AAP 2.5 and later](../platform/migrate-to-aap-2-5-or-later.md).
