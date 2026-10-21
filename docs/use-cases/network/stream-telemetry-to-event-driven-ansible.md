---
title: Stream telemetry into Event-Driven Ansible
summary: Configure model-driven telemetry on network devices and use the events to trigger remediation and health checks.
order: 160
personas: [Network engineer, Automation architect, NOC engineer]
collections: [network.telemetry, network.healthchecks, kentik.ansible_eda]
key_content:
  - network.telemetry.deploy
  - network.telemetry.deploy_collector
  - network.telemetry.health_checks
  - network.telemetry.detect
  - network.telemetry.remediate
  - kentik.ansible_eda.kentik_webhook
examples:
  - title: network.telemetry validated collection
    url: https://github.com/redhat-cop/network.telemetry
    note: telemetry configuration roles with Event-Driven Ansible integration
---

# Stream telemetry into Event-Driven Ansible

## Description

React to what the network reports instead of waiting for a schedule. Devices stream telemetry to a collector, and the events reach Event-Driven Ansible, which starts a diagnostic or remediation job in Automation Platform when a condition is met.

## Notes

- Start with rules that collect data and notify, and add automatic remediation after the results have been reviewed.
- Related: [Validate operational state and health checks](validate-operational-state-and-health-checks.md).
- Other event sources for network use cases include syslog and monitoring webhooks.
