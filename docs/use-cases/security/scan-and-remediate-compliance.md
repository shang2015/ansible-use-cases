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

## Prerequisites

1. A scanning source: Red Hat Satellite with SCAP content, Red Hat Insights compliance, or the OpenShift Compliance Operator.
2. Agreed compliance profiles and any tailoring (rule exclusions and value changes) approved by the compliance owner.
3. Credentials in Automation Platform for Satellite or Insights and for the managed hosts and clusters.
4. A remediation playbook or role for the profile, as described in [Harden RHEL to CIS and DISA STIG baselines](harden-rhel-to-cis-and-stig.md).

## Steps

1. Load the SCAP content into Satellite with `redhat.satellite.scap_content`, and define any customization with `redhat.satellite.scap_tailoring_file`.
2. Register hosts with Red Hat Insights and enable the compliance service by applying the `redhat.insights.compliance` role to the target hosts.
3. For OpenShift, install the operator and run scans with the `infra.automation_development_office.ocp_compliance_install`, `ocp_compliance_profiles` and `ocp_compliance_scan` roles.
4. Run a scheduled job template that triggers the scans and collects the failed rules per host or cluster.
5. Remediate in a controlled step: apply `infra.automation_development_office.rhel_stig_cac` or the baseline playbook to hosts with failures, and use `infra.automation_development_office.ocp_compliance_remediation` on clusters.
6. Open a ticket for failures that cannot be fixed automatically, for example with `servicenow.itsm.incident`, and record the exception decision.
7. Re-scan and store the before and after reports as job artifacts or in the reporting system.

## Success Criteria

1. Every in-scope host and cluster has a scan result that is no older than the agreed interval.
2. The compliance score per profile is visible by host group, with failed rules listed.
3. Automated remediation closes the failed rules it covers, confirmed by the next scan.
4. Failures that stay open have a ticket, an owner and an approved exception or due date.

## Notes

- Scan first and remediate in a separate job template, so a change window and an approval can sit between them.
- Pair with [Harden RHEL to CIS and DISA STIG baselines](harden-rhel-to-cis-and-stig.md) for the baseline itself and [Remediate vulnerabilities from scanner findings](remediate-vulnerabilities-from-scanner-findings.md) for patch-level findings.
- Pair with Event-Driven Ansible when a scanner can send a webhook on a new failed rule; see [Respond to security events with Event-Driven Ansible](respond-to-security-events-with-eda.md).
