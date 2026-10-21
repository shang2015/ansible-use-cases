---
title: Manage Nutanix clusters and VMs
summary: Provision and operate AHV virtual machines, images, networks, categories and protection policies on Nutanix through Prism Central.
order: 60
personas: [Virtualization administrator, Infrastructure engineer]
collections: [nutanix.ncp]
key_content:
  - nutanix.ncp.ntnx_vms_v2
  - nutanix.ncp.ntnx_vms_power_actions_v2
  - nutanix.ncp.ntnx_images_v2
  - nutanix.ncp.ntnx_subnets_v2
  - nutanix.ncp.ntnx_categories_v2
  - nutanix.ncp.ntnx_protection_policies_v2
  - nutanix.ncp.ntnx_recovery_points_v2
  - nutanix.ncp.ntnx_vms_info_v2
examples:
  - title: Nutanix Ansible collection
    url: https://github.com/nutanix/nutanix.ansible
---

# Manage Nutanix clusters and VMs

## Description

Automate the Nutanix AHV estate from Prism Central: create VMs from images, attach networks and disks, apply categories and protection policies, take recovery points and run power operations. The same job templates can serve self-service requests and scheduled maintenance.

## Notes

- The collection contains older v1 modules (without the `_v2` suffix) and newer v4 API modules (`_v2`). Choose one family per project and check which Prism Central versions it supports.
- It also covers Nutanix Database Service (`ntnx_ndb_*` modules), Foundation imaging (`ntnx_foundation*`) and Karbon Kubernetes clusters (`ntnx_karbon_*`).
- Compare with [Provision VMware virtual machines](provision-vmware-virtual-machines.md) when running both platforms side by side.
- Hyper-V and SCVMM hosts are covered by the `microsoft.hyperv` and `microsoft.scvmm` collections; see the Windows use cases for those platforms. Other certified options include `scale_computing.hypercore` for Scale Computing HyperCore and `redhat.rhv` for existing Red Hat Virtualization (oVirt) environments.
