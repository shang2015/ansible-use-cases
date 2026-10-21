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

## Notes

- Use `microsoft.hyperv` for standalone hosts or clusters managed directly. Use `microsoft.scvmm` where System Center VMM is the control point, so changes stay visible in VMM.
- Hyper-V replication (`microsoft.hyperv.hv_replication`) and shielded VMs (`microsoft.hyperv.hv_shielded_vm`) are available in the same collection for disaster recovery and security scenarios.
- Checkpoints are not a backup. Remove them promptly; long-lived checkpoints affect performance and disk use.
- Other hypervisors are covered in the virtualization use cases.
