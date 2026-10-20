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

## Prerequisites

1. Details of the circuit: both endpoints, interfaces, addresses and provider reference, in a source of truth or as job inputs.
2. Access to the devices at each end to run tests.
3. A list of acceptance tests and their expected results (reachability, MTU, latency).
4. Named approvers, and optionally a change management system.

## Steps

1. Read the circuit and endpoint data, for example from NetBox with `netbox.netbox.netbox_circuit` or the `netbox.netbox.nb_lookup` lookup, or take it from a survey.
2. Open or update a change request, for example with `servicenow.itsm.change_request`, and add an approval node to the workflow before the link is enabled.
3. Run reachability tests from each end with `ansible.netcommon.net_ping` or the platform module (`cisco.ios.ios_ping`, `cisco.nxos.nxos_ping`, `juniper.device.ping`). On Junos, test path MTU with `juniper.device.pmtud`. The `network.healthchecks.ip_reachability` role runs the same ping checks across platforms.
4. Compare results with the acceptance values and fail the workflow when a test fails.
5. Pause for approval, then enable the link or move traffic to it using the change job.
6. Run the tests again and write the result back to the change request and to the circuit record.

## Success Criteria

1. Tests are run from both ends with the same inputs, and each result is recorded.
2. No traffic is moved without an approval in the workflow history.
3. A failed test stops the workflow and leaves the previous path in place.
4. The circuit record and the change request show the final status.

## Notes

- Use the workflow approval node for the human decision, and keep test and change jobs separate so the tests can be rerun on demand.
- Related: [Validate operational state and health checks](validate-operational-state-and-health-checks.md).
- `networktocode.nautobot.circuit` is the equivalent for Nautobot.
