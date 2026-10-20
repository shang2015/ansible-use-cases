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

## Prerequisites

1. SAP installation media and SAP S-user access to download them, stored in a location the hosts can reach.
2. RHEL for SAP Solutions subscriptions and repositories.
3. A target platform: VMware, a hyperscaler, OpenShift Virtualization or bare metal, with sizing approved by SAP.
4. The landscape design: SIDs, instance numbers, host names, storage layout and, for HA, virtual IP addresses.

## Steps

1. Provision the hosts with `redhat.sap_infrastructure.sap_vm_provision` or the platform's own use case, and verify them with `redhat.sap_infrastructure.sap_vm_verify`.
2. Prepare the operating system with `redhat.sap_install.sap_general_preconfigure` and `redhat.sap_install.sap_hana_preconfigure` (and `redhat.sap_install.sap_netweaver_preconfigure` for application servers).
3. Create file systems and volumes with `redhat.sap_install.sap_storage_setup`.
4. Locate and extract the media with `redhat.sap_install.sap_install_media_detect`.
5. Install SAP HANA with `redhat.sap_install.sap_hana_install`, and the SAP application with `redhat.sap_install.sap_swpm`.
6. Install the SAP Host Agent with `redhat.sap_install.sap_hostagent`.
7. For high availability, configure HANA system replication with `redhat.sap_install.sap_ha_install_hana_hsr` and the Pacemaker cluster with `redhat.sap_install.sap_ha_pacemaker_cluster`.
8. Run the checks from `sap.sap_operations`, such as `sap.sap_operations.system_info`, and record the results.

## Success Criteria

1. The operating system passes the SAP preconfiguration checks.
2. SAP HANA and the SAP application start, and `sap.sap_operations.system_info` shows the expected instances.
3. For HA setups, the cluster is healthy and a controlled failover works.
4. The same inventory and variables rebuild an equivalent system.

## Notes

- Continue with [Run SAP Day 2 operations](run-sap-day-2-operations.md).
- The collection contains sample playbooks for single-node, distributed and two-node cluster installs. Start from the one that matches the design.
- Database tier alternatives are in [Install PostgreSQL and SQL Server](install-postgresql-and-sql-server.md).
