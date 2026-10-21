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

## Notes

- Start with the webhook path if Dynatrace workflows are already in use, because it removes polling.
- Follow the general pattern in [Build self-healing infrastructure from monitoring alerts](build-self-healing-infrastructure-from-monitoring-alerts.md).
- Roll out agents together with the other tools in [Roll out monitoring agents at scale](roll-out-monitoring-agents-at-scale.md).
