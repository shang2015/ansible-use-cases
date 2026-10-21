---
title: Deploy and patch JBoss EAP
summary: Install, configure, update and remove Red Hat JBoss Enterprise Application Platform servers with repeatable Day 1 and Day 2 automation.
order: 10
personas: [Middleware administrator, Application owner, Operations lead]
collections: [redhat.eap, redhat.runtimes_common, redhat.redhat_csp_download]
key_content:
  - redhat.eap.wildfly_install
  - redhat.eap.wildfly_systemd
  - redhat.eap.wildfly_subs
  - redhat.eap.wildfly_driver
  - redhat.eap.wildfly_snapshot
  - redhat.eap.wildfly_validation
  - redhat.eap.wildfly_uninstall
  - redhat.runtimes_common.product_download
examples:
  - title: redhat.eap collection
    url: https://github.com/ansible-middleware/wildfly
    note: roles for JBoss EAP and WildFly
---

# Deploy and patch JBoss EAP

## Description

JBoss EAP servers are installed, configured, patched and removed the same way on every host. The automation covers the full life cycle that administrators do by hand today: install and service setup, subsystem and data source configuration, a version update with a rollback point, and uninstall.

## Notes

- Deploy the applications themselves with [Deploy applications from a Maven repository](deploy-applications-from-a-maven-repository.md).
- For clusters patch node by node with [Patch application nodes one at a time behind a load balancer](patch-application-nodes-behind-a-load-balancer.md).
- Use `redhat.eap.wildfly_migration` to move configuration between versions where supported.
- The same roles manage upstream WildFly, which is useful for development environments.
