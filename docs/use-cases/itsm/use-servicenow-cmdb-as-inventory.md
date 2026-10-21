---
title: Use ServiceNow CMDB as inventory
summary: Build dynamic Automation Platform inventories from CMDB tables so automation targets the systems of record.
order: 50
personas: [Automation engineer, CMDB manager, Platform administrator]
collections: [servicenow.itsm, ansible.controller]
key_content:
  - servicenow.itsm.now
  - servicenow.itsm.configuration_item_info
  - ansible.controller.inventory_source
  - ansible.controller.inventory_source_update
---

# Use ServiceNow CMDB as inventory

## Description

Instead of keeping a second list of hosts, the inventory is built from the ServiceNow CMDB. Servers, network devices and applications that are registered and active in the CMDB become inventory hosts, grouped by class, environment or support group.

## Notes

- Data quality is the main risk: hosts without a resolvable name fail at connection time. Add a validation job that lists unreachable CMDB items.
- Pair with [Sync the CMDB from automation facts](sync-cmdb-from-automation-facts.md) so facts flow back to the CMDB.
- Other inventory sources such as Satellite, VMware and cloud providers are covered in the platform use cases.
