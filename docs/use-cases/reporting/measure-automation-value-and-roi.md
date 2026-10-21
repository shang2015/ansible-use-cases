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

## Notes

- Use conservative baselines and count only successful runs. A defensible small number is more useful than a large one that is challenged.
- Not all value is time: consistency, audit evidence and speed are better measured with change and incident data.
- Start from the activity report in [Report on job activity and host coverage](report-on-job-activity-and-host-coverage.md) and consider hosts automated per process, not only job counts.
- Unused templates in the report are a prompt for clean-up; see [Assess the current automation estate](../platform/assess-automation-estate.md).
