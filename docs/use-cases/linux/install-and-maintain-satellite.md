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

## Prerequisites

1. RHEL hosts sized and registered for Satellite and for each Capsule, with Satellite repositories enabled and the Satellite packages installed.
2. A subscription manifest, or Red Hat Customer Portal credentials to download it.
3. DNS records and certificates for each Satellite and Capsule host.
4. SSH access with privilege escalation to those hosts, and Satellite administrator credentials stored as automation controller credentials.

## Steps

1. Prepare the host: registration, firewall, time sync and dedicated storage, for example with `redhat.rhel_system_roles.rhc`, `redhat.rhel_system_roles.firewall`, `redhat.rhel_system_roles.timesync` and `redhat.rhel_system_roles.storage`.
2. Run `redhat.satellite_operations.installer` with the Satellite scenario, initial organization and administrator options.
3. Load the manifest with the `redhat.satellite.manifest` role, or `redhat.satellite.subscription_manifest` if the file is already available.
4. For each Capsule, create the certificate bundle on Satellite with `redhat.satellite_operations.capsule_certs_generate`, run the installer on the Capsule host with the Capsule scenario, then assign organizations and locations with `redhat.satellite.smart_proxy`.
5. Schedule backups with `redhat.satellite_operations.backup` (full weekly, incremental otherwise) and set the retention and destination variables.
6. Add monitoring with `redhat.satellite_operations.metrics` (Performance Co-Pilot and Grafana), and enable remote remediation from Red Hat Insights with `redhat.satellite_operations.cloud_connector`.
7. Add a recurring health check job that calls `redhat.satellite.status_info` and notifies on failure.

## Success Criteria

1. The Satellite web UI and API respond, and the manifest shows the expected subscriptions.
2. Every Capsule is listed in Satellite, assigned to its organization and location, and passes feature checks.
3. Backups run on schedule and the newest full backup is in the configured destination.
4. Metrics are visible in Grafana for the Satellite host.

## Notes

- The next step is [Configure Satellite as code](configure-satellite-as-code.md), which defines organizations, products, content views and activation keys.
- Test restores from the backup periodically; a backup that was never restored is not proof of recovery.
- `redhat.satellite_operations` has no dedicated upgrade role, so run Satellite version upgrades from a separate job template and keep a fresh backup before each one.
