---
title: Orchestrate approvals, surveys and notifications in workflows
summary: Chain job templates into one workflow with input surveys, human approval steps and notifications.
order: 60
personas: [Automation engineer, Operations lead, Service owner]
collections: [ansible.controller, servicenow.itsm]
key_content:
  - ansible.controller.workflow_job_template
  - ansible.controller.workflow_job_template_node
  - ansible.controller.workflow_approval
  - ansible.controller.notification_template
  - ansible.controller.job_template
  - servicenow.itsm.incident
---

# Orchestrate approvals, surveys and notifications in workflows

## Description

Multi-step processes, such as building a server or opening access, need inputs from a person, an approval from a manager and a message when they finish. Automation Platform workflows join several job templates with logic for success, failure and always paths, with the human steps built in.

## Notes

- Used as the foundation for [Automate change requests with approval gates](automate-change-requests-with-approval-gates.md) and [Fulfil service catalog requests with Automation Platform](fulfil-service-catalog-requests.md).
- For application stacks see [Shut down and start up a multi-tier application](../applications/shut-down-and-start-up-multi-tier-applications.md).
- Event-Driven Ansible can start the same workflow from an alert, see [Build self-healing infrastructure from monitoring alerts](../event-driven/build-self-healing-infrastructure-from-monitoring-alerts.md).
