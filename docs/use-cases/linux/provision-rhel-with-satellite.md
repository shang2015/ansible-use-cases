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

## Prerequisites

1. A Satellite with synced RHEL repositories, a content view in a lifecycle environment and an activation key (see [Patch RHEL at scale](patch-rhel-at-scale.md)).
2. A Capsule or Satellite with the provisioning services (DHCP, DNS, TFTP) enabled for the target network, or a compute resource that provides them.
3. Credentials for the compute resource (VMware, a public cloud or another supported platform) if hosts are not bare metal.
4. Satellite credentials and an inventory source for Satellite in automation controller.

## Steps

1. Define the network and operating system building blocks: `redhat.satellite.domain`, `redhat.satellite.subnet`, `redhat.satellite.operatingsystem`, `redhat.satellite.installation_medium` and `redhat.satellite.partition_table`.
2. Add `redhat.satellite.provisioning_template` entries (kickstart, PXE, finish) and link them to the operating system with `redhat.satellite.os_default_template`.
3. Register the target platform with `redhat.satellite.compute_resource` and set sizing defaults in a compute profile.
4. Create a `redhat.satellite.hostgroup` per server role. It carries the operating system, content view, lifecycle environment, activation key and network defaults.
5. Create the host with `redhat.satellite.host`, with `build: true` and the host group. For virtual and cloud platforms, pass `compute_attributes`. For bare metal, use `redhat.satellite.discovery_rule` to assign discovered hosts to host groups.
6. Start or reboot into the build with `redhat.satellite.host_power`, and wait for Satellite tasks with `redhat.satellite.wait_for_task`.
7. Refresh the Satellite inventory, then run the post-build configuration play (system roles, application setup) against the new host.
8. For hosts that already exist, generate a global registration command with `redhat.satellite.registration_command` instead of rebuilding them.

## Success Criteria

1. A new host is built from the selected host group without console access.
2. It is registered to Satellite with the intended content view, lifecycle environment and activation key.
3. It appears in the Satellite inventory in automation controller and receives its post-build configuration.
4. The same job template creates different server roles by changing only the host group and name.

## Notes

- Pair the post-build step with [Standardise RHEL configuration](standardise-rhel-configuration.md) so every host leaves provisioning compliant.
- Image-based provisioning uses images from [Build golden images with image builder](build-golden-images.md) or from the compute platform; define them with `redhat.satellite.image`.
- Capture all building blocks in Git with [Configure Satellite as code](configure-satellite-as-code.md).
- Use a survey or an ITSM request as the trigger so the requester supplies only the name, size and role.
