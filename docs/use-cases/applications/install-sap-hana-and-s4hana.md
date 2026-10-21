---
title: Install SAP HANA and S/4HANA
summary: Prepare RHEL, provision virtual machines and install SAP HANA, NetWeaver and high-availability clusters with certified roles.
order: 120
personas: [SAP Basis administrator, Linux administrator, Infrastructure architect]
collections: [redhat.sap_install, redhat.sap_infrastructure, sap.sap_operations]
key_content:
  - redhat.sap_infrastructure.sap_vm_provision
  - redhat.sap_install.sap_general_preconfigure
  - redhat.sap_install.sap_hana_preconfigure
  - redhat.sap_install.sap_storage_setup
  - redhat.sap_install.sap_hana_install
  - redhat.sap_install.sap_swpm
  - redhat.sap_install.sap_ha_pacemaker_cluster
  - redhat.sap_install.sap_install_media_detect
---

# Install SAP HANA and S/4HANA

## Description

SAP landscapes are installed from code, so that every system is built to the same Red Hat and SAP recommendations. Ansible provisions the virtual machine, prepares RHEL, sets up storage, installs SAP HANA and the application layer with SAP Software Provisioning Manager, and optionally builds the high-availability cluster.

## Notes

- Continue with [Run SAP Day 2 operations](run-sap-day-2-operations.md).
- The collection contains sample playbooks for single-node, distributed and two-node cluster installs. Start from the one that matches the design.
- Database tier alternatives are in [Install PostgreSQL and SQL Server](install-postgresql-and-sql-server.md).
