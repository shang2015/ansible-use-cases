---
title: Detect configuration drift
summary: Compare running configuration with the approved state and report every unplanned change per device and per resource.
order: 20
personas: [Network engineer, Security engineer, NetOps lead]
collections: [network.base, network.interfaces, network.bgp, network.ospf, network.acls, ansible.utils]
key_content:
  - network.base.persist
  - network.base.detect
  - network.interfaces.detect
  - network.bgp.detect
  - network.ospf.detect
  - network.acls.detect
  - ansible.utils.fact_diff
examples:
  - title: network.base validated collection
    url: https://github.com/redhat-cop/network.base
    note: platform-agnostic gather, persist, detect and remediate roles
---

# Detect configuration drift

## Description

Find out, on a schedule or after an incident, which devices no longer match their approved configuration. The result is a per-device list of what changed (interfaces, BGP, OSPF, ACLs and other resources), so engineers can decide whether to accept the change or correct it.

## Prerequisites

1. Network credentials with read access, stored as Automation Platform credentials.
2. A recorded "known good" state for each device: either facts saved as `host_vars` in a Git repository or data store, or a source of truth.
3. An inventory with `ansible_network_os` set per device, in an execution environment that contains the network collections.

## Steps

1. Capture the baseline once with the `network.base.gather` and `network.base.persist` roles, which save resource facts as YAML host variables in a local or remote data store.
2. Review and approve the baseline in Git so it becomes the intended state.
3. Create a project and a job template that runs the `network.base.detect` role for generic resources, or the scoped `network.interfaces.detect`, `network.bgp.detect`, `network.ospf.detect` and `network.acls.detect` roles.
4. For custom comparisons, use `ansible.utils.fact_diff` to diff two fact sets and return only the changed keys.
5. Schedule the job template (for example hourly or nightly) and send the drift output to a notification channel or ticket.
6. Optional: run [Back up device configuration](backup-device-configuration.md) first so the full text configuration is saved next to the structured diff.

## Success Criteria

1. Every in-scope device is checked in each run, and unreachable devices are reported separately.
2. Drift is reported per device and per resource, showing the intended and the actual values.
3. A deliberate test change on a lab device appears in the next run.
4. A run with no drift finishes without findings, so a clean report can be used as evidence.

## Notes

- Report only by default. Correct drift with [Restore configuration](restore-configuration.md) or the `remediate` roles, ideally after an approval step.
- Detection against a source of truth is described in [Manage scoped configuration with a source of truth](manage-scoped-configuration-with-source-of-truth.md).
- Pair with Event-Driven Ansible to start a detect run when a device sends a configuration-change syslog message, instead of waiting for the schedule.
- Fabric controllers have their own drift views, for example `cisco.nd.nd_compliance_analysis` for Nexus Dashboard Insights.
