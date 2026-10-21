---
title: Act on LogicMonitor Edwin AI alerts
summary: Use the correlated alerts from LogicMonitor Edwin AI as Event-Driven Ansible events and start remediation.
order: 60
personas: [SRE, Operations lead, Observability engineer]
collections: [logicmonitor.edwin_ai, logicmonitor.integration, ansible.eda, ansible.controller]
key_content:
  - logicmonitor.edwin_ai.alerts
  - logicmonitor.edwin_ai.kafka
  - logicmonitor.edwin_ai.webhook
  - logicmonitor.edwin_ai.query_api
  - logicmonitor.integration.lm_device
  - ansible.controller.job_template
---

# Act on LogicMonitor Edwin AI alerts

## Description

LogicMonitor Edwin AI correlates and reduces alert noise into fewer, more meaningful alerts. Event-Driven Ansible consumes those alerts and starts remediation for the ones with a known fix, so automation works on an incident and not on dozens of duplicate symptoms.

## Notes

- Choose Kafka when alert volumes are high or when delivery must survive controller downtime.
- See [Build self-healing infrastructure from monitoring alerts](build-self-healing-infrastructure-from-monitoring-alerts.md) for the shared pattern, and [React to Kafka and webhook event streams](react-to-kafka-and-webhook-event-streams.md) for source details.
