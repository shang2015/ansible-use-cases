---
title: Update BigPanda incidents from automation
summary: Let remediation jobs comment on, assign, tag and resolve BigPanda incidents and alerts.
order: 90
personas: [Operations lead, NOC engineer, Automation engineer]
collections: [bigpanda.incident, ansible.eda, ansible.controller]
key_content:
  - bigpanda.incident.comment
  - bigpanda.incident.assign
  - bigpanda.incident.add_tag
  - bigpanda.incident.resolve
  - bigpanda.incident.resolve_alert
  - bigpanda.incident.merge
  - ansible.eda.webhook
---

# Update BigPanda incidents from automation

## Description

BigPanda groups alerts from many tools into incidents. Automation can act on those incidents and keep BigPanda current: a job comments on the incident, tags it, assigns it, and resolves it when the fix is confirmed, so the operations center sees what automation did.

## Notes

- Use [Create and update ServiceNow incidents from automation](../itsm/create-and-update-servicenow-incidents.md) when tickets live in ServiceNow and BigPanda is only the correlation layer.
- See [Build self-healing infrastructure from monitoring alerts](build-self-healing-infrastructure-from-monitoring-alerts.md).
