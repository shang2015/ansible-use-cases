---
title: Remediate with Red Hat Insights
summary: Connect RHEL hosts to Red Hat Insights, use it for inventory and compliance scans, and run its remediations and events through Ansible.
order: 80
personas: [Linux administrator, Security engineer, Operations lead]
collections: [redhat.insights, redhat.insights_eda, redhat.rhel_system_roles, redhat.satellite_operations]
key_content:
  - redhat.rhel_system_roles.rhc
  - redhat.insights.insights
  - redhat.insights.compliance
  - redhat.insights_eda.insights
  - redhat.satellite_operations.cloud_connector
---

# Remediate with Red Hat Insights

## Description

Red Hat Insights finds configuration, vulnerability, patch and compliance issues on registered RHEL hosts and generates Ansible playbooks to fix them. This use case connects the hosts, builds inventories from Insights data and runs the fixes from Automation Platform with approval and reporting.

## Prerequisites

1. A Red Hat account with Insights access, and a service account or activation key for registration and API access.
2. RHEL hosts that can reach Red Hat (directly, through a proxy, or through Satellite).
3. Automation controller with an Insights credential, if remediation playbooks are to be run from Insights.
4. Roles in the Insights account that allow viewing inventory and, for patch data, patching.

## Steps

1. Connect hosts to Red Hat and Insights with `redhat.rhel_system_roles.rhc`, using an activation key and the `rhc_insights` settings (display name, tags and remediation support). This replaces the deprecated `redhat.insights.insights_register` and `redhat.insights.insights_config` modules.
2. For hosts registered through Satellite, configure Red Hat Cloud Connector for Satellite with `redhat.satellite_operations.cloud_connector` so remediations can be run on Satellite-managed hosts.
3. Create an automation controller inventory with the `redhat.insights.insights` inventory plugin, so hosts can be grouped by Insights tags and system data.
4. Run compliance scans with the `redhat.insights.compliance` role against the policies defined in Insights.
5. Build remediation plans in Insights for the findings that are approved for action. Add the generated playbooks to automation controller through an Insights credential and project, and create job templates from them.
6. Limit the run to the affected hosts and run it in check mode first. Run the job from a workflow that includes an approval step for production.
7. Receive Insights notifications in Event-Driven Ansible with the `redhat.insights_eda.insights` event source, and start a job template or open an ITSM ticket for selected events.
8. Re-scan after the remediation job and record the before and after counts.

## Success Criteria

1. All in-scope hosts appear in Insights with the intended tags and in the automation controller inventory.
2. A remediation plan runs to completion on its targets and the finding disappears at the next Insights check-in.
3. Compliance scan results are visible in Insights for each assigned policy.
4. Selected Insights events produce an automated action or ticket without manual triage.

## Notes

- Use [Patch RHEL at scale](patch-rhel-at-scale.md) for planned, controlled patch cycles and this use case for targeted fixes of specific findings.
- The `redhat.insights.insights_client` role is deprecated in favour of `redhat.rhel_system_roles.rhc`.
- The `redhat.insights_eda` collection provides notification-driven events: advisor recommendations, new vulnerabilities and compliance below a threshold are examples in its documentation.
- Insights remediation on a host needs the remediation packages installed; the `rhc` role installs them when remediation is enabled, which is the default, and the setting applies from RHEL 8.4.
