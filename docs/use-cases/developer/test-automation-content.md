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

## Prerequisites

1. A Git repository with the content and a branch strategy (feature branches, pull requests, protected main).
2. A lab or test inventory that mirrors production in kind: the same operating systems, network platforms or cloud account types, with disposable or snapshot-based systems.
3. A test project, inventory and credentials in the controller that cannot reach production.
4. A CI system (GitHub Actions, GitLab CI or similar) that can call the platform API and run the Ansible development tools.
5. Agreed quality rules: lint profile, required test coverage per role, naming and tagging rules.

## Steps

1. Lint every change with `ansible-lint` and a team profile, and run a syntax check; fail the pipeline on violations.
2. Test roles with Molecule scenarios that converge on a container or VM and verify the result, and test collections with `ansible-test` sanity and unit tests.
3. Validate data structures that feed the automation, such as variable files or API responses, against a schema with `ansible.utils.validate`.
4. In the pipeline, sync the test project with `ansible.controller.project_update` for the branch under test.
5. Launch the integration job template or workflow with `ansible.controller.job_launch` or `ansible.controller.workflow_launch`, then wait for the result with `ansible.controller.job_wait` and fail the pipeline on a failed status.
6. Run changes in check mode first, and run twice to prove idempotence: the second run must report no changes.
7. For platform configuration kept as code, run `infra.aap_configuration_extended.aap_rules_validation` to enforce rules before applying the configuration.
8. Publish test results as pipeline artifacts, and keep the test inventory clean by resetting it after each run.

## Success Criteria

1. Every pull request runs lint, role tests and an integration job automatically.
2. A change that breaks a role, fails lint or is not idempotent cannot be merged.
3. Integration tests run on the test inventory only; no production credentials are available there.
4. Test results are visible on the pull request.
5. Platform configuration changes are validated against the team's rules before being applied.

## Notes

- Tests are only as good as the lab. For network and appliance content, use virtual devices or a shared lab with scheduled access.
- Linting and Molecule come with the Ansible development tools, not from a collection; this page lists the platform parts that connect them to AAP.
- Continue with [Build CI/CD for automation content](build-cicd-for-automation-content.md) to chain the tests with promotion.
- Event-Driven Ansible can start the integration tests when a push or pull request event arrives, in place of polling.
