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

## Notes

- Power-specific VIOS tasks outside the HMC, such as backup and update from the VIOS itself, are covered in [Patch and maintain AIX, VIOS and IBM i](patch-and-maintain-aix-vios-and-ibm-i.md).
- `ibm.power_vios` modules such as `viosbr` and `viosecure` can be run directly against a VIOS partition.
- For firmware practices on x86 servers, see [Update server firmware and BIOS](update-server-firmware-and-bios.md).
- Event-Driven Ansible can start a service event report or an extra health check job when a serviceable event is raised.
