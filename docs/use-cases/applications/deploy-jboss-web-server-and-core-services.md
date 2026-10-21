---
title: Deploy JBoss Web Server and JBoss Core Services
summary: Install and configure Tomcat-based JBoss Web Server and Apache httpd-based JBoss Core Services with validation.
order: 20
personas: [Middleware administrator, Web operations engineer]
collections: [redhat.jws, redhat.jbcs, redhat.runtimes_common]
key_content:
  - redhat.jws.jws
  - redhat.jws.jws_validation
  - redhat.jbcs.jbcs
  - redhat.runtimes_common.product_download
  - redhat.runtimes_common.xml
---

# Deploy JBoss Web Server and JBoss Core Services

## Description

Web and servlet tiers are built the same way every time. JBoss Web Server (Apache Tomcat) hosts Java web applications, and JBoss Core Services (Apache HTTP Server) acts as the front end. The automation installs, configures, restarts, upgrades and removes both, with validation after each change.

## Notes

- Combine with [Patch application nodes one at a time behind a load balancer](patch-application-nodes-behind-a-load-balancer.md) for rolling upgrades.
- Application files are deployed separately, see [Deploy applications from a Maven repository](deploy-applications-from-a-maven-repository.md).
