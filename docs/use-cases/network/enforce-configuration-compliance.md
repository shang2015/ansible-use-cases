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

## Prerequisites

1. A written standard that can be expressed as data, such as the list of approved NTP servers.
2. Read access to the devices for the audit, and write access if remediation is in scope.
3. A place to store the standard (Git or a source of truth) and to publish results.

## Steps

1. Express the standard as variables or as a JSON schema or criteria file.
2. Collect the current values with the resource facts of the platform modules (for example `cisco.ios.ios_ntp_global` or `cisco.ios.ios_snmp_server` with `state: gathered`) or with `ansible.utils.cli_parse`.
3. Compare actual and expected data with `ansible.utils.validate`, and for ACLs run `network.acls.detect`.
4. Build a compliance result per device and per rule, then write it to the job output, a report or a ticket.
5. For approved remediation, apply the desired values with the resource modules (`arista.eos.eos_ntp_global`, `junipernetworks.junos.junos_ntp_global`, ...) or with `network.base.remediate`.
6. Schedule the audit job and run it again after remediation.

## Success Criteria

1. Each rule in the standard produces a pass or fail result for every device.
2. Non-compliant devices are listed with the actual and the expected value.
3. After remediation, a second run shows the fixed devices as compliant.
4. Results are kept for audit evidence.

## Notes

- Start in report-only mode and enable remediation per rule after owners agree.
- Related: [Detect configuration drift](detect-configuration-drift.md) compares with a recorded state, while this use case compares with a policy.
- Report results with [Generate network reports](generate-network-reports.md).
