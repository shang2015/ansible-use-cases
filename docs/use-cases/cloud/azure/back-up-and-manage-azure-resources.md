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

## Notes

- Restore tests should be run regularly into an isolated resource group; do not rely only on the existence of recovery points.
- Resource locks, via `azure.azcollection.azure_rm_lock`, protect vaults from accidental deletion.
- Related: [Provision Azure networking and virtual machines](provision-azure-networking-and-virtual-machines.md).
