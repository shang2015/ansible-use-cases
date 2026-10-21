---
title: Migrate OpenStack tenants and workloads
summary: Export projects, networks, images and instances from a source OpenStack cloud and import them into a destination cloud.
order: 30
personas: [Cloud engineer, Migration lead]
collections: [os_migrate.os_migrate]
key_content:
  - os_migrate.os_migrate.deploy_conversion_hosts
  - os_migrate.os_migrate.export_networks
  - os_migrate.os_migrate.import_networks
  - os_migrate.os_migrate.export_workloads
  - os_migrate.os_migrate.import_workloads
  - os_migrate.os_migrate.validate_data_dir
  - os_migrate.os_migrate.delete_conversion_hosts
examples:
  - title: OS-Migrate project
    url: https://github.com/os-migrate/os-migrate
    note: source repository of the os_migrate.os_migrate collection
---

# Migrate OpenStack tenants and workloads

## Description

Move a tenant from one OpenStack cloud to another, for example during a platform upgrade or consolidation. The collection exports the tenant's resources to files, recreates them in the destination, and copies instance data through conversion hosts.

## Notes

- Migrate in waves, starting with a low-risk tenant, and keep the source running until the destination is verified.
- Run the export and import steps from a workflow so each step is logged and repeatable.
- Plan for downtime of each instance during its final volume copy.
