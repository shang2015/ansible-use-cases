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

## Notes

- Install only one agent per purpose to avoid duplicate data and cost.
- Once hosts are monitored, use [Build self-healing infrastructure from monitoring alerts](build-self-healing-infrastructure-from-monitoring-alerts.md) to act on their alerts.
