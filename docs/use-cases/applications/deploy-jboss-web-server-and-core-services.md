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

## Prerequisites

1. RHEL hosts with SSH access and privilege escalation.
2. Entitlement for the JBoss Web Server and Core Services archives, and a location from which to download them.
3. A design for the tiers: which hosts run Tomcat, which run the web front end, ports and TLS certificates.
4. A supported Java runtime on the Tomcat hosts.

## Steps

1. Download the products with `redhat.runtimes_common.product_download`, or use an internal file server.
2. Install and configure Tomcat on the application hosts with the `redhat.jws.jws` role, setting ports, users, connectors and JVM options through variables.
3. Install the web front end with the `redhat.jbcs.jbcs` role and configure virtual hosts, TLS and proxy settings.
4. Edit XML configuration files that the roles do not cover with `redhat.runtimes_common.xml`.
5. Run `redhat.jws.jws_validation` and a request test through the front end to prove that the whole path works.
6. Run the same roles with a new version to upgrade, and use the service state for start, stop and restart jobs.
7. Create job templates for install, configuration change and upgrade, and a clean-up job for decommissioning.

## Success Criteria

1. Tomcat and the web front end start as services and answer a test request.
2. Configuration is identical across hosts of the same tier.
3. An upgrade job completes with validation passing and no manual edits.

## Notes

- Combine with [Patch application nodes one at a time behind a load balancer](patch-application-nodes-behind-a-load-balancer.md) for rolling upgrades.
- Application files are deployed separately, see [Deploy applications from a Maven repository](deploy-applications-from-a-maven-repository.md).
