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

## Prerequisites

1. AIX partitions, Virtual I/O Servers and IBM i systems reachable from the execution environment, with the credentials stored in Automation Platform.
2. For AIX, a NIM master if updates are applied through NIM, and outbound access (or a local fix repository) for downloading fixes from IBM Fix Central.
3. For IBM i, a fix repository or direct download access and a window for IPLs.
4. A patching policy: frequency, which fixes are mandatory, test and production groups, and rollback rules.
5. A backup or alternate disk target for the rollback point.

## Steps

1. Collect inventory and levels: `ibm.power_aix.lpp_facts`, `lpar_facts` and `lvm_facts` for AIX; `ibm.power_ibmi.ibmi_facts` and `ibmi_fix_check` for IBM i; `ibm.power_vios.mapping_facts` for VIOS.
2. Report missing fixes: `ibm.power_aix.flrtvc` produces the FLRTVC report and can install security and HIPER fixes; on IBM i, compare against the PTF group information.
3. Download the fixes: `ibm.power_aix.suma` (or `nim_suma` for NIM) for AIX service packs and technology levels, `ibm.power_vios.fix_download` for VIOS, and `ibm.power_ibmi.ibmi_download_fix` for IBM i.
4. Create a rollback point before changing the system: `ibm.power_aix.alt_disk` for an alternate rootvg, `ibm.power_aix.backup` for volume group backups, `ibm.power_vios.viosbr` and `backupios` for VIOS, and `ibm.power_ibmi.ibmi_lib_save` or `ibmi_object_save` for IBM i data.
5. Apply the updates:
   - AIX: `ibm.power_aix.install_all_updates`, `emgr` for interim fixes, or `nim` for NIM-driven updates;
   - VIOS: `ibm.power_vios.updateios`, or `nim_updateios` with `nim_vios_hc` to check a pair of VIOSes first;
   - IBM i: `ibm.power_ibmi.ibmi_fix`, or the `apply_ptf` and `sync_apply_ptf_group` roles.
6. Reboot or IPL in the planned sequence. Update the VIOS pair one at a time so client partitions keep their paths, using `ibm.power_aix.reboot` or `ibm.power_ibmi.ibmi_reboot` for the clients.
7. Verify with a post-check job: levels, error report (`ibm.power_aix.errpt`), paths and application checks. Roll back by booting from the alternate disk if a check fails.
8. Report the patch level per system and update the CMDB.

## Success Criteria

1. A report lists patch levels and missing critical fixes for every Power partition.
2. Each patched system has a documented rollback point created before the change.
3. VIOS pairs are updated one at a time and client I/O stays available.
4. Post-patch checks pass and the results are attached to the change record.

## Notes

- AIX security settings, users and groups, filesystems and NIM operations have dedicated modules in `ibm.power_aix`, so the same collection supports hardening and routine administration.
- For clusters running PowerHA, `enfence.powerha_aix` manages cluster and resource group configuration and can be used in the maintenance workflow.
- Combine with [Manage IBM Power systems with the HMC](manage-ibm-power-systems-with-hmc.md) for partition-level operations, and with [Automate IBM Z (z/OS) operations](automate-ibm-z-zos-operations.md) for a mainframe equivalent.
- Event-Driven Ansible can start a fix-check job when a new security bulletin or a monitoring alert arrives.
