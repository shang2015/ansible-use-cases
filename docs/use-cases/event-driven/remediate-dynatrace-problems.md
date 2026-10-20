---
title: Remediate Dynatrace problems
summary: Start Ansible jobs from Dynatrace problems, by polling the problems API or receiving Dynatrace workflow events.
order: 20
personas: [SRE, Operations lead, Observability engineer]
collections: [dynatrace.event_driven_ansible, dynatrace.oneagent, ansible.eda, ansible.controller]
key_content:
  - dynatrace.event_driven_ansible.dt_esa_api
  - dynatrace.event_driven_ansible.dt_webhook
  - dynatrace.oneagent.oneagent
  - ansible.eda.rulebook_activation
  - ansible.controller.job_template
---

# Remediate Dynatrace problems

## Description

Dynatrace detects problems and identifies the affected entities. With the Dynatrace event sources for Event-Driven Ansible, those problems start the right remediation job in Automation Platform, so known issues are fixed automatically and the result is reported back to the operations team.

## Prerequisites

1. A Dynatrace tenant and an API token that can read problems, or a Dynatrace workflow that can call the Red Hat Ansible connector.
2. Event-Driven Ansible controller with a decision environment that includes the `dynatrace.event_driven_ansible` collection.
3. Job templates for each remediation, and a mapping from Dynatrace entities to inventory hosts.
4. Network access from the Event-Driven Ansible controller to the tenant, or from Dynatrace to the controller for webhooks.

## Steps

1. Choose the delivery path. Use the `dt_esa_api` source to poll the tenant for problems, or the `dt_webhook` source to receive events pushed from a Dynatrace workflow.
2. Store the tenant URL and token in an Event-Driven Ansible credential.
3. Write rulebook rules that match on problem title, severity, impacted entity and status, and map the entity to a host name.
4. Add a `run_job_template` action for each approved problem type and pass the problem identifier as an extra variable.
5. Start the rulebook activation with `ansible.eda.rulebook_activation` and trigger a test problem.
6. In the job, check that the problem closes, and add a comment or ticket with the result.
7. Use the `dynatrace.oneagent.oneagent` role to install OneAgent on hosts that have no monitoring yet.

## Success Criteria

1. A new problem of an approved type starts one job for the right host.
2. Dynatrace shows the problem as closed after the fix.
3. Problems with no rule are ignored or only reported, never acted on.
4. The job output holds the Dynatrace problem identifier for audit.

## Notes

- Start with the webhook path if Dynatrace workflows are already in use, because it removes polling.
- Follow the general pattern in [Build self-healing infrastructure from monitoring alerts](build-self-healing-infrastructure-from-monitoring-alerts.md).
- Roll out agents together with the other tools in [Roll out monitoring agents at scale](roll-out-monitoring-agents-at-scale.md).
