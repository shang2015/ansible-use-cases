---
title: Manage snapshots, clones and replication
summary: Define snapshot schedules, create clones for test and recovery, set up array replication, and connect backups across storage vendors.
order: 30
personas: [Storage administrator, Backup administrator, Disaster recovery owner]
collections: [netapp.ontap, dellemc.powerstore, dellemc.powermax, dellemc.powerflex, everpure.flasharray, ibm.storage_virtualize, hitachivantara.vspone_block, cohesity.dataprotect, infra.lvm_snapshots]
key_content:
  - netapp.ontap.na_ontap_snapshot_policy
  - netapp.ontap.na_ontap_volume_clone
  - netapp.ontap.na_ontap_snapmirror
  - dellemc.powerstore.replicationsession
  - dellemc.powermax.srdf
  - everpure.flasharray.purefa_pg
  - ibm.storage_virtualize.ibm_svc_manage_flashcopy
  - hitachivantara.vspone_block.hv_snapshot
  - cohesity.dataprotect.cohesity_job
---

# Manage snapshots, clones and replication

## Description

Protect and reuse data with the array's own features: scheduled snapshots, writable clones for development and testing, and replication to a second array for disaster recovery. Automation Platform sets up the policies once, applies them to every new volume, and runs on-demand snapshots and clones as part of change and test workflows.

## Notes

- Snapshots on the same array are not a backup; keep a separate copy, either through replication or a backup product.
- On Linux hosts without array integration, use the `infra.lvm_snapshots` roles (`snapshot_create`, `snapshot_revert`, `snapshot_remove`) for pre-change rollback points.
- Application consistency (quiescing databases, hypervisor snapshots) is added in the workflow before the array snapshot node.
- Pair with [Provision block storage](provision-block-storage.md) and [Provision file storage](provision-file-storage.md). For Kubernetes data, see [Back up Kubernetes applications](../kubernetes/back-up-kubernetes-applications.md).
- Event-Driven Ansible can start a failover or an extra snapshot when replication alarms are raised.
