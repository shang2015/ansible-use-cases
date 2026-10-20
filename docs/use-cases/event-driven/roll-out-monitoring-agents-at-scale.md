---
title: Roll out monitoring agents at scale
summary: Deploy and keep current the Datadog, Dynatrace, Splunk, Zabbix and OpenTelemetry agents so that events have a source.
order: 130
personas: [Observability engineer, Linux administrator, Operations lead]
collections: [datadog.dd, dynatrace.oneagent, cisco.splunk_otel_collector, splunk.enterprise, zabbix.zabbix]
key_content:
  - datadog.dd.agent
  - dynatrace.oneagent.oneagent
  - cisco.splunk_otel_collector.collector
  - splunk.enterprise.splunk_universal_forwarder_linux
  - splunk.enterprise.win_splunk_universal_forwarder
  - zabbix.zabbix.agent
---

# Roll out monitoring agents at scale

## Description

Event-Driven remediation only works for hosts that are monitored. This use case installs, configures and upgrades the monitoring agent of the chosen platform on all servers, and applies it automatically to new builds.

## Prerequisites

1. A chosen monitoring platform and its API keys, tokens or connection settings, stored as credentials.
2. An inventory of the hosts in scope, grouped by operating system.
3. Network access from hosts to the monitoring backend or collector, or to a local proxy.
4. A change window for the first rollout, and a test group of hosts.

## Steps

1. Select the role for the platform: `datadog.dd.agent`, `dynatrace.oneagent.oneagent`, `cisco.splunk_otel_collector.collector`, `zabbix.zabbix.agent`, or the Splunk Universal Forwarder modules for Linux and Windows.
2. Put tokens and server addresses into Automation Platform credentials and pass them as variables.
3. Create a job template for each platform and run it on the test group first.
4. Verify that the hosts report to the platform, using the platform check or the `splunk.enterprise.splunk_universal_forwarder_linux_info` module where it applies.
5. Roll out in batches, and schedule a recurring run to keep configuration and version in step.
6. Call the same job from the provisioning workflow so that new servers are monitored from the first day.

## Success Criteria

1. All in-scope hosts report to the monitoring platform.
2. Agent versions and settings match the standard.
3. New servers appear in monitoring without a manual ticket.

## Notes

- Install only one agent per purpose to avoid duplicate data and cost.
- Once hosts are monitored, use [Build self-healing infrastructure from monitoring alerts](build-self-healing-infrastructure-from-monitoring-alerts.md) to act on their alerts.
