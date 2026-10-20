---
title: Provision block storage
summary: Create volumes, register host initiators, map or mask them to hosts and zone the SAN, consistently across storage vendors.
order: 10
personas: [Storage administrator, Infrastructure engineer, Virtualization administrator]
collections: [netapp.ontap, dellemc.powerstore, dellemc.powermax, dellemc.unity, everpure.flasharray, ibm.storage_virtualize, hitachivantara.vspone_block, infinidat.infinibox, cisco.nxos]
key_content:
  - netapp.ontap.na_ontap_lun
  - netapp.ontap.na_ontap_lun_map
  - dellemc.powermax.maskingview
  - dellemc.powerstore.volume
  - everpure.flasharray.purefa_volume
  - ibm.storage_virtualize.ibm_svc_manage_volume
  - hitachivantara.vspone_block.hv_ldev
  - cisco.nxos.nxos_zone_zoneset
examples:
  - title: netapp.ontap collection
    url: https://github.com/ansible-collections/netapp.ontap
  - title: dellemc.powermax collection
    url: https://github.com/dell/ansible-powermax
---

# Provision block storage

## Description

Turn a request for a disk (size, performance tier, host or cluster) into a finished block volume that the host can see. One workflow creates the volume, registers the host's initiators, maps or masks the volume, and where required zones the Fibre Channel fabric. The steps are the same across vendors; only the modules differ.

## Prerequisites

1. Management access to the storage array or controller, with a service account limited to provisioning tasks, stored in Automation Platform.
2. An execution environment with the collection for each array in scope and, for zoning, `cisco.nxos`.
3. Host identifiers: FC WWPNs or iSCSI/NVMe qualified names, collected from the host or from the hypervisor management system.
4. A standard for pools or aggregates, volume naming, performance tiers and thin provisioning.
5. For SAN zoning, access to the fabric switches and an agreed zoning convention.

## Steps

1. Collect the request: host name, volume name, size, tier, protocol and whether the volume is shared by a cluster.
2. Create the volume or LUN on the array:
   - NetApp ONTAP: `netapp.ontap.na_ontap_lun` (or the `netapp.ontap.na_ontap_san_create` role);
   - Dell PowerStore: `dellemc.powerstore.volume`, PowerMax: `dellemc.powermax.volume`, Unity: `dellemc.unity.volume`;
   - Everpure FlashArray: `everpure.flasharray.purefa_volume`;
   - IBM Storage Virtualize: `ibm.storage_virtualize.ibm_svc_manage_volume`;
   - Hitachi VSP: `hitachivantara.vspone_block.hv_ldev`;
   - Infinidat: `infinidat.infinibox.infini_vol`.
3. Register the host and its initiators:
   - ONTAP `na_ontap_igroup` and `na_ontap_igroup_initiator`;
   - PowerStore `dellemc.powerstore.host` and `hostgroup`;
   - PowerMax `dellemc.powermax.initiator` and `host`;
   - FlashArray `purefa_host` and `purefa_hg`;
   - Storage Virtualize `ibm_svc_host` and `ibm_svc_hostcluster`;
   - Hitachi `hv_hg` or `hv_iscsi_target`;
   - Infinidat `infini_host`, `infini_port` and `infini_cluster`.
4. Map or mask the volume to the host or cluster: `netapp.ontap.na_ontap_lun_map`, `dellemc.powermax.storagegroup` with `dellemc.powermax.maskingview` (plus `portgroup`), `ibm.storage_virtualize.ibm_svc_vol_map`, `infinidat.infinibox.infini_map`, or the host connection options of the PowerStore and FlashArray volume modules.
5. Zone the fabric when needed with `cisco.nxos.nxos_zone_zoneset` on MDS switches, using one zone per initiator and target group. Do this before mapping if the array requires the initiators to be logged in first.
6. Rescan the host and prepare the filesystem, for example with the Linux or Windows storage roles in a follow-up job, or let the hypervisor create the datastore.
7. Verify with the array's info module (see [Gather storage facts and capacity reports](gather-storage-facts-and-capacity-reports.md)) and record the volume in the CMDB.

## Success Criteria

1. The requested volume exists with the right size, pool and naming standard.
2. Only the intended hosts or clusters can see the volume.
3. The host sees all expected paths after the rescan.
4. Re-running the job with the same request reports no changes.

## Notes

- Keep the vendor differences in variable files and role defaults, and offer the requester one catalog item. A single job template can include the correct vendor tasks based on an array group variable.
- Pair with [Manage snapshots, clones and replication](manage-snapshots-clones-and-replication.md) and with [Decommission storage safely](decommission-storage-safely.md).
- Other certified block collections in this domain include `dellemc.powerflex` (software-defined block storage) and `dellemc.vplex`.
- On HPE ProLiant servers, local RAID volumes are handled by the server tools in [Provision bare-metal servers](../infrastructure/provision-bare-metal-servers.md).
- Event-Driven Ansible can trigger expansion of a volume when a capacity alert is received.
