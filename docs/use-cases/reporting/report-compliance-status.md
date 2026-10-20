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

## Prerequisites

1. The policies in force and the systems each applies to, agreed with security and the audit team.
2. For RHEL servers: hosts registered to Red Hat Insights with a compliance policy defined in it, or the OpenSCAP profile content installed from repositories the hosts can reach.
3. For OpenShift: Compliance Operator and, for workload vulnerabilities, Red Hat Advanced Cluster Security (RHACS) with an API token.
4. For network devices: the approved configuration stored as structured data, for example with the facts workflow in [Generate configuration and inventory reports](generate-configuration-and-inventory-reports.md).
5. A destination for reports and a ticketing route for findings.

## Steps

1. Map each policy to the scan method and the inventory group it covers.
2. Run the Insights compliance scan on RHEL hosts with the `redhat.insights.compliance` role, or run the OpenSCAP-based `infra.automation_development_office.rhel_stig_cac` role with remediation disabled to report only.
3. Create Compliance Operator scans on OpenShift with `infra.automation_development_office.ocp_compliance_scan`, and generate RHACS vulnerability reports with `infra.automation_development_office.acs_report`.
4. Check network devices with `network.inventory_reports.detect`, which compares running configuration with the desired state and lists differences.
5. Collect the outputs (scan results, CSV and summary files) into one data set per run, and calculate pass rate per policy, system group and owner.
6. Publish the report and trend to the audit team. Open incidents for new failures with `servicenow.itsm.incident`, assigned to the system owner.
7. Agree the remediation route: fix by an automation job, request an exception with expiry, or accept the risk, and record the decision.

## Success Criteria

1. Every in-scope system has a scan result no older than the agreed interval.
2. The report shows pass and fail by policy rule, system group and owner.
3. New failures create tickets with the evidence attached.
4. Trend data shows whether compliance is improving month by month.
5. Exceptions are recorded with an owner and an expiry date.

## Notes

- Scanning and remediation are separate steps: report first, then remediate in a controlled change. See the security and Linux use cases for the remediation side.
- Some roles in `infra.automation_development_office` are tailored to its bootstrap framework; check their variables before reuse.
- Insights compliance needs the host registered and a policy set in the Insights service first; the role runs the scan on the host.
- Use Event-Driven Ansible to start a rescan after a remediation or change, and to open an incident only when a control stays failed.
- Combine with [Report on job activity and host coverage](report-on-job-activity-and-host-coverage.md) so systems that were never scanned are visible too.
