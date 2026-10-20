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

## Prerequisites

1. Administrator access to the source and target arrays, and licences for snapshots, clones and replication.
2. For replication: network connectivity between sites, and peering or trust between arrays (cluster and SVM peering on ONTAP, remote system on PowerStore, array connection on FlashArray, partnerships on Storage Virtualize).
3. A protection standard: snapshot frequency and retention, RPO and RTO per tier, and a test schedule.
4. For backup, a Cohesity cluster with a protection source registered, if the backup tier is used.

## Steps

1. Define the snapshot policy per tier:
   - ONTAP `na_ontap_snapshot_policy`;
   - PowerStore `dellemc.powerstore.snapshotrule` and `protectionpolicy`;
   - PowerMax `dellemc.powermax.snapshotpolicy`;
   - FlashArray protection groups with `purefa_pg` and `purefa_pgsched`;
   - Storage Virtualize `ibm_sv_manage_snapshotpolicy`;
   - Hitachi `hv_snapshot` and `hv_snapshot_group`.
2. Attach the policy to the volumes, filesystems or consistency groups created by the provisioning jobs.
3. Create on-demand snapshots before changes with `na_ontap_snapshot`, `dellemc.powerstore.snapshot`, `dellemc.powermax.snapshot`, `purefa_pgsnap` or `ibm_sv_manage_snapshot`, and remove them when the change is closed.
4. Create clones for test and recovery with `na_ontap_volume_clone`, `ibm_sv_manage_clone`, `ibm_svc_manage_flashcopy` or `dellemc.powerflex.thin_clone`, then mount them to the target host.
5. Set up replication:
   - ONTAP `na_ontap_cluster_peer`, `na_ontap_vserver_peer` and `na_ontap_snapmirror` (or the `na_ontap_snapmirror_create` role);
   - PowerStore `replicationrule` and `replicationsession`;
   - PowerMax `dellemc.powermax.srdf`;
   - FlashArray `purefa_connect` and `purefa_pod_replica`;
   - Storage Virtualize `ibm_svc_manage_replication` and `ibm_sv_manage_replication_policy`;
   - Hitachi `hv_truecopy`, `hv_hur` and `hv_gad`.
6. Connect the backup tier: define policies and jobs with `cohesity.dataprotect.cohesity_policy` and `cohesity.dataprotect.cohesity_job`, and test restores with `cohesity.dataprotect.cohesity_restore_vm`.
7. Test recovery on a schedule: switch to the replica or restore a clone, run an application check, and fail back or discard the test copy. Report the achieved RPO.

## Success Criteria

1. All volumes in scope have the standard snapshot policy attached, and snapshots appear on schedule.
2. A clone can be created and mounted in test environments by a single job.
3. Replication relationships are healthy and the lag is within the RPO.
4. A recovery test is run and documented at the agreed interval.

## Notes

- Snapshots on the same array are not a backup; keep a separate copy, either through replication or a backup product.
- On Linux hosts without array integration, use the `infra.lvm_snapshots` roles (`snapshot_create`, `snapshot_revert`, `snapshot_remove`) for pre-change rollback points.
- Application consistency (quiescing databases, hypervisor snapshots) is added in the workflow before the array snapshot node.
- Pair with [Provision block storage](provision-block-storage.md) and [Provision file storage](provision-file-storage.md). For Kubernetes data, see [Back up Kubernetes applications](../kubernetes/back-up-kubernetes-applications.md).
- Event-Driven Ansible can start a failover or an extra snapshot when replication alarms are raised.
