---
title: Test links and circuits with approvals
summary: Run reachability and quality tests on a new or changed circuit, with approval steps and results recorded in the source of truth.
order: 100
personas: [Network engineer, NOC engineer, Service delivery manager]
collections: [ansible.netcommon, network.healthchecks, cisco.ios, cisco.nxos, juniper.device, netbox.netbox, servicenow.itsm]
key_content:
  - ansible.netcommon.net_ping
  - network.healthchecks.ip_reachability
  - cisco.ios.ios_ping
  - cisco.nxos.nxos_ping
  - juniper.device.ping
  - juniper.device.pmtud
  - netbox.netbox.netbox_circuit
  - servicenow.itsm.change_request
---

# Test links and circuits with approvals

## Description

Prove that a new or changed link works before traffic is moved to it. A workflow in Automation Platform runs the tests from both ends of the circuit, stops for approval at defined points and records the outcome in the ticket and inventory records.

## Notes

- Use the workflow approval node for the human decision, and keep test and change jobs separate so the tests can be rerun on demand.
- Related: [Validate operational state and health checks](validate-operational-state-and-health-checks.md).
- `networktocode.nautobot.circuit` is the equivalent for Nautobot.
