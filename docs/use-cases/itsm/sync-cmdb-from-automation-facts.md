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

## Prerequisites

1. A ServiceNow service account with write access to the CMDB classes that will be maintained.
2. Agreed CI classes, identification keys (for example serial number or FQDN) and the attributes to populate.
3. Inventories covering the systems in scope, and fact gathering that works against them.
4. A CMDB owner who approves which attributes automation is allowed to overwrite.

## Steps

1. Gather facts with the normal fact-gathering tasks, or with the platform-specific `*_facts` modules.
2. Map facts to the CMDB attributes, for example name, OS, CPU, memory and IP address.
3. Look up existing items with `servicenow.itsm.configuration_item_info` to decide between create and update.
4. Create or update items with `servicenow.itsm.configuration_item`. Use `servicenow.itsm.configuration_item_batch` for large inventories to cut the number of API calls.
5. Maintain relations with `servicenow.itsm.configuration_item_relations`, and verify them with `servicenow.itsm.configuration_item_relations_info`.
6. Mark items as retired when a decommission job completes.
7. Schedule the job template with `ansible.controller.schedule` and run it again at the end of every build or change job.

## Success Criteria

1. Every in-scope system exists in the CMDB exactly once, with attributes that match the host.
2. Relations between applications, servers and services are present and correct.
3. Decommissioned systems no longer appear as active.
4. A reconciliation report shows no unexplained difference between inventory and CMDB.

## Notes

- Pair with [Use ServiceNow CMDB as inventory](use-servicenow-cmdb-as-inventory.md) to close the loop in both directions.
- Agree on a single source of truth per attribute to avoid automation and discovery tools overwriting each other.
