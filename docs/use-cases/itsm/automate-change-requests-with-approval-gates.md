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

## Prerequisites

1. A ServiceNow instance and a service account with rights on `change_request` and `change_task`.
2. A change model or template that matches the automated change, such as a standard change template for patching.
3. Job templates for the change itself, a pre-check and a post-check.
4. Named approvers in Automation Platform when an extra approval node is wanted.

## Steps

1. Build a workflow job template with `ansible.controller.workflow_job_template` and add the nodes in order: pre-check, create change, wait for approval, implement, verify, close change.
2. Create the change request with `servicenow.itsm.change_request`, setting the template or type, planned start and end, assignment group and the affected configuration item.
3. Poll `servicenow.itsm.change_request_info` until the change reaches an approved or scheduled state. Fail the job on rejection or timeout.
4. Add an approval node, handled with `ansible.controller.workflow_approval`, when a second approval inside Automation Platform is required, for example for production.
5. Run the implementation job template. Record each major step as a change task with `servicenow.itsm.change_request_task`.
6. Close the change request with a close code and notes on success. On failure run a rollback node and set the change to the failed state.
7. Schedule the workflow inside the planned change window, or launch it from ServiceNow flows using the Automation Platform integration.

## Success Criteria

1. No implementation job runs before the change is approved.
2. Each change record has planned and actual times, tasks and the job link.
3. Failed changes are rolled back automatically and show the failure reason in ServiceNow.
4. Auditors can trace a configuration change to an approved change number.

## Notes

- Combine with [Orchestrate approvals, surveys and notifications in workflows](orchestrate-approvals-surveys-and-notifications.md) for the workflow mechanics.
- Emergency changes can skip the wait node but should still create and close a change record.
- Patching, configuration and cloud use cases elsewhere on this site can be dropped in as the implementation node.
