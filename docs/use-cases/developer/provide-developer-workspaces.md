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

## Notes

- Continue with [Test automation content](test-automation-content.md) and [Build CI/CD for automation content](build-cicd-for-automation-content.md).
- Image build and registration are detailed in [Build and manage execution environments](../platform/build-execution-environments.md).
- Keep the workstation baseline small. Every extra tool makes it harder to reproduce a problem.
- Hosted workspaces keep source code and credentials off laptops, which helps with contractors and regulated environments.
