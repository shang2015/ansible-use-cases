---
title: Deploy Red Hat Data Grid and caches
summary: Install Data Grid (Infinispan) servers and create caches at runtime with Ansible.
order: 100
personas: [Middleware administrator, Application owner]
collections: [redhat.data_grid, redhat.runtimes_common]
key_content:
  - redhat.data_grid.infinispan
  - redhat.data_grid.infinispan_cache
  - redhat.runtimes_common.product_download
---

# Deploy Red Hat Data Grid and caches

## Description

In-memory data grids hold session data and fast-changing application data. The automation installs a Data Grid cluster with the same security and clustering settings on every node, and creates or changes caches without restarting the servers.

## Prerequisites

1. RHEL hosts with SSH access and privilege escalation and a supported Java runtime.
2. Data Grid entitlement and a download location.
3. Cluster design: node count, discovery method, authentication, TLS and cache definitions.

## Steps

1. Download the server with `redhat.runtimes_common.product_download`.
2. Install and cluster the nodes with the `redhat.data_grid.infinispan` role, or the collection playbook of the same name.
3. Define the caches (mode, expiration, memory limits) as variables and create them with the `redhat.data_grid.infinispan_cache` role.
4. Check cluster membership and a read/write test from an application host.
5. Change cache settings through the same variables and re-run the job, which applies the change at runtime.
6. Schedule validation, and update nodes one at a time.

## Success Criteria

1. All nodes form one cluster and report the expected members.
2. Defined caches exist on the cluster with the agreed settings.
3. Adding a cache needs only a variable change and a job run.

## Notes

- Use Data Grid together with [Deploy and patch JBoss EAP](deploy-and-patch-jboss-eap.md) for session clustering.
