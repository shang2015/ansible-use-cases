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

## Prerequisites

1. LogicMonitor with Edwin AI enabled and access credentials for its API.
2. Event-Driven Ansible controller with a decision environment that includes `logicmonitor.edwin_ai`.
3. Job templates for approved fixes and an inventory whose host names match the devices in LogicMonitor.

## Steps

1. Pick the delivery method for Edwin AI alerts: `logicmonitor.edwin_ai.alerts`, `logicmonitor.edwin_ai.kafka` or `logicmonitor.edwin_ai.webhook`.
2. Write the rulebook with that source and rules on alert severity, resource and correlated incident, using `run_job_template` for approved fixes.
3. In the job, look up more detail on the alert with `logicmonitor.edwin_ai.query_api`.
4. Use `logicmonitor.integration.lm_device` and the other `logicmonitor.integration` modules to keep devices, groups and collectors in LogicMonitor in step with the inventory, for example after builds and decommissions.
5. Test with the `logicmonitor.edwin_ai.debug_event` playbook or a test alert, then start the activation.
6. Add verification and a ticket or note for the outcome.

## Success Criteria

1. A correlated alert of an approved type starts one job, not one per symptom.
2. LogicMonitor shows devices that match the automation inventory.
3. The job output links back to the Edwin AI alert.

## Notes

- Choose Kafka when alert volumes are high or when delivery must survive controller downtime.
- See [Build self-healing infrastructure from monitoring alerts](build-self-healing-infrastructure-from-monitoring-alerts.md) for the shared pattern, and [React to Kafka and webhook event streams](react-to-kafka-and-webhook-event-streams.md) for source details.
