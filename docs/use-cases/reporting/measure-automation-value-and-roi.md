---
title: Measure automation value and ROI
summary: Convert job history into hours saved, cost avoided and lead-time improvement for each automated process.
order: 20
personas: [Automation lead, IT finance partner, Executive sponsor]
collections: [ansible.controller, servicenow.itsm]
key_content:
  - ansible.controller.job_list
  - ansible.controller.controller_api
  - ansible.controller.label
  - servicenow.itsm.change_request_info
  - servicenow.itsm.incident_info
---

# Measure automation value and ROI

## Description

Show the business what automation returns. For each automated process the team records how long and how costly the manual version was, and Ansible multiplies that by the number of successful runs. The result is a regular statement of hours saved, cost avoided and, where change or incident data is available, faster lead times.

## Prerequisites

1. A list of automated processes, mapped to the job templates and workflows that implement them, with a named owner for each.
2. An agreed baseline for each process: manual effort in minutes, number of people involved, the hourly cost rate and the error or rework rate. Take the figures from time studies or from the process owners and write down their source.
3. Agreement with finance on how savings are calculated and presented, including any items that are not counted.
4. Access to job history in the platform, kept long enough to cover the reporting period.
5. Optional: access to the ITSM system for change request and incident data.

## Steps

1. Tag job templates with `ansible.controller.label` for the process or category (for example patching, onboarding, compliance), so jobs can be grouped.
2. Keep a baseline table in Git: template or workflow, manual minutes per run or per host, people, hourly rate and source of the estimate.
3. Collect successful jobs for the period with `ansible.controller.job_list` or the `ansible.controller.controller_api` lookup, including host counts for per-host processes.
4. Calculate for each process: runs, hosts, hours saved (runs or hosts times baseline minutes), cost avoided and automation run time, and sum by category and business unit.
5. Where ITSM data is available, read change requests with `servicenow.itsm.change_request_info` and incidents with `servicenow.itsm.incident_info` to compare lead time, failed changes and mean time to resolve before and after automation.
6. Add the costs: platform subscription, infrastructure and the effort spent developing and maintaining content, to show net benefit.
7. Publish the figures on a schedule, with the method and assumptions included in the report, and review them with finance each quarter.

## Success Criteria

1. Every reported process has an owner, a baseline and a source for the baseline.
2. The hours saved figure can be traced to job runs and baseline values.
3. Costs of running the platform are included, so the figure is net.
4. The report is issued each quarter and accepted by finance as a consistent method.
5. At least one process is reprioritised, retired or expanded based on the numbers.

## Notes

- Use conservative baselines and count only successful runs. A defensible small number is more useful than a large one that is challenged.
- Not all value is time: consistency, audit evidence and speed are better measured with change and incident data.
- Start from the activity report in [Report on job activity and host coverage](report-on-job-activity-and-host-coverage.md) and consider hosts automated per process, not only job counts.
- Unused templates in the report are a prompt for clean-up; see [Assess the current automation estate](../platform/assess-automation-estate.md).
