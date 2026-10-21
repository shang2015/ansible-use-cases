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

## Notes

- Pair with [Build self-healing infrastructure from monitoring alerts](../event-driven/build-self-healing-infrastructure-from-monitoring-alerts.md) so alerts create the incident and the fix closes it. The `servicenow.itsm.records` event source can also start automation when an incident is assigned or updated.
- For approval-gated changes use [Automate change requests with approval gates](automate-change-requests-with-approval-gates.md).
- ManageEngine ServiceDesk Plus Cloud users can use the `manageengine.sdp_cloud` collection for the same pattern.
- Store the ServiceNow password as a credential, never in the playbook or inventory.
