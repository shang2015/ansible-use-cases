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

## Notes

- Use Data Grid together with [Deploy and patch JBoss EAP](deploy-and-patch-jboss-eap.md) for session clustering.
