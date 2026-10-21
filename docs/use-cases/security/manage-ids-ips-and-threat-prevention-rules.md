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

## Notes

- Zscaler also supports custom IPS signatures through `zscaler.ziacloud.zia_ips_signature_rules`.
- In `trendmicro.deepsec`, older modules such as `deepsec_intrusion_preventionrules` are marked deprecated; use the resource modules such as `deepsec_intrusion_prevention_rules`.
- Combine with [Manage firewall policy across vendors](manage-firewall-policy-across-vendors.md) for the policy that the profile is attached to.
- Pair with Event-Driven Ansible to push a block rule when a SIEM alert names an attacker address; see [Respond to security events with Event-Driven Ansible](respond-to-security-events-with-eda.md).
