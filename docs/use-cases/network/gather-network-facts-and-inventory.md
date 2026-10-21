---
title: Gather network facts and inventory
summary: Collect structured device facts, hardware and resource data across vendors and keep them as reusable data.
order: 40
personas: [Network engineer, Network architect, NetOps lead]
collections: [network.base, network.inventory_reports, ansible.utils, ansible.netcommon, cisco.ios, arista.eos, junipernetworks.junos]
key_content:
  - network.base.gather
  - network.inventory_reports.gather
  - ansible.utils.cli_parse
  - cisco.ios.ios_facts
  - arista.eos.eos_facts
  - junipernetworks.junos.junos_facts
  - ansible.netcommon.cli_command
---

# Gather network facts and inventory

## Description

Build an accurate, current picture of what is in the network: models, software versions, serial numbers, interfaces, VLANs and routing configuration. The data is collected in the same structure for every vendor, so it can feed reports, audits, upgrade planning and a source of truth.

## Notes

- Turn the data into HTML or CSV with [Generate network reports](generate-network-reports.md).
- Use the persisted data as the baseline for [Detect configuration drift](detect-configuration-drift.md).
- Controllers such as Cisco Catalyst Center also expose inventory information, for example through `cisco.catalystcenter.network_devices_info_workflow_manager`.
