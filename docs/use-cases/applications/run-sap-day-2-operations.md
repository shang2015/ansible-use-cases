---
title: Run SAP Day 2 operations
summary: Back up, update, patch and check SAP HANA and SAP systems, and orchestrate Avantra workflows, from Automation Platform.
order: 130
personas: [SAP Basis administrator, Operations lead]
collections: [sap.sap_operations, avantra.core, redhat.sap_install]
key_content:
  - sap.sap_operations.hana_backup
  - sap.sap_operations.hana_restore
  - sap.sap_operations.hana_update
  - sap.sap_operations.sap_kernel_update
  - sap.sap_operations.system
  - sap.sap_operations.pcs_status_info
  - sap.sap_operations.hana_system_replication_info
  - avantra.core.workflow_execution
---

# Run SAP Day 2 operations

## Description

Routine SAP administration, such as backups, start and stop, kernel and HANA updates, license handling and cluster checks, is run as controlled automation. Basis teams get the same procedure on every system, with approvals and logs, and fewer hand-typed commands.

## Prerequisites

1. Running SAP systems on RHEL, with an inventory that groups hosts by SID and role.
2. SAP user credentials for downloads and a HANA account for backups, stored in Automation Platform.
3. A change process and maintenance windows for stop, update and start operations.
4. Optional: an Avantra installation and an API token if Avantra workflows are used.

## Steps

1. Collect the current state of each system with `sap.sap_operations.system_info`, `sap.sap_operations.host_info` and `sap.sap_operations.hana_system_replication_info`.
2. Run HANA backups with `sap.sap_operations.hana_backup` on a schedule, and test restores with `sap.sap_operations.hana_restore` on a non-production system.
3. Stop and start systems and services in order with `sap.sap_operations.system` and `sap.sap_operations.service`.
4. Update the SAP kernel with the `sap.sap_operations.sap_kernel_update` role and the HANA database with the `sap.sap_operations.hana_update` role, after a backup.
5. For clusters, check status before and after with `sap.sap_operations.pcs_status_info` and the `sap.sap_operations.pcs_config_checks` role.
6. Import ABAP transports with `sap.sap_operations.abap_transport_import` as a step in a release workflow.
7. Call Avantra from the same workflows with `avantra.core.workflow_execution`, to start monitoring or maintenance workflows, and read systems with `avantra.core.sapsystem_info`.
8. Combine the steps in workflows with approvals, notifications and a change record.

## Success Criteria

1. Backups are taken on schedule, and a restore test succeeds.
2. Planned maintenance runs in the right order, and the system is healthy afterwards.
3. Cluster and replication checks pass before and after each change.
4. Each operation has a job record with the user, time and result.

## Notes

- The system build is in [Install SAP HANA and S/4HANA](install-sap-hana-and-s4hana.md).
- Use [Shut down and start up a multi-tier application](shut-down-and-start-up-multi-tier-applications.md) when SAP is one part of a larger stack.
- Take care with restores: always require an explicit approval.
