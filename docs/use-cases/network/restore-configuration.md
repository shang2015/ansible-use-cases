---
title: Restore configuration
summary: Roll a device back to a known-good configuration from a previous backup or from the approved state.
order: 30
personas: [Network engineer, NetOps lead]
collections: [network.backup, network.base, ansible.netcommon, cisco.ios, arista.eos, junipernetworks.junos]
key_content:
  - network.backup.restore
  - ansible.netcommon.cli_restore
  - network.base.remediate
  - cisco.ios.ios_config
  - arista.eos.eos_config
  - junipernetworks.junos.junos_config
examples:
  - title: network.backup validated collection
    url: https://github.com/redhat-cop/network.backup
    note: platform-agnostic backup and restore roles
---

# Restore configuration

## Description

Return a router, switch or firewall to a previous good configuration after a failed change, a hardware replacement or detected drift. Restores run from Automation Platform with the same credentials and logging as every other network job.

## Notes

- Restore can drop sessions. Use a workflow with an approval node before the restore job, and run it with limited forks.
- Use `check_mode` first where the module supports it to preview the difference.
- Pair with [Detect configuration drift](detect-configuration-drift.md) to find the devices that need a restore.
