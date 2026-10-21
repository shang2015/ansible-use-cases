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

## Notes

- Keep the vendor differences in variable files and role defaults, and offer the requester one catalog item. A single job template can include the correct vendor tasks based on an array group variable.
- Pair with [Manage snapshots, clones and replication](manage-snapshots-clones-and-replication.md) and with [Decommission storage safely](decommission-storage-safely.md).
- Other certified block collections in this domain include `dellemc.powerflex` (software-defined block storage) and `dellemc.vplex`.
- On HPE ProLiant servers, local RAID volumes are handled by the server tools in [Provision bare-metal servers](../infrastructure/provision-bare-metal-servers.md).
- Event-Driven Ansible can trigger expansion of a volume when a capacity alert is received.
