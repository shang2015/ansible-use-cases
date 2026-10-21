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

## Notes

- Other load balancers have their own collections in the network domain, so replace the pool member step to suit.
- Use this pattern for [Deploy and patch JBoss EAP](deploy-and-patch-jboss-eap.md), [Deploy JBoss Web Server and JBoss Core Services](deploy-jboss-web-server-and-core-services.md), and database node maintenance.
- Run it from a workflow that adds approval and a ServiceNow change, see [Automate change requests with approval gates](../itsm/automate-change-requests-with-approval-gates.md).
