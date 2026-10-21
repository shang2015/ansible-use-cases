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

## Notes

- Report only by default. Correct drift with [Restore configuration](restore-configuration.md) or the `remediate` roles, ideally after an approval step.
- Detection against a source of truth is described in [Manage scoped configuration with a source of truth](manage-scoped-configuration-with-source-of-truth.md).
- Pair with Event-Driven Ansible to start a detect run when a device sends a configuration-change syslog message, instead of waiting for the schedule.
- Fabric controllers have their own drift views, for example `cisco.nd.nd_compliance_analysis` for Nexus Dashboard Insights.
