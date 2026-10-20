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

## Prerequisites

1. A BigPanda account with an API token that can update incidents and alerts.
2. A way to deliver incident events to Event-Driven Ansible, such as a BigPanda webhook integration to the `ansible.eda.webhook` source or an event stream.
3. Job templates for approved fixes and a mapping from incident tags to hosts.

## Steps

1. Configure BigPanda to send new and updated incidents to the Event-Driven Ansible endpoint.
2. Write a rulebook that matches incident status, severity and tags and runs the matching job template.
3. At the start of the job, add a comment with `bigpanda.incident.comment` and a tag with `bigpanda.incident.add_tag`, such as `auto-remediation`.
4. Assign the incident to the owning team or user with `bigpanda.incident.assign` if the fix is not automated.
5. After verification, close the underlying alerts with `bigpanda.incident.resolve_alert` or the whole incident with `bigpanda.incident.resolve`.
6. Use `bigpanda.incident.merge` and `bigpanda.incident.split` to correct grouping when automation finds related or unrelated incidents.

## Success Criteria

1. Each automated action leaves a comment and a tag on the incident.
2. Incidents that are fixed are resolved without operator clicks.
3. Incidents that are not fixed are assigned and keep the job output as a comment.

## Notes

- Use [Create and update ServiceNow incidents from automation](../itsm/create-and-update-servicenow-incidents.md) when tickets live in ServiceNow and BigPanda is only the correlation layer.
- See [Build self-healing infrastructure from monitoring alerts](build-self-healing-infrastructure-from-monitoring-alerts.md).
