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

## Prerequisites

1. Credentials for the devices and servers in scope, stored as platform credentials, and an inventory that groups them by platform.
2. A decision on the data to report: network resources (interfaces, VLANs, routing), hardware and software versions, installed packages and services, or a mix.
3. For network devices, the platform collections for the vendors in scope (for example `cisco.ios`, `arista.eos`, `cisco.iosxr`, `cisco.nxos`) and `network.base`.
4. A Git repository or object store for the fact files and the rendered reports.
5. For CMDB updates, an integration user in ServiceNow and the agreed class and field mapping.

## Steps

1. Group the inventory by platform, site and role, and define the report scope per audience.
2. Collect network facts with the `network.inventory_reports.gather` role, which uses native parsers per platform.
3. Store the facts as structured YAML in Git with `network.inventory_reports.persist`, so history shows what changed between runs.
4. Render the HTML report with `network.inventory_reports.generate_report`, and produce CSV for spreadsheet users by preparing the data with the `network.inventory_reports.flatten_dict` filter.
5. For servers, collect facts and package or service information with the setup and fact modules, and write them in the same file layout.
6. Read the current CMDB records with `servicenow.itsm.configuration_item_info`, compare them with the collected data and update the differences with `servicenow.itsm.configuration_item_batch`.
7. Run the job template on a schedule, publish the report where the audience reads it, and send a notification with the link.

## Success Criteria

1. A report exists for every in-scope device or server, produced by the latest scheduled run.
2. Fact files in Git show what changed between two runs.
3. CSV and HTML reports open without manual editing and cover the agreed columns.
4. CMDB records match the collected data for the in-scope classes, and differences are listed.
5. Devices that could not be reached are listed in the report and in a notification.

## Notes

- The network roles currently cover a defined set of platforms, so check the supported platform list before promising coverage of a vendor.
- Related: [Back up device configuration](../network/backup-device-configuration.md) stores configuration text, whereas this use case stores structured facts.
- Pair with [Report compliance status](report-compliance-status.md): the same stored facts are the baseline for drift detection.
- Event-Driven Ansible can refresh the inventory and CMDB after a change event, so reports do not wait for the next schedule.
