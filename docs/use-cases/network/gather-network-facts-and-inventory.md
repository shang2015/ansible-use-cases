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

## Prerequisites

1. Read-only credentials for the devices, stored in Automation Platform.
2. An inventory with `ansible_network_os` and the right connection type per group.
3. A place to keep the output, for example a Git repository, data store or reporting system.

## Steps

1. Start with a platform fact module such as `cisco.ios.ios_facts`, `arista.eos.eos_facts` or `junipernetworks.junos.junos_facts` to collect device facts and, with `gather_network_resources`, resource facts.
2. For a platform-independent collection, run `network.base.gather` for configuration resources, or `network.inventory_reports.gather` for device and hardware details.
3. For data that no module returns, run the command with `ansible.netcommon.cli_command` and parse the text into structured data with `ansible.utils.cli_parse`.
4. Store the structured output with `network.base.persist`, or write it to a file or API.
5. Schedule the job and keep each run's output for comparison.

## Success Criteria

1. Every device in the inventory returns facts, and failures are listed.
2. Facts use one structure across vendors for the common fields (model, version, serial number, interfaces).
3. The collected data is stored where reports and other jobs can read it.

## Notes

- Turn the data into HTML or CSV with [Generate network reports](generate-network-reports.md).
- Use the persisted data as the baseline for [Detect configuration drift](detect-configuration-drift.md).
- Controllers such as Cisco Catalyst Center also expose inventory information, for example through `cisco.catalystcenter.network_devices_info_workflow_manager`.
