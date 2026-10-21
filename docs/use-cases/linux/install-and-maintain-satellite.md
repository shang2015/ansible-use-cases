---
title: Install and maintain Satellite and Capsules
summary: Install Satellite and Capsule servers, load the subscription manifest, and automate backups, metrics and Cloud Connector.
order: 20
personas: [Linux administrator, Platform engineer]
collections: [redhat.satellite_operations, redhat.satellite, redhat.rhel_system_roles]
key_content:
  - redhat.satellite_operations.installer
  - redhat.satellite_operations.capsule_certs_generate
  - redhat.satellite_operations.backup
  - redhat.satellite_operations.metrics
  - redhat.satellite_operations.cloud_connector
  - redhat.satellite.manifest
  - redhat.satellite.smart_proxy
  - redhat.satellite.status_info
examples:
  - title: redhat.satellite_operations collection
    url: https://github.com/RedHatSatellite/satellite-operations-collection
---

# Install and maintain Satellite and Capsules

## Description

Red Hat Satellite is the content, patch and provisioning hub for a RHEL estate. This use case automates the server side of that hub: installing Satellite and its Capsules, loading the subscription manifest and setting up the routine operations (backups, metrics, health checks) so every site is built the same way.

## Notes

- The next step is [Configure Satellite as code](configure-satellite-as-code.md), which defines organizations, products, content views and activation keys.
- Test restores from the backup periodically; a backup that was never restored is not proof of recovery.
- `redhat.satellite_operations` has no dedicated upgrade role, so run Satellite version upgrades from a separate job template and keep a fresh backup before each one.
