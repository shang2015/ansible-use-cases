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

## Prerequisites

1. An inventory with host groups per server role, built from Satellite, a CMDB or a static file.
2. A Git project holding the SOE variables, kept in `group_vars` per environment and role.
3. The `redhat.rhel_system_roles` collection in the execution environment, from automation hub.
4. Agreement on the baseline: NTP sources, SELinux mode, firewall zones, log destinations and crypto policy.

## Steps

1. Write the baseline as variables: time sources, SELinux state, firewall services and zones, kernel parameters, logging outputs and crypto policy.
2. Create a baseline playbook that calls `redhat.rhel_system_roles.timesync`, `redhat.rhel_system_roles.selinux`, `redhat.rhel_system_roles.firewall`, `redhat.rhel_system_roles.kernel_settings`, `redhat.rhel_system_roles.crypto_policies` and `redhat.rhel_system_roles.logging`.
3. Add registration and Insights connection with `redhat.rhel_system_roles.rhc`, using an activation key so no user password is stored.
4. Add role-specific layers on top of the baseline, for example `redhat.rhel_system_roles.storage`, `redhat.rhel_system_roles.podman` or `redhat.rhel_system_roles.postgresql`, and `ansible.posix.sysctl` for settings the roles do not cover.
5. Test in a non-production group, then run the job template against production with check mode first to preview changes.
6. Schedule the baseline job template (for example daily) so manual changes are reverted and reported as drift.
7. Run the same playbook after provisioning, conversion or upgrade so new and changed hosts converge to the baseline.

## Success Criteria

1. All hosts in a group show identical values for the baseline settings.
2. A manual change to a managed setting is corrected at the next scheduled run, and the job output shows the change.
3. A new host reaches the baseline within one job run after provisioning.
4. The baseline variables are the only place to change a setting, and every change is a reviewed commit.

## Notes

- Other roles in the collection cover `ad_integration`, `aide`, `auditd`, `bootloader`, `certificate`, `cockpit`, `fapolicyd`, `ha_cluster`, `journald`, `kdump`, `metrics`, `network`, `nbde_client`, `nbde_server`, `postfix`, `sudo`, `ssh`, `tlog` and `vpn`. Add them as the baseline grows.
- See [Manage users, sudo and SSH](manage-users-sudo-and-ssh.md) for access settings and [Provision RHEL with Satellite](provision-rhel-with-satellite.md) for the build step that comes before this baseline.
- Benchmark-driven hardening (CIS, DISA STIG) is a separate use case. Keep the SOE and the hardening profile as separate layers so each can change on its own schedule.
- Use Event-Driven Ansible to re-run the baseline for a single host when a monitoring tool reports configuration drift.
