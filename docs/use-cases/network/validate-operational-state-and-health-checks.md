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

## Notes

- Combine with [Upgrade network OS and firmware](upgrade-network-os.md) and [Restore configuration](restore-configuration.md) as the verification step.
- Feed the results to [Generate network reports](generate-network-reports.md) for management summaries.
- Pair with Event-Driven Ansible: a monitoring alert for a BGP session can start the same health check job and attach the output to the ticket.
