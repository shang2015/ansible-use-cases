---
title: Patch application nodes one at a time behind a load balancer
summary: Drain, update and return each application node to the load balancer in turn so the service stays available.
order: 30
personas: [Middleware administrator, Operations lead, Application owner]
collections: [f5networks.f5_modules, redhat.eap, redhat.jws, redhat.runtimes_common]
key_content:
  - f5networks.f5_modules.bigip_pool_member
  - redhat.eap.wildfly_snapshot
  - redhat.eap.wildfly_install
  - redhat.eap.wildfly_validation
  - redhat.jws.jws_validation
  - redhat.runtimes_common.tail_grep
---

# Patch application nodes one at a time behind a load balancer

## Description

Clustered application servers are updated without an outage. A playbook takes one node at a time out of the load balancer pool, stops traffic, patches or reconfigures it, checks health and puts it back, and only then moves to the next node.

## Prerequisites

1. An application tier with at least two nodes behind a load balancer, and spare capacity to run one node less.
2. Automation access to the load balancer API (this page uses F5 BIG-IP) and to the application hosts.
3. A health check that proves that a node serves traffic, for example an HTTP status URL.
4. A change window and an owner for rollback decisions.

## Steps

1. Group the nodes in the inventory by cluster and set the play to run with `serial: 1`, or a batch size that keeps enough capacity.
2. Disable the node in the pool with `f5networks.f5_modules.bigip_pool_member`, and wait until existing connections have drained.
3. Take a snapshot with `redhat.eap.wildfly_snapshot` and stop the application service.
4. Apply the update with `redhat.eap.wildfly_install` for EAP, or the `redhat.jws.jws` role for Tomcat, or the configuration change itself.
5. Start the service and wait for the server log to show a successful start with `redhat.runtimes_common.tail_grep`.
6. Validate with `redhat.eap.wildfly_validation` or `redhat.jws.jws_validation`, and a request to the health URL.
7. Enable the node in the pool again with `bigip_pool_member`, and continue with the next node only when the check passes.
8. Stop the run on the first failed node, leave it out of the pool and notify the owner.

## Success Criteria

1. The service stays available during the whole run, and no more than the planned number of nodes is out of the pool.
2. Every node that was changed passes validation before it receives traffic.
3. A failed node is left out of the pool with its snapshot available.

## Notes

- Other load balancers have their own collections in the network domain, so replace the pool member step to suit.
- Use this pattern for [Deploy and patch JBoss EAP](deploy-and-patch-jboss-eap.md), [Deploy JBoss Web Server and JBoss Core Services](deploy-jboss-web-server-and-core-services.md), and database node maintenance.
- Run it from a workflow that adds approval and a ServiceNow change, see [Automate change requests with approval gates](../itsm/automate-change-requests-with-approval-gates.md).
