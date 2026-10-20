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

## Prerequisites

1. Devices that support the telemetry method used. The `network.telemetry` roles target model-driven telemetry, with the health check role aimed at Cisco NX-OS.
2. A host for the collector and a route to it from the devices.
3. An Event-Driven Ansible controller connected to Automation Platform, and the job templates to run.
4. Agreed conditions that justify an automatic response, and the actions allowed for each.

## Steps

1. Deploy the collection infrastructure with the `network.telemetry.deploy_collector` role, which sets up a containerized Telegraf collector.
2. Configure telemetry subscriptions and destinations on the devices with the `network.telemetry.deploy` role from data stored in a data store.
3. Check the telemetry setup with `network.telemetry.health_checks`.
4. Write a rulebook that listens to the telemetry or alert source and matches conditions. For example `kentik.ansible_eda.kentik_webhook` receives alert webhooks from Kentik.
5. Map each rule to a job template: a health check from `network.healthchecks`, a data collection job, or a remediation job.
6. Keep the telemetry configuration itself consistent with `network.telemetry.detect` and `network.telemetry.remediate`.

## Success Criteria

1. Devices stream data to the collector, and the health check shows a good state.
2. A test event starts the mapped job template within the expected time.
3. Every automatic action is logged with the event that caused it.
4. Telemetry configuration drift is detected and corrected.

## Notes

- Start with rules that collect data and notify, and add automatic remediation after the results have been reviewed.
- Related: [Validate operational state and health checks](validate-operational-state-and-health-checks.md).
- Other event sources for network use cases include syslog and monitoring webhooks.
