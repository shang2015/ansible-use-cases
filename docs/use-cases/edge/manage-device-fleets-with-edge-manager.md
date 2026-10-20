---
title: Manage device fleets with Red Hat Edge Manager
summary: Enroll edge devices, group them into fleets and roll out operating system and configuration updates from Ansible.
order: 10
personas: [Edge platform engineer, Operations lead]
collections: [redhat.edge_manager]
key_content:
  - redhat.edge_manager.flightctl_resource
  - redhat.edge_manager.flightctl_resource_info
  - redhat.edge_manager.flightctl_certificate_management
  - redhat.edge_manager.flightctl_enrollment_config_info
  - redhat.edge_manager.flightctl_image_builder
  - redhat.edge_manager.flightctl
  - redhat.edge_manager.flightctl_console
examples:
  - title: Red Hat Edge Manager collection (Flight Control)
    url: https://github.com/flightctl/flightctl-ansible
    note: modules, inventory plugin and demo playbooks
---

# Manage device fleets with Red Hat Edge Manager

## Description

Manage thousands of edge devices as fleets instead of one by one. Red Hat Edge Manager (based on Flight Control) keeps each device on the operating system image and configuration declared for its fleet; Ansible creates the fleets, approves new devices and changes the desired state, and Edge Manager rolls it out to the devices.

## Prerequisites

1. A running Red Hat Edge Manager service with an API version supported by the collection (1.3 or later), and credentials for it stored as an automation controller credential.
2. An execution environment with `redhat.edge_manager` and its Python requirements; the collection requires Python 3.12 or later and, on Automation Platform, release 2.5.20250326 or later.
3. OS images in a container registry that devices can reach, for example built with the process in [Build and update edge OS images](build-and-update-edge-os-images.md).
4. A fleet design: labels for site, hardware type and role, and the update policy for each fleet.

## Steps

1. Read the enrollment settings the devices need with `redhat.edge_manager.flightctl_enrollment_config_info` and bake them into the device image or provisioning process.
2. Define each fleet as code with `redhat.edge_manager.flightctl_resource` (`kind: Fleet`), including the target OS image and the configuration to apply, and store the definitions in Git.
3. Approve enrollment requests for devices that pass your checks with `redhat.edge_manager.flightctl_certificate_management`, applying labels so devices land in the right fleet.
4. List devices and fleets and their status with `redhat.edge_manager.flightctl_resource_info`, or use the `redhat.edge_manager.flightctl` inventory plugin to run other playbooks against enrolled devices.
5. Roll out a new OS image by changing the fleet's OS image reference and running the job again. Watch device status through `flightctl_resource_info` until devices report the new version.
6. Build images through the Image Builder service with `redhat.edge_manager.flightctl_image_builder` (`ImageBuild` and `ImageExport` resources), and run the same job from a workflow before the fleet update.
7. For troubleshooting, run commands on a device through the `redhat.edge_manager.flightctl_console` connection plugin.

## Success Criteria

1. Every enrolled device belongs to a fleet and reports its status.
2. Fleet definitions in Git match the resources in Edge Manager.
3. A change to the fleet OS image reaches all devices of that fleet, and devices that fail to update are listed.
4. New devices are approved and labelled without manual console work.

## Notes

- Roll out in stages: update a canary fleet or label first, then widen the change after status checks.
- Pair with [Deploy MicroShift at the edge](deploy-microshift-at-the-edge.md) when the devices run Kubernetes workloads.
- Use Event-Driven Ansible to trigger an enrollment approval or a rollback job when device status events arrive from your monitoring system.
