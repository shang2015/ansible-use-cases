---
title: Sync the CMDB from automation facts
summary: Keep ServiceNow configuration items accurate by writing discovered facts and relations back from playbooks.
order: 40
personas: [CMDB manager, Operations lead, Automation engineer]
collections: [servicenow.itsm, ansible.controller]
key_content:
  - servicenow.itsm.configuration_item
  - servicenow.itsm.configuration_item_batch
  - servicenow.itsm.configuration_item_info
  - servicenow.itsm.configuration_item_relations
  - servicenow.itsm.configuration_item_relations_info
  - ansible.controller.schedule
---

# Sync the CMDB from automation facts

## Description

Automation already gathers accurate facts from servers, devices and applications. Writing those facts to the ServiceNow CMDB keeps configuration items current without a separate discovery tool, and keeps relations such as "application runs on server" correct after builds and changes.

## Notes

- Pair with [Use ServiceNow CMDB as inventory](use-servicenow-cmdb-as-inventory.md) to close the loop in both directions.
- Agree on a single source of truth per attribute to avoid automation and discovery tools overwriting each other.
