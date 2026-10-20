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

## Prerequisites

1. At least three RHEL hosts for brokers or controllers, with fast storage and network connectivity between them.
2. Entitlements or licences and package access for the chosen product.
3. A design for listeners, authentication, TLS certificates, topics and retention.
4. DNS names for each node and open firewall ports between nodes.

## Steps

1. Define the inventory groups for the chosen product and the cluster variables.
2. For AMQ Streams, deploy with `redhat.amq_streams.amq_streams_kraft` and `redhat.amq_streams.amq_streams_broker` (the collection also has a Zookeeper role for existing clusters), with `redhat.amq_streams.amq_streams_common` setting up shared prerequisites.
3. For Confluent Platform, apply `confluent.platform.kafka_controller`, `confluent.platform.kafka_broker` and `confluent.platform.schema_registry`, and add other components such as `confluent.platform.kafka_connect` as needed.
4. Add Kafka Connect with `redhat.amq_streams.amq_streams_connect` and monitoring with `redhat.amq_streams.amq_streams_exporter`, or create connectors on Confluent with the `confluent.platform.kafka_connectors` module.
5. Run the validation: the `redhat.amq_streams.validate` playbook or `confluent.platform.health_check`.
6. Create topics and access rules, and test a producer and consumer.
7. Perform rolling restarts and updates one node at a time, using the product playbooks, and re-run the validation.

## Success Criteria

1. All nodes join the cluster and the validation passes.
2. Topics are created with the agreed replication and retention.
3. A node restart does not interrupt producers and consumers.
4. Re-running the playbooks does not change a healthy cluster.

## Notes

- Confluent playbooks also support support-bundle collection when a run fails, which helps with vendor cases.
- Use [React to Kafka and webhook event streams](../event-driven/react-to-kafka-and-webhook-event-streams.md) to start automation from the topics.
- For traditional queues and topics see [Deploy AMQ Broker messaging](deploy-amq-broker.md).
