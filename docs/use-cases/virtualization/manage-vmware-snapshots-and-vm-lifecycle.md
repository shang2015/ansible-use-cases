---
title: Manage VMware snapshots and VM lifecycle
summary: Take, report on, revert and clean up VM snapshots, and run power, resize and decommission operations from one controlled workflow.
order: 20
personas: [Virtualization administrator, Operations lead]
collections: [vmware.vmware, cloud.vmware_ops]
key_content:
  - vmware.vmware.vm_snapshot
  - vmware.vmware.vm_snapshot_info
  - vmware.vmware.vm_snapshot_revert
  - vmware.vmware.vm_powerstate
  - vmware.vmware.vm_info
  - cloud.vmware_ops.snapshot_management
  - cloud.vmware_ops.export_vm_as_ovf
---

# Manage VMware snapshots and VM lifecycle

## Description

Give operations teams one governed path for the routine things done to existing VMs: snapshot before a change, roll back if it fails, remove stale snapshots, resize, power cycle, export and delete. Using Automation Platform adds approvals, logging and consistent naming, and stops forgotten snapshots from consuming datastore space.

## Notes

- VMware snapshots are not backups; keep them short-lived and use a backup product for retention. See [Manage Nutanix clusters and VMs](manage-nutanix-clusters-and-vms.md) for the equivalent recovery point approach on AHV.
- Use `vmware.vmware.vm_snapshot_info` in a check step so a job fails safely when a VM already carries more snapshots than policy allows.
- The `cloud.vmware_ops.snapshot_management` collection playbooks provide ready-made create, remove, remove-all and revert entry points.
- Pair with [Provision VMware virtual machines](provision-vmware-virtual-machines.md) for the build side of the lifecycle.
