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

## Notes

- For rolling firmware or driver updates, combine host maintenance mode with the vendor firmware jobs in [Update server firmware and BIOS](../infrastructure/update-server-firmware-and-bios.md).
- `cloud.vmware_ops` also provides playbooks to deploy a vCenter appliance on an ESXi host (`provision_vcenter`) and a nested ESXi host (`provision_virtual_esxi`), which are useful for lab and rebuild scenarios.
- `vmware.vmware.key_provider_native` and `vmware.vmware.key_provider_standard` manage vCenter key providers when encryption is part of the standard.
- Pair with [Provision VMware virtual machines](provision-vmware-virtual-machines.md).
