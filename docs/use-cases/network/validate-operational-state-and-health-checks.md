---
title: Validate operational state and health checks
summary: Check BGP, OSPF, interfaces, reachability and device resources, and turn the results into pass or fail evidence.
order: 70
personas: [Network engineer, NOC engineer, NetOps lead]
collections: [network.healthchecks, network.bgp, network.ospf, network.interfaces, ansible.utils, ansible.netcommon]
key_content:
  - network.healthchecks.bgp
  - network.healthchecks.ospf
  - network.healthchecks.interfaces
  - network.healthchecks.ip_reachability
  - network.healthchecks.cpu
  - network.healthchecks.memory
  - network.bgp.health_checks
  - ansible.utils.cli_parse
examples:
  - title: network.healthchecks validated collection
    url: https://github.com/ansible-automation-platform/network.healthchecks
    note: platform-independent health check roles
---

# Validate operational state and health checks

## Description

Confirm that the network is working, not only that it is configured: BGP sessions are established, OSPF neighbors are up, interfaces are in the expected state and devices have headroom. The same checks run before and after a change, and on a schedule, with a clear pass or fail result.

## Prerequisites

1. Read access to the devices and a supported platform in the inventory.
2. The expected state, for example the list of BGP neighbors or the interfaces that must be up.
3. Thresholds for resource checks such as CPU or memory.

## Steps

1. Choose the checks. The `network.healthchecks` collection has roles for `bgp`, `ospf`, `interfaces`, `ip_reachability`, `cpu`, `memory`, `filesystem`, `uptime`, `environment` and `crashfiles`. Protocol collections add `network.bgp.health_checks` and `network.ospf.health_checks`.
2. Create a playbook that calls the roles with the targets and thresholds, and a job template with read-only credentials.
3. For anything not covered, run the command and parse it into structured data with `ansible.utils.cli_parse`, then assert on the values.
4. Evaluate the results into pass or fail per device and per check, and fail the job when required checks fail.
5. Run the job template before and after change jobs, in a workflow, and on a schedule for continuous assurance.

## Success Criteria

1. Each device returns a result for every selected check.
2. A neighbor that is down or an interface that is in the wrong state makes the job fail and names the device.
3. The before and after results of a change can be compared side by side.
4. Results are kept in job history or exported for reports.

## Notes

- Combine with [Upgrade network OS and firmware](upgrade-network-os.md) and [Restore configuration](restore-configuration.md) as the verification step.
- Feed the results to [Generate network reports](generate-network-reports.md) for management summaries.
- Pair with Event-Driven Ansible: a monitoring alert for a BGP session can start the same health check job and attach the output to the ticket.
