---
title: Scan and remediate compliance
summary: Run SCAP-based compliance scans on RHEL and OpenShift, report the failures and remediate them through Automation Platform.
order: 20
personas: [Compliance officer, Security engineer, Platform operations]
collections: [redhat.satellite, redhat.insights, infra.automation_development_office, redhat.rhel_system_roles, servicenow.itsm]
key_content:
  - redhat.satellite.scap_content
  - redhat.satellite.scap_tailoring_file
  - redhat.insights.compliance
  - infra.automation_development_office.rhel_stig_cac
  - infra.automation_development_office.ocp_compliance_scan
  - infra.automation_development_office.ocp_compliance_remediation
  - servicenow.itsm.incident
---

# Scan and remediate compliance

## Description

Detect configuration that does not meet the chosen security policy, report it in a form auditors accept, and fix it with the same automation that applies the baseline. The loop covers RHEL hosts and OpenShift clusters and runs continuously, not only before audits.

## Notes

- Scan first and remediate in a separate job template, so a change window and an approval can sit between them.
- Pair with [Harden RHEL to CIS and DISA STIG baselines](harden-rhel-to-cis-and-stig.md) for the baseline itself and [Remediate vulnerabilities from scanner findings](remediate-vulnerabilities-from-scanner-findings.md) for patch-level findings.
- Pair with Event-Driven Ansible when a scanner can send a webhook on a new failed rule; see [Respond to security events with Event-Driven Ansible](respond-to-security-events-with-eda.md).
