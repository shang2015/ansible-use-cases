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

## Prerequisites

1. A build host with `podman` (or Docker) and `ansible-builder`, or an execution environment that can run them.
2. Access to the Red Hat registry for the base images, and a private automation hub or other registry to push to.
3. The list of collections, Python packages and system packages each team requires, with versions.
4. Credentials for the registry and for the controller or gateway, stored as platform credentials.
5. A Git repository to hold the build definitions.

## Steps

1. Capture each image definition as variables: name, base image, collection requirements, Python requirements and system packages.
2. For legacy Tower or AAP 1.x environments, run `infra.ee_utilities.virtualenv_migrate` on the node to derive the Python requirements from the custom virtual environments.
3. Build the images with the `infra.ee_utilities.ee_builder` role or the `infra.ee_utilities.create_execution_environment` playbook; `infra.automation_development_office.aap_build_ee` is an alternative that also accepts locally built collection archives.
4. Push the images to private automation hub, after defining the repository with `ansible.hub.ah_ee_repository` and, for mirrored images, a remote registry with `ansible.hub.ah_ee_registry`.
5. Register each image in the controller with `ansible.controller.execution_environment`, set the pull policy, and assign it to organizations, projects or job templates.
6. Run a representative job template with each new image before it replaces the previous tag.
7. Rebuild on a schedule or when a base image or collection is updated, and keep older tags for rollback.

## Success Criteria

1. Every execution environment in use is built from a definition in Git.
2. Images are stored in private automation hub, and the controller pulls them from there.
3. A job template running with the new image produces the same results as with the previous one.
4. No job depends on a custom virtual environment on a controller node.
5. A rebuild after a collection update takes one pipeline run.

## Notes

- Pair with [Publish collections to automation hub](../developer/publish-collections-to-automation-hub.md) so that collections land in hub before the image build consumes them.
- Keep the number of images small: a few purpose-based images (for example one per technology domain) are easier to patch than one per team.
- Use [Manage Automation Platform as code](manage-aap-as-code.md) to register the images, hub repositories and job template assignments.
- Disconnected sites push the built images to an internal registry and sync hub content offline.
