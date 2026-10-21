---
title: Build CI/CD for automation content
summary: Run tests, update projects and promote automation from development to production through Git events, webhooks and workflows.
order: 30
personas: [DevOps engineer, Automation developer, Platform engineer]
collections: [ansible.scm, ansible.controller, ansible.hub, ansible.eda]
key_content:
  - ansible.scm.git_retrieve
  - ansible.scm.git_publish
  - ansible.controller.project
  - ansible.controller.project_update
  - ansible.controller.job_template
  - ansible.controller.workflow_job_template
  - ansible.eda.webhook
examples:
  - title: Ansible validated GitHub workflows
    url: https://github.com/redhat-cop/infra.ansible_validated_workflows
    note: reusable CI workflows for automation content repositories
  - title: ansible.scm collection
    url: https://github.com/ansible-collections/ansible.scm
    note: git_retrieve and git_publish modules
---

# Build CI/CD for automation content

## Description

Treat playbooks, roles and collections like software. A merge in Git triggers the tests, updates the project in Automation Platform, and promotes the same version through development, test and production environments with approvals where needed. Nobody edits content on the controller.

## Notes

- Related: [Test automation content](test-automation-content.md) and [Manage Automation Platform as code](../platform/manage-aap-as-code.md), which applies the same pipeline to the platform configuration.
- Keep webhook secrets and tokens in credentials, and rotate them; see [Rotate vaulted secrets and platform credentials](../platform/rotate-secrets-and-credentials.md).
- Use workflow approval nodes for production gates; the approvals can be answered from an ITSM tool through the API.
- For large estates, prefer Git tags over branches for production so that what ran is always identifiable.
