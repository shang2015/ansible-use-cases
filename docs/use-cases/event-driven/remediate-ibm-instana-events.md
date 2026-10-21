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

## Notes

- Publish the Event-Driven Ansible endpoint through a load balancer or an event stream if Instana cannot reach the controller directly.
- Follow [Build self-healing infrastructure from monitoring alerts](build-self-healing-infrastructure-from-monitoring-alerts.md) for design guidance.
