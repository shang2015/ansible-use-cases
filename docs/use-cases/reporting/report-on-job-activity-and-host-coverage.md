---
title: Report on job activity and host coverage
summary: Produce scheduled reports on job volume, success rate, duration and which managed hosts were or were not automated.
order: 10
personas: [Automation lead, Operations manager, Platform owner]
collections: [ansible.controller, ansible.platform, infra.aap_configuration]
key_content:
  - ansible.controller.job_list
  - ansible.platform.job_list
  - ansible.controller.controller_api
  - infra.aap_configuration.get_stats
  - ansible.controller.schedule
  - ansible.controller.notification_template
---

# Report on job activity and host coverage

## Description

Answer the questions management asks about automation: how many jobs ran, how many succeeded, who used the platform, how long jobs took, and how much of the estate is actually touched by automation. Ansible reads the platform's own data, builds the report on a schedule and sends it to the people who need it.

## Prerequisites

1. Read access to the platform API through an auditor-type account or token, stored as a credential.
2. The audience and the questions: for example a weekly summary for the automation lead and a monthly coverage view for the CIO.
3. Inventories that represent the managed estate. Coverage is only as complete as the inventory, so a reference list (CMDB or hypervisor) is needed to find hosts that are missing.
4. Agreement on the reporting period, retention of job history and what counts as covered (for example a successful job in the last 30 days).
5. A destination for the report: email, a Git repository, a file share or a wiki.

## Steps

1. Define the metrics: jobs per day and per template, success and failure rates, average and peak duration, queue wait, active users and teams, and hosts changed.
2. Collect job records with `ansible.controller.job_list` (or `ansible.platform.job_list` through the gateway) for the reporting period, or query specific endpoints with the `ansible.controller.controller_api` lookup.
3. Add platform totals such as templates, users and license use with `infra.aap_configuration.get_stats`.
4. Compute host coverage: list hosts per inventory with the `ansible.controller.controller_api` lookup, check the last job that touched each host, and compare against the reference list to find hosts that are unmanaged or stale.
5. Render the results into CSV and an HTML summary with a template, and keep each period's files in Git or object storage for trend comparison.
6. Create a job template for the report and schedule it with `ansible.controller.schedule`, for example weekly.
7. Deliver the result with a notification template (`ansible.controller.notification_template`) or by a mail or upload task, and agree the follow-up actions for failing templates and uncovered hosts.

## Success Criteria

1. The report is produced on schedule without manual work.
2. Job counts and success rates match the figures shown in the platform for the same period.
3. A list of hosts without recent automation is produced and reviewed by the owners.
4. The metrics definition is documented, so numbers do not change between periods.
5. Report history is available for trend charts.

## Notes

- The platform's built-in dashboards cover day-to-day views. Build a custom report when the audience needs different grouping, such as by business unit, or data merged with other sources.
- Keep job history retention (cleanup jobs) aligned with the reporting period, otherwise old figures disappear.
- Use [Measure automation value and ROI](measure-automation-value-and-roi.md) to turn these counts into time and cost savings.
- Pair with [Monitor Automation Platform health and capacity](../platform/monitor-aap-health-and-capacity.md) for operational rather than business reporting.
