---
title: Patch Windows servers
summary: Search, install and verify Windows updates in rings with reboots and retries, using Windows Update or WSUS.
order: 10
personas: [Windows administrator, Operations lead]
collections: [ansible.windows, infra.windows_ops]
key_content:
  - infra.windows_ops.windows_manage_updates
  - ansible.windows.win_updates
  - ansible.windows.win_reboot
  - ansible.windows.win_reboot_info
  - ansible.windows.win_disk_info
  - infra.windows_ops.windows_manage_disk_cleanup
  - ansible.windows.win_service_info
examples:
  - title: infra.windows_ops validated collection
    url: https://github.com/redhat-cop/infra.windows_ops
    note: roles and playbooks for Windows Server operations
---

# Patch Windows servers

## Description

Apply Windows updates to servers on a schedule, in order, with the reboots and retries that Windows Update needs. Servers are grouped into rings (test, then production tiers) so a bad update is caught before it reaches critical systems.

## Notes

- Where MECM controls update deployment, use [Patch Windows with MECM](patch-windows-with-mecm.md) instead of installing updates directly on the servers.
- The role can compile .NET native images after updates that change the host (`windows_manage_updates_compile_assemblies`), which avoids a slow first start of .NET applications.
- Put monitored servers in maintenance mode while patching with [Respond to Windows alerts from SCOM](respond-to-windows-alerts-from-scom.md).
- Use `ansible.windows.win_hotfix` for a single standalone hotfix package that is not delivered through Windows Update.
