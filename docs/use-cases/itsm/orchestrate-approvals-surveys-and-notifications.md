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

## Prerequisites

1. Individual job templates for each task, tested on their own.
2. Teams and users in Automation Platform with roles for who can launch, approve and view the workflow.
3. A messaging target for notifications: e-mail, Slack, Mattermost or a webhook for tools such as Microsoft Teams.
4. Optional ServiceNow access, if the workflow should create or update tickets.

## Steps

1. Define the process: inputs, approval points, order of tasks, failure handling and who is told what.
2. Add a survey to the workflow, or its first job template, to collect inputs with defaults and validation.
3. Create the workflow with `ansible.controller.workflow_job_template` and add the nodes with `ansible.controller.workflow_job_template_node`. Set the success, failure and always links.
4. Insert approval nodes where a person must decide. Set a timeout so that a request that is left waiting does not block forever. Approvals can also be handled from automation with `ansible.controller.workflow_approval`.
5. Create notification templates with `ansible.controller.notification_template` and attach them to the workflow for started, approved, success and failure events.
6. Add a failure path that opens a ServiceNow incident with `servicenow.itsm.incident` and runs cleanup.
7. Use set-fact artifacts to pass values, such as host names, from one node to the next.
8. Test every path, including rejection and timeout, and then publish the workflow to the requesting team.

## Success Criteria

1. The workflow asks for inputs once, and passes them to every node.
2. Tasks do not start before the approver accepts, and rejections end the workflow cleanly.
3. Requesters and approvers receive a message at each agreed point.
4. A failed run creates a ticket and does not leave half-built resources.

## Notes

- Used as the foundation for [Automate change requests with approval gates](automate-change-requests-with-approval-gates.md) and [Fulfil service catalog requests with Automation Platform](fulfil-service-catalog-requests.md).
- For application stacks see [Shut down and start up a multi-tier application](../applications/shut-down-and-start-up-multi-tier-applications.md).
- Event-Driven Ansible can start the same workflow from an alert, see [Build self-healing infrastructure from monitoring alerts](../event-driven/build-self-healing-infrastructure-from-monitoring-alerts.md).
