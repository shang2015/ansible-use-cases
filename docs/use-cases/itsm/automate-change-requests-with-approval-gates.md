---
title: Automate change requests with approval gates
summary: Raise ServiceNow change requests from automation, wait for approval, run the change and record the outcome.
order: 20
personas: [Change manager, Operations lead, Automation engineer]
collections: [servicenow.itsm, ansible.controller]
key_content:
  - servicenow.itsm.change_request
  - servicenow.itsm.change_request_info
  - servicenow.itsm.change_request_task
  - ansible.controller.workflow_job_template
  - ansible.controller.workflow_approval
---

# Automate change requests with approval gates

## Description

Standard and normal changes follow a fixed process: request, approval, implementation, review. Automation Platform runs the implementation, and ServiceNow stays the system of record. The change record is created from the playbook, the job waits until the change is approved, and the result is written back to the change.

## Notes

- Combine with [Orchestrate approvals, surveys and notifications in workflows](orchestrate-approvals-surveys-and-notifications.md) for the workflow mechanics.
- Emergency changes can skip the wait node but should still create and close a change record.
- Patching, configuration and cloud use cases elsewhere on this site can be dropped in as the implementation node.
