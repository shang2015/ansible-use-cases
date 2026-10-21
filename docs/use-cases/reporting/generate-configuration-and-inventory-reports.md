---
title: Generate configuration and inventory reports
summary: Collect facts from network devices and servers and publish structured inventory and configuration reports, also into the CMDB.
order: 30
personas: [Infrastructure manager, Network engineer, CMDB owner, Auditor]
collections: [network.inventory_reports, network.base, servicenow.itsm, cisco.ios, arista.eos, cisco.iosxr, cisco.nxos]
key_content:
  - network.inventory_reports.gather
  - network.inventory_reports.persist
  - network.inventory_reports.generate_report
  - network.inventory_reports.flatten_dict
  - servicenow.itsm.configuration_item_batch
  - servicenow.itsm.configuration_item_info
---

# Generate configuration and inventory reports

## Description

Replace spreadsheets and one-off scripts with a repeatable report of what is deployed: devices, versions, interfaces, addresses, installed software and configuration items. Ansible gathers the facts, stores them as structured data, renders HTML and CSV for readers, and keeps the configuration management database in step with what is really there.

## Notes

- The network roles currently cover a defined set of platforms, so check the supported platform list before promising coverage of a vendor.
- Related: [Back up device configuration](../network/backup-device-configuration.md) stores configuration text, whereas this use case stores structured facts.
- Pair with [Report compliance status](report-compliance-status.md): the same stored facts are the baseline for drift detection.
- Event-Driven Ansible can refresh the inventory and CMDB after a change event, so reports do not wait for the next schedule.
