---
title: Contain threats from EDR detections
summary: Isolate compromised hosts and endpoints automatically after an EDR detection, and restore them after review.
order: 60
personas: [SOC analyst, Incident responder, Security engineer]
collections: [crowdstrike.falcon, cisco.ise, ansible.eda, servicenow.itsm]
key_content:
  - crowdstrike.falcon.host_info
  - crowdstrike.falcon.host_contain
  - crowdstrike.falcon.host_group
  - cisco.ise.anc_policy
  - cisco.ise.anc_endpoint_apply
  - cisco.ise.anc_endpoint_clear
  - servicenow.itsm.incident
---

# Contain threats from EDR detections

## Description

Limit the spread of an attack in minutes. When the EDR reports a high-severity detection, the automation confirms the host, isolates it at the endpoint and at the network access layer, opens an incident, and releases the host only after an analyst approves.

## Notes

- Use an approval step for critical servers where automatic isolation could cause an outage.
- Falcon sensors themselves can be rolled out and configured with `crowdstrike.falcon.falcon_install` and `crowdstrike.falcon.falcon_configure`.
- Combine with [Enrich SIEM investigations and automate response](enrich-siem-investigations.md) and [Respond to security events with Event-Driven Ansible](respond-to-security-events-with-eda.md).
