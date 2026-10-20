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

## Prerequisites

1. A running RHACS Central instance and an API token with administrative rights, stored as an Automation Platform credential.
2. The policy set to be applied, exported from an existing instance or written from scratch.
3. Notification targets (email, Slack, ticketing) and an identity provider for logins.
4. A Git repository for the configuration, with a review process.

## Steps

1. Export the current policies as the baseline, using the policy export module `infra.rhacs_configuration.rhacs_policy_export`, and commit them.
2. Define policies in variables and apply them with `infra.rhacs_configuration.rhacs_policy`.
3. Create notification channels with `infra.rhacs_configuration.rhacs_notifier_integration` and attach them to policies with `infra.rhacs_configuration.rhacs_policy_notifier`.
4. Connect the identity provider with `infra.rhacs_configuration.rhacs_auth_provider`, and map groups to roles.
5. Schedule vulnerability reports and compliance scans with `infra.rhacs_configuration.rhacs_report_schedule` and `infra.rhacs_configuration.rhacs_compliance_schedule`.
6. Run the job template on every merge to the main branch and on a schedule to correct drift.

## Success Criteria

1. The policies in RHACS match the repository after each run.
2. Violations of high-severity policies are sent to the defined notification channel.
3. Users log in through the identity provider and hold only the roles mapped from their groups.
4. Scheduled vulnerability and compliance reports run and are delivered to their recipients.

## Notes

- The validated roles `infra.automation_development_office.acs_upload_policies` and `infra.automation_development_office.acs_report` apply policies and generate vulnerability workload reports on top of the collection.
- Policies set to enforce can block deployments. Introduce them in inform mode first.
- Related: [Secure the software supply chain](secure-the-software-supply-chain.md).
