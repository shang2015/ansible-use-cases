---
title: Enforce configuration compliance
summary: Check device settings such as NTP, SNMP, AAA and logging against a standard, report violations and optionally fix them.
order: 50
personas: [Network engineer, Security engineer, Compliance officer]
collections: [ansible.utils, ansible.netcommon, network.base, network.acls, cisco.ios, arista.eos, junipernetworks.junos]
key_content:
  - ansible.utils.validate
  - ansible.utils.cli_parse
  - network.base.remediate
  - network.acls.detect
  - cisco.ios.ios_ntp_global
  - cisco.ios.ios_snmp_server
  - arista.eos.eos_ntp_global
  - junipernetworks.junos.junos_ntp_global
---

# Enforce configuration compliance

## Description

Define the settings every device must have, for example approved NTP servers, SNMP communities or users, syslog targets and access lists, then verify them across all vendors. Violations are listed per device and can be corrected with the same automation.

## Notes

- Start in report-only mode and enable remediation per rule after owners agree.
- Related: [Detect configuration drift](detect-configuration-drift.md) compares with a recorded state, while this use case compares with a policy.
- Report results with [Generate network reports](generate-network-reports.md).
