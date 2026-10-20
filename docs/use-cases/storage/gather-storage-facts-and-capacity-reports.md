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

## Prerequisites

1. Read-only credentials for each array or for its management and analytics service (for example ONTAP Unified Manager or Pure1), stored in Automation Platform.
2. The collections for the platforms in scope in one execution environment.
3. A reporting format and destination: CSV or HTML, a wiki page, a CMDB or an observability tool.
4. Capacity thresholds and a list of owners per system or pool.

## Steps

1. Build the inventory of storage systems, grouped by vendor, with the management address for each.
2. Collect the facts per vendor:
   - ONTAP `na_ontap_info` or `na_ontap_rest_info`, and `netapp.um_info.na_um_volumes_info` and `na_um_aggregates_info` for fleet-level views;
   - PowerStore `dellemc.powerstore.info`, PowerMax `dellemc.powermax.info`, Unity `dellemc.unity.info`, PowerScale `dellemc.powerscale.info`, PowerFlex `dellemc.powerflex.info`;
   - FlashArray `purefa_info`, FlashBlade `purefb_info`, and the Pure1 fleet view with `everpure.pure1.pure1_info` and `pure1_volumes`;
   - Storage Virtualize `ibm_svc_info`, Hitachi `hv_storagesystem_facts`, `hv_storagepool_facts` and `hv_ldev_facts`;
   - Cohesity `cohesity.dataprotect.cohesity_facts` for the backup tier.
3. Normalise the output into one structure with Jinja2 filters, and compute used and free capacity, growth since the last run and thin-provisioning ratios.
4. Collect health and alert information, for example `purefa_messages`, `pure1_alerts` or the alert objects returned by the info modules.
5. Validate state against intent: compare expected volumes, hosts and mappings from the source of truth to the facts, and fail the job or raise a ticket for differences. On ONTAP, `na_ontap_wait_for_condition` can wait for a state before continuing.
6. Publish the report (CSV, HTML, wiki or email) and update the CMDB with the inventory.
7. Schedule the job daily and keep each run's data so that growth trends can be charted.

## Success Criteria

1. One report lists every storage system, pool and volume with capacity and owner.
2. Pools above the capacity threshold are flagged, with the owning team named.
3. Differences between provisioned and expected state appear in a validation report.
4. The job completes for all systems on schedule, with unreachable systems called out in the output.

## Notes

- Use read-only accounts for reporting jobs.
- Large arrays return a lot of data; request only the subsets needed (many info modules can limit what they gather).
- Pair with [Standardise storage system configuration](standardise-storage-system-configuration.md) and [Decommission storage safely](decommission-storage-safely.md), which uses the same facts to find unused volumes.
- Event-Driven Ansible can start expansion or clean-up jobs when capacity or health alerts arrive, using this report as the first diagnostic step.
