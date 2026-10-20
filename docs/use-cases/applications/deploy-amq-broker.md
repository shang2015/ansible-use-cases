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

## Prerequisites

1. RHEL hosts with SSH access and privilege escalation, a supported Java runtime and, for pairs, shared storage or a replication network.
2. Entitlement and download location for the AMQ Broker archive.
3. Design of the broker topology, addresses and queues, users and roles, and TLS certificates.

## Steps

1. Download the product with `redhat.runtimes_common.product_download` or an internal file server.
2. Install and configure a broker with the `redhat.amq_broker.activemq` role, setting acceptors, security settings, addresses and queues in variables.
3. For high availability, use the collection playbook `redhat.amq_broker.activemq_cluster` to deploy a primary and backup pair with a shared data directory.
4. Read back the effective configuration with `redhat.amq_broker.activemq_facts` and keep it as a report.
5. Test with a producer and a consumer, and verify failover by stopping the primary during a test.
6. Update the broker by running the role with a new version, one node at a time.
7. Remove a broker with `redhat.amq_broker.activemq_uninstall`.

## Success Criteria

1. The broker or pair starts as a service and accepts authenticated connections.
2. Configured addresses and queues exist, and unauthorised users are denied.
3. Failover moves clients to the backup within the agreed time.

## Notes

- For event streaming see [Deploy Apache Kafka with AMQ Streams or Confluent Platform](deploy-kafka-with-amq-streams-or-confluent.md).
- Event-Driven Ansible can consume the same Kafka topics, see [React to Kafka and webhook event streams](../event-driven/react-to-kafka-and-webhook-event-streams.md).
