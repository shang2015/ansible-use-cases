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

## Notes

- Use [Patch RHEL at scale](patch-rhel-at-scale.md) for planned, controlled patch cycles and this use case for targeted fixes of specific findings.
- The `redhat.insights.insights_client` role is deprecated in favour of `redhat.rhel_system_roles.rhc`.
- The `redhat.insights_eda` collection provides notification-driven events: advisor recommendations, new vulnerabilities and compliance below a threshold are examples in its documentation.
- Insights remediation on a host needs the remediation packages installed; the `rhc` role installs them when remediation is enabled, which is the default, and the setting applies from RHEL 8.4.
