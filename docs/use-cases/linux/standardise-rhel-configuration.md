---
title: Standardise RHEL configuration
summary: Apply a standard operating environment to every RHEL host with RHEL System Roles and keep it from drifting.
order: 60
personas: [Linux administrator, Platform engineer]
collections: [redhat.rhel_system_roles, ansible.posix]
key_content:
  - redhat.rhel_system_roles.rhc
  - redhat.rhel_system_roles.timesync
  - redhat.rhel_system_roles.selinux
  - redhat.rhel_system_roles.firewall
  - redhat.rhel_system_roles.kernel_settings
  - redhat.rhel_system_roles.crypto_policies
  - redhat.rhel_system_roles.logging
  - ansible.posix.sysctl
---

# Standardise RHEL configuration

## Description

Define the standard operating environment (SOE) once as variables and apply it to every RHEL host. RHEL System Roles give a supported, version-independent interface for time, firewall, SELinux, logging, crypto and kernel settings, so one playbook can target several RHEL releases.

## Notes

- Other roles in the collection cover `ad_integration`, `aide`, `auditd`, `bootloader`, `certificate`, `cockpit`, `fapolicyd`, `ha_cluster`, `journald`, `kdump`, `metrics`, `network`, `nbde_client`, `nbde_server`, `postfix`, `sudo`, `ssh`, `tlog` and `vpn`. Add them as the baseline grows.
- See [Manage users, sudo and SSH](manage-users-sudo-and-ssh.md) for access settings and [Provision RHEL with Satellite](provision-rhel-with-satellite.md) for the build step that comes before this baseline.
- Benchmark-driven hardening (CIS, DISA STIG) is a separate use case. Keep the SOE and the hardening profile as separate layers so each can change on its own schedule.
- Use Event-Driven Ansible to re-run the baseline for a single host when a monitoring tool reports configuration drift.
