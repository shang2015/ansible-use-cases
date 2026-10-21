---
title: Shut down and start up a multi-tier application
summary: Stop and start web, application and database tiers in the right order with a workflow, approvals and health checks.
order: 140
personas: [Operations lead, Application owner, Automation engineer]
collections: [ansible.controller, redhat.runtimes_common]
key_content:
  - ansible.controller.workflow_job_template
  - ansible.controller.workflow_job_template_node
  - ansible.controller.workflow_launch
  - ansible.controller.workflow_approval
  - ansible.controller.schedule
  - redhat.runtimes_common.tail_grep
---

# Shut down and start up a multi-tier application

## Description

Maintenance windows, data centre moves and disaster recovery tests need an application to be stopped and started in the right order: web tier first, then application servers, then databases, and the reverse at start-up. A workflow encodes that order and checks health between the steps.

## Notes

- Patching and upgrade steps belong in the maintenance node: see [Patch application nodes one at a time behind a load balancer](patch-application-nodes-behind-a-load-balancer.md).
- Workflow mechanics are explained in [Orchestrate approvals, surveys and notifications in workflows](../itsm/orchestrate-approvals-surveys-and-notifications.md).
- For SAP stacks combine this with [Run SAP Day 2 operations](run-sap-day-2-operations.md).
