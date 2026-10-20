---
title: Manage IBM Power systems with the HMC
summary: Create, resize, migrate and install Power partitions and Virtual I/O Servers through the Hardware Management Console, and keep inventory and firmware current.
order: 40
personas: [Power systems administrator, Infrastructure engineer]
collections: [ibm.power_hmc, ibm.power_vios]
key_content:
  - ibm.power_hmc.powervm_lpar_instance
  - ibm.power_hmc.powervm_dlpar
  - ibm.power_hmc.powervm_lpar_migration
  - ibm.power_hmc.power_system
  - ibm.power_hmc.firmware_update
  - ibm.power_hmc.vios
  - ibm.power_hmc.powervm_inventory
  - ibm.power_hmc.redhat_linux_install
examples:
  - title: ansible-power-hmc collection
    url: https://github.com/IBM/ansible-power-hmc
---

# Manage IBM Power systems with the HMC

## Description

Operate IBM Power servers through the Hardware Management Console with the same job templates used for other infrastructure. Administrators create and activate partitions, change CPU and memory dynamically, move running partitions between systems, set up virtual networking and Virtual I/O Servers, and maintain HMC and system firmware.

## Prerequisites

1. One or more HMCs reachable from the execution environment, with a service account that has the needed HMC roles, stored in Automation Platform.
2. Managed systems registered in the HMC, with a documented partition, network and storage design.
3. An execution environment with `ibm.power_hmc` and its Python requirements.
4. A boot source for new partitions: a NIM server, an ISO or a PXE server.
5. Firmware and update images for the HMC, systems and VIOS, if updates are in scope.

## Steps

1. Build an inventory from the HMC with the `ibm.power_hmc.powervm_inventory` inventory plugin, and gather facts on managed systems with `ibm.power_hmc.power_system`.
2. Set up shared infrastructure: Virtual I/O Servers with `ibm.power_hmc.vios`, virtual switches and networks with `powervm_virtual_switches`, `powervm_virtual_network` and `power_network_bridge`.
3. Create the partition with `ibm.power_hmc.powervm_lpar_instance`, defining profile settings, then adjust profiles with `powervm_partition_profile` and client network adapters with `powervm_client_network_adapter`.
4. Install the operating system: install AIX through NIM from `ibm.power_aix`, or Red Hat Enterprise Linux with the `ibm.power_hmc.redhat_linux_install` role.
5. Resize running partitions with `ibm.power_hmc.powervm_dlpar` and move them between servers with `ibm.power_hmc.powervm_lpar_migration`, which validates the move before running it.
6. Maintain the platform: apply firmware with `ibm.power_hmc.firmware_update` or `platform_update`, update VIOS from the HMC with `vios_update_upgrade`, and manage HMC users and password policy with `hmc_user` and `hmc_pwdpolicy`.
7. Record serviceable events with `ibm.power_hmc.create_service_event` and report on them as part of operations reviews.
8. Hand the new partition to the operating system configuration jobs.

## Success Criteria

1. A partition request produces an activated, correctly sized partition with its network and storage connections.
2. Inventory from the HMC matches the CMDB for all managed systems.
3. A partition migration is validated and completed without manual HMC work.
4. HMC and system firmware levels are reported and updated within the maintenance process.

## Notes

- Power-specific VIOS tasks outside the HMC, such as backup and update from the VIOS itself, are covered in [Patch and maintain AIX, VIOS and IBM i](patch-and-maintain-aix-vios-and-ibm-i.md).
- `ibm.power_vios` modules such as `viosbr` and `viosecure` can be run directly against a VIOS partition.
- For firmware practices on x86 servers, see [Update server firmware and BIOS](update-server-firmware-and-bios.md).
- Event-Driven Ansible can start a service event report or an extra health check job when a serviceable event is raised.
