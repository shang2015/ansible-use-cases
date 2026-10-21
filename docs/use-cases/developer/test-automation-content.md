---
title: Test automation content
summary: Lint, unit-test and integration-test playbooks, roles and platform configuration before they reach production.
order: 20
personas: [Automation developer, DevOps engineer, Quality engineer]
collections: [ansible.controller, ansible.utils, infra.aap_configuration_extended]
key_content:
  - ansible.controller.project_update
  - ansible.controller.job_launch
  - ansible.controller.job_wait
  - ansible.controller.workflow_launch
  - ansible.utils.validate
  - infra.aap_configuration_extended.aap_rules_validation
---

# Test automation content

## Description

Catch problems in automation before it touches production systems. Content passes style and syntax checks, role and collection tests, and finally a run in AAP against a lab inventory. The same checks run on a developer machine and in the pipeline, and a failed check blocks the merge.

## Notes

- Tests are only as good as the lab. For network and appliance content, use virtual devices or a shared lab with scheduled access.
- Linting and Molecule come with the Ansible development tools, not from a collection; this page lists the platform parts that connect them to AAP.
- Continue with [Build CI/CD for automation content](build-cicd-for-automation-content.md) to chain the tests with promotion.
- Event-Driven Ansible can start the integration tests when a push or pull request event arrives, in place of polling.
