---
title: Decommission storage safely
summary: Retire volumes, shares and hosts in a safe order with evidence of non-use, backups, mapping removal and a recovery period before deletion.
order: 70
personas: [Storage administrator, Change manager]
collections: [netapp.ontap, dellemc.powerstore, dellemc.powermax, everpure.flasharray, ibm.storage_virtualize, hitachivantara.vspone_block, infinidat.infinibox, cisco.nxos]
key_content:
  - netapp.ontap.na_ontap_lun_map
  - netapp.ontap.na_ontap_volume
  - netapp.ontap.na_ontap_vserver_delete
  - dellemc.powermax.maskingview
  - dellemc.powerstore.volume
  - everpure.flasharray.purefa_volume
  - everpure.flasharray.purefa_zte
  - ibm.storage_virtualize.ibm_svc_vol_map
---

# Decommission storage safely

## Description

Remove storage that is no longer needed without breaking a workload or leaving data behind. The workflow proves that the volume is unused, takes a final copy where required, removes access in the right order, waits through a recovery period, and only then deletes data and, for retired arrays, erases the system.

## Prerequisites

1. An approved decommission request that names the volumes, shares, hosts or arrays, with the owner's sign-off.
2. Facts and usage data for the objects in scope, from [Gather storage facts and capacity reports](gather-storage-facts-and-capacity-reports.md).
3. A retention rule: a final backup or snapshot kept for an agreed period, and a data destruction standard for retired hardware.
4. Administrative credentials for the arrays and, if zoning is removed, the fabric switches.

## Steps

1. Identify the objects and their dependants: which hosts have the volume mapped, which replication or snapshot relationships exist, and which exports or shares are in use.
2. Check for activity using the performance or session information from the info modules, and stop the job if the volume shows recent I/O or active clients.
3. Take a final snapshot or backup and record its identifier in the change record.
4. Unmap or unmask the volume: ONTAP `na_ontap_lun_map` with absent state, PowerMax `dellemc.powermax.maskingview` and `storagegroup`, Storage Virtualize `ibm_svc_vol_map`, Infinidat `infini_map`. For NAS, remove exports and shares first.
5. Remove replication and snapshot relationships that depend on the volume.
6. Wait for the agreed recovery period, ideally a scheduled step in the workflow with a final approval node.
7. Delete the object: ONTAP `na_ontap_volume`, PowerStore `dellemc.powerstore.volume`, FlashArray `purefa_volume`, Hitachi `hv_ldev`. Note that some platforms keep deleted volumes for a time (a recycle bin on PowerStore, an eradication timer on FlashArray), which must be set to the policy.
8. Remove hosts and initiator entries that are no longer used, and the fabric zones with `cisco.nxos.nxos_zone_zoneset`.
9. For a retired array or SVM, use the vendor erase or delete function, for example the `netapp.ontap.na_ontap_vserver_delete` role or `everpure.flasharray.purefa_zte` (Zero Touch Erasure), and attach the evidence to the change record.
10. Update the CMDB, the capacity report and the cost allocation.

## Success Criteria

1. No host or client still references the removed storage, and no alarms were raised by the removal.
2. The final backup or snapshot exists for the retention period.
3. The delete step only happens after the recovery period and approval.
4. Retired hardware has a recorded erase or delete operation, and the CMDB no longer lists the objects.

## Notes

- Decommissioning is destructive; run the whole workflow in a check or report-only mode first and show the list to the owner.
- Deleting an SVM with `na_ontap_vserver_delete` removes its volumes, snapshots and clones, so use it only after all earlier steps are complete.
- Pair with [Provision block storage](provision-block-storage.md) and [Manage snapshots, clones and replication](manage-snapshots-clones-and-replication.md) for the matching create and protect steps.
- Hypervisor datastores and Kubernetes persistent volumes on the storage should be migrated first; see [Operate vSphere clusters and ESXi hosts](../virtualization/operate-vsphere-clusters-and-esxi-hosts.md).
