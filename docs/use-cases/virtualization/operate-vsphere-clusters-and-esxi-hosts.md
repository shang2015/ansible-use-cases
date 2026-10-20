---
title: Operate vSphere clusters and ESXi hosts
summary: Add, patch-prepare, maintain and standardise ESXi hosts and cluster settings (HA, DRS, services) as code.
order: 30
personas: [Virtualization administrator, Platform engineer]
collections: [vmware.vmware, cloud.vmware_ops]
key_content:
  - vmware.vmware.cluster
  - vmware.vmware.cluster_ha
  - vmware.vmware.cluster_drs
  - vmware.vmware.esxi_maintenance_mode
  - vmware.vmware.esxi_info
  - vmware.vmware.vcsa_backup_schedule
  - cloud.vmware_ops.cluster_settings
  - cloud.vmware_ops.esxi_maintenance_mode
---

# Operate vSphere clusters and ESXi hosts

## Description

Keep the vSphere platform consistent: clusters have the same HA and DRS settings, hosts are added and removed the same way, maintenance is entered and exited safely, and the vCenter appliance is backed up. Defining this in Ansible lets a team rebuild or compare environments instead of relying on tribal knowledge.

## Prerequisites

1. vCenter administrator credentials (or a dedicated automation role) stored in Automation Platform.
2. A defined cluster standard: HA admission control, DRS automation level, vCLS placement and services on each host.
3. For adding hosts: reachable ESXi hosts with root credentials and agreed licensing.
4. A backup target and schedule for the vCenter Server Appliance.

## Steps

1. Inventory the platform with `vmware.vmware.cluster_info`, `vmware.vmware.esxi_info`, `vmware.vmware.appliance_info` and `vmware.vmware.license_info`, and keep the output as a baseline report.
2. Create or update clusters with `vmware.vmware.cluster`, then set HA and DRS with `vmware.vmware.cluster_ha` and `vmware.vmware.cluster_drs`. The `cloud.vmware_ops.cluster_settings` role bundles these settings.
3. Add hosts to vCenter with `vmware.vmware.esxi_host`, or the `cloud.vmware_ops.esxi_management.add_esxi_host_to_vcenter` playbook, and manage connection state with `vmware.vmware.esxi_connection`.
4. Configure host services with `vmware.vmware.esxi_service`, and vCenter settings with `vmware.vmware.vcsa_settings`.
5. Before hardware or firmware work, enter maintenance mode with `vmware.vmware.esxi_maintenance_mode` (or the `cloud.vmware_ops.esxi_maintenance_mode` role). Exit it afterwards and confirm the host reconnects.
6. Configure the VCSA backup with `vmware.vmware.vcsa_backup_schedule` and confirm it with `vmware.vmware.vcsa_backup_schedule_info`.
7. Schedule a drift report that compares live cluster settings with the standard and raises a ticket on differences.

## Success Criteria

1. All clusters report the same HA and DRS settings as the defined standard.
2. A host can be added, placed in maintenance and returned to service by a single job.
3. A vCenter backup schedule exists and its configuration is reported as enabled.
4. The baseline report of clusters, hosts and licences is produced on a schedule.

## Notes

- For rolling firmware or driver updates, combine host maintenance mode with the vendor firmware jobs in [Update server firmware and BIOS](../infrastructure/update-server-firmware-and-bios.md).
- `cloud.vmware_ops` also provides playbooks to deploy a vCenter appliance on an ESXi host (`provision_vcenter`) and a nested ESXi host (`provision_virtual_esxi`), which are useful for lab and rebuild scenarios.
- `vmware.vmware.key_provider_native` and `vmware.vmware.key_provider_standard` manage vCenter key providers when encryption is part of the standard.
- Pair with [Provision VMware virtual machines](provision-vmware-virtual-machines.md).
