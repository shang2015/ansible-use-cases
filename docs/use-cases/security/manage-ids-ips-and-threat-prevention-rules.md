---
title: Manage IDS/IPS and threat-prevention rules
summary: Keep intrusion prevention profiles and signatures consistent across Fortinet, Check Point, Trend Micro and Zscaler.
order: 70
personas: [Security engineer, Network security engineer]
collections: [fortinet.fortios, fortinet.fortimanager, check_point.mgmt, trendmicro.deepsec, zscaler.ziacloud]
key_content:
  - fortinet.fortios.fortios_ips_sensor
  - fortinet.fortimanager.fmgr_ips_sensor
  - check_point.mgmt.cp_mgmt_threat_profile
  - check_point.mgmt.cp_mgmt_run_ips_update
  - trendmicro.deepsec.deepsec_intrusion_prevention_rules
  - zscaler.ziacloud.zia_cloud_firewall_ips_rules
---

# Manage IDS/IPS and threat-prevention rules

## Description

Treat intrusion detection and prevention settings as managed configuration. Profiles, custom signatures, exceptions and update schedules live in version control, are applied the same way across devices and products, and can be changed quickly when a new threat appears.

## Prerequisites

1. Administrative API access to the products in scope: FortiGate or FortiManager, Check Point management, Trend Micro Deep Security, Zscaler Internet Access.
2. A current inventory of which profile applies to which zone, policy or workload group.
3. A test environment or a monitor-only mode to validate new signatures.
4. A change process for exceptions and for blocking rules.

## Steps

1. Export the current IPS profiles and exceptions as the starting point and store them in Git.
2. Define the desired profiles as variables, one per environment or risk class.
3. Apply them with the platform modules: `fortinet.fortios.fortios_ips_sensor` on a FortiGate, `fortinet.fortimanager.fmgr_ips_sensor` through FortiManager, `check_point.mgmt.cp_mgmt_threat_profile` on Check Point, `trendmicro.deepsec.deepsec_intrusion_prevention_rules` in Deep Security and `zscaler.ziacloud.zia_cloud_firewall_ips_rules` in Zscaler.
4. Trigger signature updates where the platform exposes them, for example `check_point.mgmt.cp_mgmt_run_ips_update`.
5. Roll out a new or changed profile in detect-only mode first, then switch it to prevent after review of the logs.
6. Install or publish the policy and verify that the active configuration matches Git.

## Success Criteria

1. IPS profile settings on every in-scope device match the versions in Git.
2. New signatures or exceptions reach all affected devices in one run.
3. A rollback to the previous profile can be done by re-running the job with the previous Git revision.
4. Each change is traceable to a ticket and a reviewer.

## Notes

- Zscaler also supports custom IPS signatures through `zscaler.ziacloud.zia_ips_signature_rules`.
- In `trendmicro.deepsec`, older modules such as `deepsec_intrusion_preventionrules` are marked deprecated; use the resource modules such as `deepsec_intrusion_prevention_rules`.
- Combine with [Manage firewall policy across vendors](manage-firewall-policy-across-vendors.md) for the policy that the profile is attached to.
- Pair with Event-Driven Ansible to push a block rule when a SIEM alert names an attacker address; see [Respond to security events with Event-Driven Ansible](respond-to-security-events-with-eda.md).
