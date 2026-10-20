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

## Prerequisites

1. RHEL hosts with SSH access and a service account that can use privilege escalation.
2. JBoss EAP entitlement and access to the installation archive or patch, either from the Red Hat Customer Portal or from an internal repository.
3. A Java runtime supported by the target EAP version.
4. A standard configuration (ports, users, subsystems, JVM options) agreed by the application teams.

## Steps

1. Make the installation files available on the control side or on an internal server, using `redhat.runtimes_common.product_download` or `redhat.redhat_csp_download.redhat_csp_download`.
2. Install the server with the `redhat.eap.wildfly_install` role and register it as a service with `redhat.eap.wildfly_systemd`. Open the required ports with `redhat.eap.wildfly_firewalld`.
3. Configure subsystems, such as logging, security domains and data sources, with `redhat.eap.wildfly_subs`, and add JDBC drivers with `redhat.eap.wildfly_driver`.
4. Take a configuration snapshot with `redhat.eap.wildfly_snapshot` before every change, so that it can be rolled back.
5. Apply a version update or patch by running the install role with the new version, restart through the service, and check with `redhat.eap.wildfly_validation`.
6. Start, stop and restart servers through systemd from the same job template, using tags or survey choices for the action.
7. Remove a server and its files with `redhat.eap.wildfly_uninstall`, and clean up users, firewall rules and data directories.
8. Create job templates for install, configure, patch and uninstall, and add a schedule or approval where the process requires it.

## Success Criteria

1. A new EAP host is built from the playbooks and passes validation without manual steps.
2. Servers on the same environment have identical configuration, and drift can be detected by re-running the job in check mode.
3. A patch run produces a snapshot first, and a failed update can be rolled back.
4. Uninstall leaves no service, firewall rule or install directory behind.

## Notes

- Deploy the applications themselves with [Deploy applications from a Maven repository](deploy-applications-from-a-maven-repository.md).
- For clusters patch node by node with [Patch application nodes one at a time behind a load balancer](patch-application-nodes-behind-a-load-balancer.md).
- Use `redhat.eap.wildfly_migration` to move configuration between versions where supported.
- The same roles manage upstream WildFly, which is useful for development environments.
