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

## Prerequisites

1. vCenter credentials in Automation Platform with rights for snapshot, power and reconfigure operations on the target VMs.
2. A VM inventory, for example from the `vmware.vmware.vms` inventory plugin, grouped by folder, cluster or tag.
3. A snapshot policy: naming convention, maximum age and who may revert.
4. For decommissioning, an agreed retention step such as a backup or OVF export.

## Steps

1. Gather the current state with `vmware.vmware.vm_info` and `vmware.vmware.vm_snapshot_info`, and publish the list of VMs with snapshots as a report.
2. Create a pre-change snapshot with `vmware.vmware.vm_snapshot`, or the `cloud.vmware_ops.snapshot_management` role, using a name that carries the change ticket number.
3. Run the change (patching, application upgrade or configuration job) as the next step of a workflow.
4. On failure, revert with `vmware.vmware.vm_snapshot_revert`. On success, remove the snapshot with `vmware.vmware.vm_snapshot`.
5. Schedule a clean-up job that finds snapshots older than the policy limit and removes them, with a notification to the VM owner first.
6. Handle other lifecycle actions with `vmware.vmware.vm_powerstate`, `vmware.vmware.vm` (resize or delete), `vmware.vmware.vm_advanced_settings` and `vmware.vmware.vm_resource_info`.
7. Before deleting a VM, export it with `cloud.vmware_ops.export_vm_as_ovf` (the VM must be powered off) or confirm a current backup exists.
8. Record the result in the CMDB or ticket as the final workflow node.

## Success Criteria

1. Every change window has a named pre-change snapshot, and a failed change is reverted by the workflow.
2. No snapshot older than the policy limit remains in the inventory.
3. A report lists all VMs with snapshots, their age and owner.
4. Decommissioned VMs have a retained export or backup reference before deletion.

## Notes

- VMware snapshots are not backups; keep them short-lived and use a backup product for retention. See [Manage Nutanix clusters and VMs](manage-nutanix-clusters-and-vms.md) for the equivalent recovery point approach on AHV.
- Use `vmware.vmware.vm_snapshot_info` in a check step so a job fails safely when a VM already carries more snapshots than policy allows.
- The `cloud.vmware_ops.snapshot_management` collection playbooks provide ready-made create, remove, remove-all and revert entry points.
- Pair with [Provision VMware virtual machines](provision-vmware-virtual-machines.md) for the build side of the lifecycle.
