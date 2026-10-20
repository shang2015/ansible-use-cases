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

## Prerequisites

1. CrowdStrike Falcon with an API client that has host-management scope, stored as a credential in Automation Platform.
2. Optional: Cisco ISE with ANC (adaptive network control) policies defined for quarantine.
3. A severity and asset policy that states which detections trigger containment and which hosts are excluded (domain controllers, production databases).
4. A notification and ticketing path for the incident response team.

## Steps

1. Receive the detection as an event in Event-Driven Ansible, or poll for detections from a job template.
2. Look up the host with `crowdstrike.falcon.host_info` and check it against the exclusion list.
3. Contain the host with `crowdstrike.falcon.host_contain`, and add it to a quarantine host group with `crowdstrike.falcon.host_group` if group-based policy is used.
4. Quarantine the endpoint at the network edge: apply a pre-defined ANC policy with `cisco.ise.anc_endpoint_apply`; policies are managed with `cisco.ise.anc_policy`.
5. Open an incident with `servicenow.itsm.incident`, including the detection, host and actions taken.
6. After analyst approval, lift containment: containment in the same `crowdstrike.falcon.host_contain` module and clear the quarantine with `cisco.ise.anc_endpoint_clear`.

## Success Criteria

1. A qualifying detection leads to host containment within the agreed time, recorded in the job log.
2. Excluded hosts are never contained automatically and raise a manual alert instead.
3. Each containment has an incident record with the actions and the approver of the release.
4. Containment can be reversed from a job template without console access.

## Notes

- Use an approval step for critical servers where automatic isolation could cause an outage.
- Falcon sensors themselves can be rolled out and configured with `crowdstrike.falcon.falcon_install` and `crowdstrike.falcon.falcon_configure`.
- Combine with [Enrich SIEM investigations and automate response](enrich-siem-investigations.md) and [Respond to security events with Event-Driven Ansible](respond-to-security-events-with-eda.md).
