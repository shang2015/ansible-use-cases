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

## Notes

- Combine with [Build CI/CD for automation content](build-cicd-for-automation-content.md) and [Test automation content](test-automation-content.md) so that migrated content stays maintainable.
- Use [Publish collections to automation hub](publish-collections-to-automation-hub.md) once shared roles exist.
- No Ansible collection converts Puppet, Chef or Salt code automatically; treat the old code as documentation of intent and verify with tests.
- Migrating from Tower or an older platform version is a different task: [Migrate from Ansible Tower or AAP 2.4 to AAP 2.5 and later](../platform/migrate-to-aap-2-5-or-later.md).
