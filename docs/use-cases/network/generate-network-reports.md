---
title: Generate network reports
summary: Produce HTML or CSV inventory, configuration and health reports from collected network data.
order: 80
personas: [Network engineer, Network architect, IT manager]
collections: [network.inventory_reports, network.healthchecks, ansible.utils]
key_content:
  - network.inventory_reports.gather
  - network.inventory_reports.generate_report
  - network.inventory_reports.flatten_dict
  - network.healthchecks.health_check_view
  - ansible.utils.cli_parse
examples:
  - title: network.inventory_reports validated collection
    url: https://github.com/ansible-automation-platform/network.inventory_reports
    note: gather facts and generate HTML reports
---

# Generate network reports

## Description

Give managers, auditors and other teams a readable view of the network without sending them to the CLI. Automation collects device data and turns it into a report that can be opened in a browser or loaded into a spreadsheet.

## Prerequisites

1. Read access to the devices and an inventory with `ansible_network_os`.
2. A decision on the content and audience: hardware and software inventory, configuration summary, health results or compliance results.
3. A location to publish the output, such as a web server, file share or artifact store.

## Steps

1. Collect the data with the `network.inventory_reports.gather` role, or reuse facts from [Gather network facts and inventory](gather-network-facts-and-inventory.md).
2. Render the HTML report with the `network.inventory_reports.generate_report` role.
3. For CSV exports, flatten nested data with the `network.inventory_reports.flatten_dict` filter and write it with a template or the `copy` module.
4. For health summaries, include the output of the `network.healthchecks` roles, shaped with the `network.healthchecks.health_check_view` filter.
5. Publish the files to the destination and schedule the job template, for example weekly.
6. Send a notification with the link to the report.

## Success Criteria

1. The report contains every device that is in the inventory, with the agreed columns.
2. The report is generated on a schedule without manual steps and is dated.
3. Readers can open it without Ansible or network access.

## Notes

- Combine with [Enforce configuration compliance](enforce-configuration-compliance.md) to report pass or fail by rule.
- Controllers have their own reporting: `cisco.catalystcenter.reports_workflow_manager` for Catalyst Center and `juniper.apstra.blueprint_report` for Apstra blueprints.
- Automation Platform job and host metrics for the automation itself are covered in the reporting domain.
