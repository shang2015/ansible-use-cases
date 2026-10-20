---
title: Back up and manage Azure resources
summary: Protect Azure VMs and disks with Azure Backup policies and snapshots, and manage storage and resource lifecycle.
order: 30
personas: [Cloud engineer, Backup administrator]
collections: [azure.azcollection, cloud.azure_ops]
key_content:
  - azure.azcollection.azure_rm_recoveryservicesvault
  - azure.azcollection.azure_rm_backuppolicy
  - azure.azcollection.azure_rm_backupazurevm
  - cloud.azure_ops.azure_manage_snapshot
  - azure.azcollection.azure_rm_snapshot
  - cloud.azure_ops.azure_manage_storage_account
---

# Back up and manage Azure resources

## Description

Put backup configuration for Azure virtual machines under automation: recovery vaults, policies and VM protection, plus snapshots for changes. Storage accounts and other resources are managed with the same definitions, so protection is not forgotten on new workloads.

## Prerequisites

1. An Azure credential in Automation Platform with rights on the vault and the VMs.
2. Backup requirements per workload class: frequency, retention and region.
3. A tagging convention or inventory group that marks the VMs to protect.
4. An execution environment with `azure.azcollection` and `cloud.azure_ops`.

## Steps

1. Create the recovery services vault with `azure.azcollection.azure_rm_recoveryservicesvault`.
2. Define the schedule and retention with `azure.azcollection.azure_rm_backuppolicy` (or `azure_rm_vmbackuppolicy`).
3. Enable protection for the VMs in the inventory with `azure.azcollection.azure_rm_backupazurevm`.
4. Take a snapshot before risky changes with the `cloud.azure_ops.azure_manage_snapshot` role or `azure.azcollection.azure_rm_snapshot`.
5. Manage storage accounts for exports and logs with the `cloud.azure_ops.azure_manage_storage_account` role.
6. Schedule a report listing VMs without protection, and open a ticket or auto-enable protection for them.

## Success Criteria

1. Every VM in scope is attached to a backup policy.
2. Recovery points are created on the policy schedule.
3. A pre-change snapshot exists for every change window and is removed after the retention period.
4. Unprotected VMs are reported within one schedule interval.

## Notes

- Restore tests should be run regularly into an isolated resource group; do not rely only on the existence of recovery points.
- Resource locks, via `azure.azcollection.azure_rm_lock`, protect vaults from accidental deletion.
- Related: [Provision Azure networking and virtual machines](provision-azure-networking-and-virtual-machines.md).
