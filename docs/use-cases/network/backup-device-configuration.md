---
title: Back up device configuration
summary: Capture running configs from every network device on a schedule and store them in Git or object storage.
order: 10
personas: [Network engineer, NetOps lead]
collections: [network.backup, ansible.netcommon, cisco.ios, arista.eos, junipernetworks.junos]
key_content:
  - network.backup.backup
  - ansible.netcommon.cli_backup
  - cisco.ios.ios_config
  - arista.eos.eos_config
  - junipernetworks.junos.junos_config
examples:
  - title: network.backup validated collection
    url: https://github.com/redhat-cop/network.backup
    note: platform-agnostic backup and restore roles
---

# Back up device configuration

## Description

Use Ansible to collect the running configuration of every router, switch and firewall and store it as a versioned file, in a Git repository or an S3-compatible bucket. Backups run on a schedule from Automation Platform, so there is always a known-good copy to compare against or restore from.

## Prerequisites

1. Read access to the devices (SSH/NETCONF/API credentials stored as Automation Platform credentials).
2. Write access to the backup destination (Git repository, S3 bucket or file share).
3. An inventory that groups devices by platform (`ansible_network_os`).

## Steps

1. Build the inventory, statically or from a source of truth such as NetBox, ServiceNow or Infoblox.
2. Add a project containing a playbook that calls the `network.backup.backup` role, or the platform `*_config` module with `backup: true`.
3. Create a job template with the device and destination credentials attached.
4. Schedule the job template, for example nightly or before every change window.
5. Optional: chain it in a workflow before any configuration change job.

## Success Criteria

1. A configuration file exists for every device in the inventory, named by host and date.
2. Each run commits only the files that changed, so Git history shows who changed what and when.
3. Failed devices are reported in the job output and in a notification.

## Notes

- Pair with [Detect configuration drift](detect-configuration-drift.md) and [Restore configuration](restore-configuration.md) to cover the full lifecycle.
- Where SSH is not available, SNMP-based collection is an alternative for basic facts.
