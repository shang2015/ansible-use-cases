---
title: Patch and maintain AIX, VIOS and IBM i
summary: Apply security fixes and updates, take backups, and manage users and storage on AIX, Virtual I/O Servers and IBM i with a repeatable, approval-gated process.
order: 50
personas: [Power systems administrator, Security lead, Operations lead]
collections: [ibm.power_aix, ibm.power_vios, ibm.power_ibmi, enfence.powerha_aix]
key_content:
  - ibm.power_aix.flrtvc
  - ibm.power_aix.suma
  - ibm.power_aix.nim
  - ibm.power_aix.alt_disk
  - ibm.power_vios.updateios
  - ibm.power_vios.viosbr
  - ibm.power_ibmi.ibmi_fix
  - ibm.power_ibmi.ibmi_lib_save
examples:
  - title: ansible-power-aix collection
    url: https://github.com/IBM/ansible-power-aix
  - title: ansible-power-vios collection
    url: https://github.com/IBM/ansible-power-vios
---

# Patch and maintain AIX, VIOS and IBM i

## Description

Bring order to patching and routine maintenance on IBM Power operating systems. The process checks installed levels, identifies missing security and HIPER fixes, takes a rollback point, applies the fix, and verifies the result, with the same approvals and reporting as for Linux and Windows servers.

## Notes

- AIX security settings, users and groups, filesystems and NIM operations have dedicated modules in `ibm.power_aix`, so the same collection supports hardening and routine administration.
- For clusters running PowerHA, `enfence.powerha_aix` manages cluster and resource group configuration and can be used in the maintenance workflow.
- Combine with [Manage IBM Power systems with the HMC](manage-ibm-power-systems-with-hmc.md) for partition-level operations, and with [Automate IBM Z (z/OS) operations](automate-ibm-z-zos-operations.md) for a mainframe equivalent.
- Event-Driven Ansible can start a fix-check job when a new security bulletin or a monitoring alert arrives.
