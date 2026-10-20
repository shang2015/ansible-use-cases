---
title: React to Kafka and webhook event streams
summary: Start automation from Kafka topics, webhooks and cloud queues using the event sources and event streams of Event-Driven Ansible.
order: 100
personas: [Automation engineer, Integration architect, SRE]
collections: [ansible.eda, ansible.controller, ansible.scm]
key_content:
  - ansible.eda.kafka
  - ansible.eda.webhook
  - ansible.eda.aws_sqs_queue
  - ansible.eda.azure_service_bus
  - ansible.eda.event_stream
  - ansible.eda.json_filter
  - ansible.controller.project_update
---

# React to Kafka and webhook event streams

## Description

Business and platform events often travel on Kafka topics, cloud queues or webhooks: a new order, a deployment record, a pushed commit or a cloud audit event. Event-Driven Ansible subscribes to them and launches the matching automation, so integrations no longer depend on polling or on scheduled jobs.

## Prerequisites

1. The event producer and the connection details: Kafka brokers and topic, queue URL or webhook sender.
2. Event-Driven Ansible controller with a decision environment that contains the needed sources.
3. Network and credentials for the controller to reach the broker or queue, or for the sender to reach the controller.
4. A written event schema, even a short one, so rules can rely on stable field names.

## Steps

1. Choose the source: `ansible.eda.kafka` for topics, `ansible.eda.aws_sqs_queue` or `ansible.eda.azure_service_bus` for cloud queues, and `ansible.eda.webhook` for HTTP callbacks.
2. For webhooks, create an event stream in the Event-Driven Ansible controller with `ansible.eda.event_stream`, choose its authentication type and give the sender the endpoint.
3. Write the rulebook with conditions on the event fields. Use `ansible.eda.json_filter` to remove large or sensitive keys, and `ansible.eda.dashes_to_underscores` or `ansible.eda.normalize_keys` to make keys usable in rules.
4. Use `run_job_template` or `run_workflow_template` to start automation, passing the event data as variables.
5. Make jobs idempotent and tolerate duplicates, because brokers can deliver the same message more than once.
6. For source-control events, send a push webhook from Git, and refresh the project with `ansible.controller.project_update` before the job runs. Use `ansible.scm` modules when a job needs to read or publish repository content.
7. Test with sample messages and watch the activation log, then enable it in the production environment.

## Success Criteria

1. A message on the topic or a call to the endpoint starts the expected job once.
2. Malformed or unexpected events are ignored and logged.
3. The rulebook activation recovers after a broker or controller restart.

## Notes

- Use Kafka rather than direct webhooks when the sender cannot retry, or when events must be buffered.
- Avoid putting secrets in events. Use credentials in Automation Platform for the job itself.
- Observability tools that offer their own source plugins are covered by the vendor pages, starting with [Build self-healing infrastructure from monitoring alerts](build-self-healing-infrastructure-from-monitoring-alerts.md).
