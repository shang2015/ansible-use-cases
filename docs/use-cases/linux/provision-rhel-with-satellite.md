---
title: Provision RHEL with Satellite
summary: Build new RHEL hosts on bare metal, virtual platforms or clouds from Satellite host groups, then configure them automatically.
order: 40
personas: [Linux administrator, Virtualization administrator, Platform engineer]
collections: [redhat.satellite, redhat.rhel_system_roles]
key_content:
  - redhat.satellite.host
  - redhat.satellite.hostgroup
  - redhat.satellite.compute_resource
  - redhat.satellite.provisioning_template
  - redhat.satellite.subnet
  - redhat.satellite.host_power
  - redhat.satellite.wait_for_task
  - redhat.satellite.registration_command
---

# Provision RHEL with Satellite

## Description

Turn a request for a server into a repeatable build. Satellite holds the provisioning building blocks (subnets, domains, installation media, partition tables, templates, compute resources and host groups); Ansible creates the host from them, waits for the build and hands it to the configuration playbooks.

## Notes

- Pair the post-build step with [Standardise RHEL configuration](standardise-rhel-configuration.md) so every host leaves provisioning compliant.
- Image-based provisioning uses images from [Build golden images with image builder](build-golden-images.md) or from the compute platform; define them with `redhat.satellite.image`.
- Capture all building blocks in Git with [Configure Satellite as code](configure-satellite-as-code.md).
- Use a survey or an ITSM request as the trigger so the requester supplies only the name, size and role.
