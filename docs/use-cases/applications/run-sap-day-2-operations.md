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

## Notes

- The system build is in [Install SAP HANA and S/4HANA](install-sap-hana-and-s4hana.md).
- Use [Shut down and start up a multi-tier application](shut-down-and-start-up-multi-tier-applications.md) when SAP is one part of a larger stack.
- Take care with restores: always require an explicit approval.
