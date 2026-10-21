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

## Notes

- Pair with [Detect configuration drift](detect-configuration-drift.md) and [Restore configuration](restore-configuration.md) to cover the full lifecycle.
- Where SSH is not available, SNMP-based collection is an alternative for basic facts.
