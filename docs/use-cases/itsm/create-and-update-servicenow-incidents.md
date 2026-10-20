---
title: Create and update ServiceNow incidents from automation
summary: Open, enrich, resolve and close ServiceNow incidents from playbooks so every automated action leaves a ticket trail.
order: 10
personas: [ITSM process owner, Operations lead, Automation engineer]
collections: [servicenow.itsm, ansible.controller, manageengine.sdp_cloud]
key_content:
  - servicenow.itsm.incident
  - servicenow.itsm.incident_info
  - servicenow.itsm.problem
  - servicenow.itsm.attachment_upload
  - servicenow.itsm.api
  - ansible.controller.notification_template
---

# Create and update ServiceNow incidents from automation

## Description

Operations teams want every automated fix to be visible in the ticketing system. Playbooks open an incident when a job fails or a problem is detected, add work notes and attachments while the work runs, and resolve the incident when the fix is verified.

## Prerequisites

1. A ServiceNow instance and a service account with rights on the `incident` table (and `problem` if used).
2. A ServiceNow credential in Automation Platform, or the instance URL, user and password provided as environment variables to the job.
3. An execution environment that includes the `servicenow.itsm` collection.
4. An agreed incident template: caller, category, assignment group, impact and urgency, and the close codes to use.

## Steps

1. Create a job template for each automated task and attach the ServiceNow credential.
2. Open an incident at the start of the task, or on failure, with `servicenow.itsm.incident` and `state: new`. Keep the returned incident number as a fact.
3. Add work notes and move the state to `in_progress` as the playbook progresses. Upload logs or reports with `servicenow.itsm.attachment_upload`.
4. Find existing open incidents for the same configuration item with `servicenow.itsm.incident_info` to avoid duplicates.
5. Resolve the incident with a close code and notes when verification passes, or leave it open and assign it to a group when it fails.
6. Link recurring incidents to a problem record with `servicenow.itsm.problem`. Use `servicenow.itsm.api` for tables or fields that have no dedicated module.
7. Add a notification template on the job template so failures also reach a chat channel or e-mail list.

## Success Criteria

1. Each automated run that changes a system has a matching incident with work notes and a final state.
2. No duplicate incidents are created for the same configuration item while one is open.
3. Failed runs leave an open, assigned incident with the job output attached.
4. Incident numbers appear in the job output so auditors can move between the ticket and the job.

## Notes

- Pair with [Build self-healing infrastructure from monitoring alerts](../event-driven/build-self-healing-infrastructure-from-monitoring-alerts.md) so alerts create the incident and the fix closes it. The `servicenow.itsm.records` event source can also start automation when an incident is assigned or updated.
- For approval-gated changes use [Automate change requests with approval gates](automate-change-requests-with-approval-gates.md).
- ManageEngine ServiceDesk Plus Cloud users can use the `manageengine.sdp_cloud` collection for the same pattern.
- Store the ServiceNow password as a credential, never in the playbook or inventory.
