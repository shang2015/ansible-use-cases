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

## Notes

- Use Kafka rather than direct webhooks when the sender cannot retry, or when events must be buffered.
- Avoid putting secrets in events. Use credentials in Automation Platform for the job itself.
- Observability tools that offer their own source plugins are covered by the vendor pages, starting with [Build self-healing infrastructure from monitoring alerts](build-self-healing-infrastructure-from-monitoring-alerts.md).
