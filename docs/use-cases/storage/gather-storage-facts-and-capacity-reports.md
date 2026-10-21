---
title: Gather storage facts and capacity reports
summary: Collect inventory, capacity, health and alert data from every array and publish consolidated reports and state checks.
order: 60
personas: [Storage administrator, Capacity planner, Operations lead]
collections: [netapp.ontap, netapp.um_info, dellemc.powerstore, dellemc.powermax, dellemc.unity, dellemc.powerscale, dellemc.powerflex, everpure.flasharray, everpure.flashblade, everpure.pure1, ibm.storage_virtualize, hitachivantara.vspone_block, cohesity.dataprotect]
key_content:
  - netapp.ontap.na_ontap_info
  - netapp.ontap.na_ontap_rest_info
  - netapp.um_info.na_um_volumes_info
  - dellemc.powerstore.info
  - dellemc.powermax.info
  - everpure.flasharray.purefa_info
  - everpure.pure1.pure1_info
  - ibm.storage_virtualize.ibm_svc_info
  - hitachivantara.vspone_block.hv_storagesystem_facts
---

# Gather storage facts and capacity reports

## Description

Answer "what do we have, how full is it and is it healthy?" without logging in to each array. Facts are collected from all storage platforms, normalised into a common record (system, pool, volume, host, usage), and published as reports, a dashboard feed or a CMDB update. The same facts can validate that the state matches what was provisioned.

## Notes

- Use read-only accounts for reporting jobs.
- Large arrays return a lot of data; request only the subsets needed (many info modules can limit what they gather).
- Pair with [Standardise storage system configuration](standardise-storage-system-configuration.md) and [Decommission storage safely](decommission-storage-safely.md), which uses the same facts to find unused volumes.
- Event-Driven Ansible can start expansion or clean-up jobs when capacity or health alerts arrive, using this report as the first diagnostic step.
