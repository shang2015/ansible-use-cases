---
title: Remediate IBM Instana events
summary: Receive Instana events in Event-Driven Ansible and run remediation jobs for application and infrastructure issues.
order: 50
personas: [SRE, Application owner, Observability engineer]
collections: [ibm.instana, ansible.eda, ansible.controller]
key_content:
  - ibm.instana.instana_webhook
  - ansible.eda.rulebook_activation
  - ansible.eda.normalize_keys
  - ansible.controller.job_template
---

# Remediate IBM Instana events

## Description

IBM Instana detects application and infrastructure issues in real time. The Instana webhook source passes those events to Event-Driven Ansible, where rules decide which job template to start, such as restarting a service, scaling a tier or clearing a queue.

## Prerequisites

1. An Instana tenant and permission to define an alert channel of the webhook type.
2. Event-Driven Ansible controller reachable from Instana, with a decision environment that includes `ibm.instana`.
3. Job templates for each approved fix, and a mapping from the Instana entity to an inventory host.

## Steps

1. Add the `ibm.instana.instana_webhook` source to a rulebook, with a port and, where supported, a token.
2. Create an Instana alert channel that posts to that address, and attach it to the alert configurations in scope.
3. Use the `ansible.eda.normalize_keys` filter if event keys contain characters that rules cannot match on.
4. Write rules on issue type, severity and entity, and start the job template with `run_job_template`, passing event details as variables.
5. Start the activation and trigger a test issue, then check the payload in the activation log.
6. Make the job verify recovery and add a note or ticket with the result.

## Success Criteria

1. An approved Instana issue starts one job for the affected host.
2. Instana shows the issue as closed after the fix.
3. Unknown events are logged and ignored.

## Notes

- Publish the Event-Driven Ansible endpoint through a load balancer or an event stream if Instana cannot reach the controller directly.
- Follow [Build self-healing infrastructure from monitoring alerts](build-self-healing-infrastructure-from-monitoring-alerts.md) for design guidance.
