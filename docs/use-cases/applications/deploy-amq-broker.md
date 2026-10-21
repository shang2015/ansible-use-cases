---
title: Deploy AMQ Broker messaging
summary: Install and configure Red Hat AMQ Broker (ActiveMQ Artemis) standalone or as a primary/backup pair.
order: 80
personas: [Middleware administrator, Integration engineer]
collections: [redhat.amq_broker, redhat.runtimes_common]
key_content:
  - redhat.amq_broker.activemq
  - redhat.amq_broker.activemq_cluster
  - redhat.amq_broker.activemq_facts
  - redhat.amq_broker.activemq_uninstall
  - redhat.runtimes_common.product_download
---

# Deploy AMQ Broker messaging

## Description

Messaging brokers are installed with the same security and queue configuration in every environment. The automation builds standalone brokers or primary and backup pairs, configures addresses, queues and users, and removes brokers cleanly when they are retired.

## Notes

- For event streaming see [Deploy Apache Kafka with AMQ Streams or Confluent Platform](deploy-kafka-with-amq-streams-or-confluent.md).
- Event-Driven Ansible can consume the same Kafka topics, see [React to Kafka and webhook event streams](../event-driven/react-to-kafka-and-webhook-event-streams.md).
