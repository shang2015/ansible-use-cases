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

## Prerequisites

1. Credentials (clouds.yaml entries) for the source and destination clouds, with enough rights to read and create the resources in scope.
2. A migration host with network access to both clouds, and an execution environment containing `os_migrate.os_migrate` and the OpenStack SDK.
3. An inventory of projects, networks, images, volumes and instances to migrate, with agreed downtime for each workload.
4. Free capacity and quotas in the destination.

## Steps

1. Create a data directory, and run the `os_migrate.os_migrate.validate_data_dir` playbook to confirm the layout.
2. Export the tenant resources with the export playbooks, for example `export_projects`, `export_networks`, `export_subnets`, `export_routers`, `export_security_groups`, `export_flavors`, `export_images`, and `export_keypairs`.
3. Review the exported YAML files, and edit them where the destination differs, for example different network names or flavors.
4. Import in dependency order with the matching playbooks, such as `import_projects`, `import_networks`, `import_subnets`, `import_routers`, `import_security_groups`, `import_images` and `import_keypairs`.
5. Deploy conversion hosts with `os_migrate.os_migrate.deploy_conversion_hosts`.
6. Export workloads with `os_migrate.os_migrate.export_workloads`, then import them with `os_migrate.os_migrate.import_workloads`, which copies the volume data.
7. Verify each workload, switch users to the destination, and clean up with `os_migrate.os_migrate.delete_conversion_hosts`.

## Success Criteria

1. The destination contains the projects, networks, security groups and images listed in the plan.
2. Migrated instances boot in the destination with their data and expected addresses or equivalents.
3. The exported resource files are kept under version control as a record of what moved.
4. Conversion hosts are removed after the migration.

## Notes

- Migrate in waves, starting with a low-risk tenant, and keep the source running until the destination is verified.
- Run the export and import steps from a workflow so each step is logged and repeatable.
- Plan for downtime of each instance during its final volume copy.
