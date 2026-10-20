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

## Prerequisites

1. A ServiceNow service account with read access to the CMDB tables to be used, for example server and network device classes.
2. CMDB records with a usable host name or IP address and with the attributes needed for grouping.
3. A ServiceNow credential in Automation Platform and an execution environment that includes `servicenow.itsm`.

## Steps

1. Choose the CMDB table, query filter and fields that define a host, and test them with `servicenow.itsm.configuration_item_info`.
2. Write an inventory file for the `servicenow.itsm.now` plugin with the table, the query, the host name field and the groupings, using `keyed_groups` or `compose`.
3. Add the file to a project and create an inventory source with `ansible.controller.inventory_source`, attaching the ServiceNow credential.
4. Sync the source on a schedule, or on demand with `ansible.controller.inventory_source_update`.
5. Add host variables from CMDB fields that jobs need, such as environment, owner or support group.
6. Point job templates and limits at the groups, and use the CMDB state to leave out retired systems.

## Success Criteria

1. The inventory shows the active CMDB items in scope, grouped as agreed.
2. A CMDB change appears in the inventory after the next sync.
3. Job templates run against CMDB-defined groups with no hand-maintained host list.

## Notes

- Data quality is the main risk: hosts without a resolvable name fail at connection time. Add a validation job that lists unreachable CMDB items.
- Pair with [Sync the CMDB from automation facts](sync-cmdb-from-automation-facts.md) so facts flow back to the CMDB.
- Other inventory sources such as Satellite, VMware and cloud providers are covered in the platform use cases.
