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

## Prerequisites

1. Prism Central reachable from the execution environment, with a service account that has the roles needed for VM, image and network management.
2. Prism Central credentials stored in Automation Platform, and the `nutanix.ncp` collection in the execution environment.
3. Images (ISO or disk) uploaded or available by URL, and subnets or VPCs planned.
4. Category and protection policy design agreed with the backup and DR owners.

## Steps

1. Inventory the environment with `nutanix.ncp.ntnx_clusters_info_v2`, `nutanix.ncp.ntnx_hosts_info_v2` and `nutanix.ncp.ntnx_vms_info_v2`.
2. Import images with `nutanix.ncp.ntnx_images_v2`, and define subnets and VPCs with `nutanix.ncp.ntnx_subnets_v2` and `nutanix.ncp.ntnx_vpcs_v2`.
3. Create the VM with `nutanix.ncp.ntnx_vms_v2`, then adjust disks, NICs and cd-roms with `nutanix.ncp.ntnx_vms_disks_v2`, `nutanix.ncp.ntnx_vms_nics_v2` and `nutanix.ncp.ntnx_vms_cd_rom_v2`. Use `nutanix.ncp.ntnx_vms_stage_guest_customization_v2` for first-boot configuration.
4. Associate categories with `nutanix.ncp.ntnx_vms_categories_v2` so protection, security and ownership policies apply by category.
5. Define protection with `nutanix.ncp.ntnx_protection_policies_v2`, take recovery points with `nutanix.ncp.ntnx_recovery_points_v2`, and test a restore with `nutanix.ncp.ntnx_recovery_point_restore_v2`.
6. Run operational actions with `nutanix.ncp.ntnx_vms_power_actions_v2`, `nutanix.ncp.ntnx_vms_clone_v2` and `nutanix.ncp.ntnx_vm_revert_v2`.
7. Enforce placement rules with `nutanix.ncp.ntnx_vm_anti_affinity_policy_v2` and `nutanix.ncp.ntnx_vm_host_affinity_policy_v2`.
8. Hand the new VM to the normal OS configuration job templates.

## Success Criteria

1. A VM request produces a running AHV VM on the right cluster, subnet and categories.
2. Protection policies cover all VMs in the protected categories, and a restore test succeeds.
3. Anti-affinity and host-affinity rules are present and reported as compliant.
4. Inventory reports show clusters, hosts and VMs with current state.

## Notes

- The collection contains older v1 modules (without the `_v2` suffix) and newer v4 API modules (`_v2`). Choose one family per project and check which Prism Central versions it supports.
- It also covers Nutanix Database Service (`ntnx_ndb_*` modules), Foundation imaging (`ntnx_foundation*`) and Karbon Kubernetes clusters (`ntnx_karbon_*`).
- Compare with [Provision VMware virtual machines](provision-vmware-virtual-machines.md) when running both platforms side by side.
- Hyper-V and SCVMM hosts are covered by the `microsoft.hyperv` and `microsoft.scvmm` collections; see the Windows use cases for those platforms. Other certified options include `scale_computing.hypercore` for Scale Computing HyperCore and `redhat.rhv` for existing Red Hat Virtualization (oVirt) environments.
