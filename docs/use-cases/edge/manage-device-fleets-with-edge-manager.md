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

## Notes

- Roll out in stages: update a canary fleet or label first, then widen the change after status checks.
- Pair with [Deploy MicroShift at the edge](deploy-microshift-at-the-edge.md) when the devices run Kubernetes workloads.
- Use Event-Driven Ansible to trigger an enrollment approval or a rollback job when device status events arrive from your monitoring system.
