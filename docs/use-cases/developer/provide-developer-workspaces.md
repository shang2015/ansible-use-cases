---
title: Provide standard automation developer workspaces
summary: Give automation developers a ready workstation or browser-based workspace with the editor, Ansible development tools and the same execution environment as production.
order: 10
personas: [Automation developer, DevOps engineer, Platform engineer]
collections: [infra.automation_development_office, infra.ee_utilities]
key_content:
  - infra.automation_development_office.ocp_devspaces
  - infra.automation_development_office.ocp_dev_hub
  - infra.automation_development_office.install_gitlab
  - infra.automation_development_office.aap_build_ee
  - infra.ee_utilities.ee_builder
---

# Provide standard automation developer workspaces

## Description

Make the first day of a new automation developer short and the results consistent. Every developer works in the same editor setup with the same Ansible development tools and runs content in the same execution environment image that production uses, either on the laptop or in a browser-based workspace hosted on OpenShift.

## Prerequisites

1. A source control system for automation content (GitHub, GitLab or similar) and a decision on branching and review rules.
2. Access to the Red Hat registry and private automation hub for the execution environment image and the collections.
3. For hosted workspaces: an OpenShift cluster with cluster-admin access to install the Dev Spaces operator, and an identity provider.
4. A list of the tools every developer needs: editor with the Ansible extension, Ansible development tools (such as `ansible-navigator`, `ansible-lint` and `ansible-builder`), `podman`, and Git.
5. A small sample repository that shows the standard project layout.

## Steps

1. Choose the model: local workstations with a documented setup, hosted workspaces, or both.
2. Build the developer execution environment with `infra.ee_utilities.ee_builder` or `infra.automation_development_office.aap_build_ee`, using the same collection versions as the production images, and publish it to private automation hub.
3. For hosted workspaces, deploy OpenShift Dev Spaces with `infra.automation_development_office.ocp_devspaces`, set the default workspace image and replace the sample projects with the team's own starter repositories.
4. Optional: publish a developer portal with starter templates and documentation using `infra.automation_development_office.ocp_dev_hub`, and a Git host with `infra.automation_development_office.install_gitlab` where none exists.
5. Ship the standard configuration in the repository: `ansible.cfg`, a navigator settings file that points to the execution environment, lint rules and editor settings.
6. Write a short onboarding guide: clone, open the workspace, run a sample playbook with the execution environment, commit and open a pull request.
7. Update the image and the template on a schedule so developers get new collection versions in a controlled way.

## Success Criteria

1. A new developer runs the sample playbook in the execution environment within the first hour.
2. A playbook that runs in the workspace runs in the controller with the same result.
3. Lint results are the same locally and in the pipeline.
4. Workspaces and starter repositories are created from code, not by hand.

## Notes

- Continue with [Test automation content](test-automation-content.md) and [Build CI/CD for automation content](build-cicd-for-automation-content.md).
- Image build and registration are detailed in [Build and manage execution environments](../platform/build-execution-environments.md).
- Keep the workstation baseline small. Every extra tool makes it harder to reproduce a problem.
- Hosted workspaces keep source code and credentials off laptops, which helps with contractors and regulated environments.
