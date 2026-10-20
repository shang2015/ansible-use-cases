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

## Prerequisites

1. A Git service (GitHub, GitLab, Bitbucket or similar) and a CI system, with a service account for the platform.
2. A repository layout and branching or tagging model, for example feature branches, a main branch for test and release tags for production.
3. Separate controller organizations, projects, inventories and credentials for development, test and production, or separate platform instances.
4. The test jobs from [Test automation content](test-automation-content.md).
5. A reachable callback address for webhooks, or an Event-Driven Ansible controller that can receive them.

## Steps

1. Create a project per environment with `ansible.controller.project`, each pointing at a branch or tag, and keep them in code.
2. Configure the Git service to send push and pull request events: either through the job template webhook settings of `ansible.controller.job_template`, or to an Event-Driven Ansible rulebook with the `ansible.eda.webhook` source.
3. On a pull request, run lint and role tests in CI, then sync the test project with `ansible.controller.project_update` and run the integration workflow built with `ansible.controller.workflow_job_template`.
4. On merge to main, deploy to the test environment automatically and run the acceptance workflow.
5. Promote to production by creating a release tag. The workflow updates the production project to that tag and includes an approval node before the first production job.
6. Use `ansible.scm.git_retrieve` and `ansible.scm.git_publish` in playbooks that must change repositories, for example to commit generated configuration or inventory, and push the change as a branch for review.
7. Publish collections and execution environment images in the same pipeline (see [Publish collections to automation hub](publish-collections-to-automation-hub.md)).
8. Record the version of content that ran in each job, and keep a rollback procedure: re-point the production project to the previous tag.

## Success Criteria

1. A merged pull request reaches the test environment without manual steps.
2. A release tag reaches production through an approval and the project shows the exact tag.
3. A bad release is rolled back by moving the production project to the previous tag.
4. Nobody has edit rights on content in the controller; all changes come from Git.
5. The pipeline status and the job link are visible on the pull request.

## Notes

- Related: [Test automation content](test-automation-content.md) and [Manage Automation Platform as code](../platform/manage-aap-as-code.md), which applies the same pipeline to the platform configuration.
- Keep webhook secrets and tokens in credentials, and rotate them; see [Rotate vaulted secrets and platform credentials](../platform/rotate-secrets-and-credentials.md).
- Use workflow approval nodes for production gates; the approvals can be answered from an ITSM tool through the API.
- For large estates, prefer Git tags over branches for production so that what ran is always identifiable.
