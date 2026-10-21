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

## Notes

- Combine with [Enforce configuration compliance](enforce-configuration-compliance.md) to report pass or fail by rule.
- Controllers have their own reporting: `cisco.catalystcenter.reports_workflow_manager` for Catalyst Center and `juniper.apstra.blueprint_report` for Apstra blueprints.
- Automation Platform job and host metrics for the automation itself are covered in the reporting domain.
