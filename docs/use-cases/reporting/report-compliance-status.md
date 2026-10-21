---
title: Report compliance status
summary: Scan servers, OpenShift clusters and network devices against security baselines and report pass, fail and drift per system.
order: 40
personas: [Compliance officer, Security engineer, Operations lead]
collections: [redhat.insights, infra.automation_development_office, network.inventory_reports, servicenow.itsm]
key_content:
  - redhat.insights.compliance
  - infra.automation_development_office.rhel_stig_cac
  - infra.automation_development_office.ocp_compliance_scan
  - infra.automation_development_office.acs_report
  - network.inventory_reports.detect
  - servicenow.itsm.incident
---

# Report compliance status

## Description

Give auditors and security teams a current, repeatable view of how systems compare with the policies the organization has chosen (for example CIS or DISA STIG profiles, or an approved device configuration). Ansible runs the scans on a schedule, collects the results from each tool, and produces one report with the failures and the owners to act on them.

## Notes

- Scanning and remediation are separate steps: report first, then remediate in a controlled change. See the security and Linux use cases for the remediation side.
- Some roles in `infra.automation_development_office` are tailored to its bootstrap framework; check their variables before reuse.
- Insights compliance needs the host registered and a policy set in the Insights service first; the role runs the scan on the host.
- Use Event-Driven Ansible to start a rescan after a remediation or change, and to open an incident only when a control stays failed.
- Combine with [Report on job activity and host coverage](report-on-job-activity-and-host-coverage.md) so systems that were never scanned are visible too.
