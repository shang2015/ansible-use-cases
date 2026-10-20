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

## Prerequisites

1. A list of the application's tiers, hosts and dependencies, agreed with the application owner.
2. Job templates that stop, start and check each tier, tested separately.
3. Inventory groups per tier and per application.
4. Approvers and a notification target for planned shutdowns.

## Steps

1. Document the stop order and start order, and the health check for each tier.
2. Write one job template per tier and action, for example stop web, stop app, stop database, and a health check template. Use `redhat.runtimes_common.tail_grep` to wait for a "started" message in server logs.
3. Create a shutdown workflow with `ansible.controller.workflow_job_template` and chain the nodes with `ansible.controller.workflow_job_template_node`, one tier after the other.
4. Create a start-up workflow in the reverse order, with a health check node after each tier and a failure path that stops the run and alerts the team.
5. Insert an approval step in front of the shutdown, handled by `ansible.controller.workflow_approval`, and notifications at the start and the end.
6. Add a parent workflow that runs shutdown, the maintenance task and start-up, started with `ansible.controller.workflow_launch`, for a complete change window.
7. Schedule recurring windows with `ansible.controller.schedule`, or run on demand from a ServiceNow change.
8. Rehearse in a test environment, and record the durations.

## Success Criteria

1. Tiers stop and start in the documented order every time.
2. Start-up ends with the application passing end-to-end health checks.
3. A failure at any tier stops the workflow and notifies the owner.
4. The elapsed time of a maintenance window is measured and falls with each rehearsal.

## Notes

- Patching and upgrade steps belong in the maintenance node: see [Patch application nodes one at a time behind a load balancer](patch-application-nodes-behind-a-load-balancer.md).
- Workflow mechanics are explained in [Orchestrate approvals, surveys and notifications in workflows](../itsm/orchestrate-approvals-surveys-and-notifications.md).
- For SAP stacks combine this with [Run SAP Day 2 operations](run-sap-day-2-operations.md).
