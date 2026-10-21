---
title: Configure RHACS as code
summary: Manage Red Hat Advanced Cluster Security policies, integrations, access and reports from Git.
order: 150
personas: [Platform engineer, Security engineer, Kubernetes administrator]
collections: [infra.rhacs_configuration, infra.automation_development_office]
key_content:
  - infra.rhacs_configuration.rhacs_policy
  - infra.rhacs_configuration.rhacs_policy_notifier
  - infra.rhacs_configuration.rhacs_notifier_integration
  - infra.rhacs_configuration.rhacs_auth_provider
  - infra.rhacs_configuration.rhacs_report_schedule
  - infra.rhacs_configuration.rhacs_compliance_schedule
---

# Configure RHACS as code

## Description

Keep the Kubernetes security policy for all clusters in one reviewed place. Policies, notifiers, authentication, report schedules and compliance schedules of Red Hat Advanced Cluster Security for Kubernetes are defined as variables and applied by Automation Platform, so every central and secured cluster behaves the same.

## Notes

- The validated roles `infra.automation_development_office.acs_upload_policies` and `infra.automation_development_office.acs_report` apply policies and generate vulnerability workload reports on top of the collection.
- Policies set to enforce can block deployments. Introduce them in inform mode first.
- Related: [Secure the software supply chain](secure-the-software-supply-chain.md).
