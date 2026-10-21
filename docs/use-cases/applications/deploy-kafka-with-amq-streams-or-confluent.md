---
title: Deploy Apache Kafka with AMQ Streams or Confluent Platform
summary: Install Kafka clusters on RHEL hosts with Red Hat AMQ Streams or Confluent Platform and validate their health.
order: 90
personas: [Platform engineer, Integration architect, Middleware administrator]
collections: [redhat.amq_streams, confluent.platform]
key_content:
  - redhat.amq_streams.amq_streams_kraft
  - redhat.amq_streams.amq_streams_broker
  - redhat.amq_streams.amq_streams_connect
  - redhat.amq_streams.amq_streams_exporter
  - confluent.platform.kafka_broker
  - confluent.platform.kafka_controller
  - confluent.platform.schema_registry
  - confluent.platform.kafka_connectors
---

# Deploy Apache Kafka with AMQ Streams or Confluent Platform

## Description

Event streaming clusters are built from the same inventory and variables every time. Ansible installs the brokers, controllers and supporting services, applies security settings and validates the cluster. Two certified options are covered: Red Hat AMQ Streams, and Confluent Platform.

## Notes

- Confluent playbooks also support support-bundle collection when a run fails, which helps with vendor cases.
- Use [React to Kafka and webhook event streams](../event-driven/react-to-kafka-and-webhook-event-streams.md) to start automation from the topics.
- For traditional queues and topics see [Deploy AMQ Broker messaging](deploy-amq-broker.md).
