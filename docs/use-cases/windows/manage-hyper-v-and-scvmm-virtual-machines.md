---
title: Manage Hyper-V and SCVMM virtual machines
summary: Create, change, protect and move virtual machines on Hyper-V hosts and clusters, directly or through System Center VMM.
order: 70
personas: [Virtualization administrator, Windows administrator]
collections: [microsoft.hyperv, microsoft.scvmm]
key_content:
  - microsoft.hyperv.hv_vm
  - microsoft.hyperv.hv_vm_state
  - microsoft.hyperv.hv_checkpoint
  - microsoft.hyperv.hv_vm_move
  - microsoft.hyperv.hv_cluster_node_maintenance
  - microsoft.scvmm.scvmm_vm
  - microsoft.scvmm.scvmm_template
  - microsoft.scvmm.scvmm_vm_checkpoint
---

# Manage Hyper-V and SCVMM virtual machines

## Description

Run the virtual machine lifecycle on Microsoft virtualization from Automation Platform: create VMs from standard definitions or templates, adjust CPU, memory, disks and networks, take checkpoints before changes, power VMs on and off, and move them off hosts before maintenance.

## Prerequisites

1. Hyper-V hosts or clusters reachable over WinRM, or an SCVMM server (the SCVMM collection targets SCVMM 2022) with an account that has the required roles.
2. VM definitions or templates: sizing, VHD or VHDX sources, virtual switches, VLANs and naming.
3. Storage and network capacity for the planned VMs.
4. Credentials stored as automation controller credentials, with the PowerShell modules for Hyper-V or VMM available on the managed node.

## Steps

1. Build the inventory of existing VMs and hosts with `microsoft.hyperv.hv_vm_info` and `microsoft.hyperv.hv_host_info`, or with the `microsoft.scvmm.scvmm_inventory` inventory plugin for SCVMM-managed environments.
2. Create virtual switches and disks with `microsoft.hyperv.hv_vswitch` and `microsoft.hyperv.hv_vhd`, then create VMs with `microsoft.hyperv.hv_vm`. In SCVMM, deploy from a template with `microsoft.scvmm.scvmm_template` and `microsoft.scvmm.scvmm_vm`, or copy an existing VM with `microsoft.scvmm.scvmm_vm_clone`.
3. Adjust resources with the specific modules, for example `microsoft.hyperv.hv_processor`, `microsoft.hyperv.hv_memory` and `microsoft.hyperv.hv_network_adapter`.
4. Wait for the guest with `microsoft.hyperv.hv_vm_guest_wait`, then run first-boot configuration with `microsoft.hyperv.hv_guest_command` or the standard Windows or Linux playbooks.
5. Take a checkpoint before a risky change with `microsoft.hyperv.hv_checkpoint` or `microsoft.scvmm.scvmm_vm_checkpoint`, and remove it after sign-off.
6. Control power state with `microsoft.hyperv.hv_vm_state` or `microsoft.scvmm.scvmm_vm_state`.
7. For host maintenance, drain a clustered host with `microsoft.hyperv.hv_cluster_node_maintenance` and live-migrate VMs with `microsoft.hyperv.hv_vm_move` (or `microsoft.scvmm.scvmm_vm_migrate`).
8. Run the create and decommission jobs from a self-service request with a survey for name, size and network.

## Success Criteria

1. A requested VM is created with the specified CPU, memory, disk and network and is reachable by name.
2. Checkpoints exist for each change window and are removed afterwards.
3. VMs are moved off a host before maintenance without service interruption beyond what live migration allows.
4. The inventory of VMs and hosts is current at the start of every run.

## Notes

- Use `microsoft.hyperv` for standalone hosts or clusters managed directly. Use `microsoft.scvmm` where System Center VMM is the control point, so changes stay visible in VMM.
- Hyper-V replication (`microsoft.hyperv.hv_replication`) and shielded VMs (`microsoft.hyperv.hv_shielded_vm`) are available in the same collection for disaster recovery and security scenarios.
- Checkpoints are not a backup. Remove them promptly; long-lived checkpoints affect performance and disk use.
- Other hypervisors are covered in the virtualization use cases.
