---
title: Build and manage execution environments
summary: Build execution environment images in a pipeline, publish them to automation hub and register them in the controller.
order: 60
personas: [Platform engineer, Automation developer, DevOps engineer]
collections: [infra.ee_utilities, ansible.hub, ansible.controller, infra.automation_development_office]
key_content:
  - infra.ee_utilities.ee_builder
  - infra.ee_utilities.create_execution_environment
  - infra.ee_utilities.virtualenv_migrate
  - ansible.hub.ah_ee_repository
  - ansible.hub.ah_ee_registry
  - ansible.controller.execution_environment
  - infra.automation_development_office.aap_build_ee
---

# Build and manage execution environments

## Description

Package the Ansible runtime, collections and Python or system dependencies a team needs into a container image, test it, publish it to private automation hub and make it selectable in the controller. Ansible runs the build the same way every time, so jobs behave the same on a laptop, in a pipeline and on an execution node.

## Notes

- Pair with [Publish collections to automation hub](../developer/publish-collections-to-automation-hub.md) so that collections land in hub before the image build consumes them.
- Keep the number of images small: a few purpose-based images (for example one per technology domain) are easier to patch than one per team.
- Use [Manage Automation Platform as code](manage-aap-as-code.md) to register the images, hub repositories and job template assignments.
- Disconnected sites push the built images to an internal registry and sync hub content offline.
