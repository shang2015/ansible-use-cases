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

## Notes

- The platform's built-in dashboards cover day-to-day views. Build a custom report when the audience needs different grouping, such as by business unit, or data merged with other sources.
- Keep job history retention (cleanup jobs) aligned with the reporting period, otherwise old figures disappear.
- Use [Measure automation value and ROI](measure-automation-value-and-roi.md) to turn these counts into time and cost savings.
- Pair with [Monitor Automation Platform health and capacity](../platform/monitor-aap-health-and-capacity.md) for operational rather than business reporting.
