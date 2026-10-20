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

## Prerequisites

1. A backup of the target device created by [Back up device configuration](backup-device-configuration.md), or an approved desired state stored as host variables.
2. Credentials with configuration (privileged) access to the device.
3. A change window or approval, and console or out-of-band access in case management connectivity is lost.

## Steps

1. Identify the device and the backup version to restore, for example by Git commit or file date, and pass them as survey variables on the job template.
2. Run the `network.backup.restore` role, which restores a stored backup on supported platforms such as IOS, IOS-XR, NX-OS, EOS and Junos. Where a role is not suitable, `ansible.netcommon.cli_restore` or the platform `*_config` module can load the file.
3. For a partial rollback of only the drifted resources, run `network.base.remediate` so the running configuration is overridden with the approved host variables.
4. Take a fresh backup, then check the device state with [Validate operational state and health checks](validate-operational-state-and-health-checks.md).
5. Record the restore in the change record and notify the owners.

## Success Criteria

1. The restored device configuration matches the chosen backup, confirmed by a drift check with no differences.
2. Management access, routing adjacencies and key interfaces are up after the restore.
3. The job output shows who restored which version, when and why.

## Notes

- Restore can drop sessions. Use a workflow with an approval node before the restore job, and run it with limited forks.
- Use `check_mode` first where the module supports it to preview the difference.
- Pair with [Detect configuration drift](detect-configuration-drift.md) to find the devices that need a restore.
