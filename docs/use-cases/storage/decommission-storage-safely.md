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

## Notes

- Decommissioning is destructive; run the whole workflow in a check or report-only mode first and show the list to the owner.
- Deleting an SVM with `na_ontap_vserver_delete` removes its volumes, snapshots and clones, so use it only after the hosts are unmapped and the data is backed up or no longer needed.
- Pair with [Provision block storage](provision-block-storage.md) and [Manage snapshots, clones and replication](manage-snapshots-clones-and-replication.md) for the matching create and protect steps.
- Hypervisor datastores and Kubernetes persistent volumes on the storage should be migrated first; see [Operate vSphere clusters and ESXi hosts](../virtualization/operate-vsphere-clusters-and-esxi-hosts.md).
