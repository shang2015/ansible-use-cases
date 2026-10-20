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

## Prerequisites

1. WinRM (or SSH) connectivity from the execution environment to the servers, with an account that can install updates, stored as an automation controller credential.
2. Update source reachable from the servers: Microsoft Update, Windows Update or a WSUS server that is already configured through Group Policy.
3. Inventory groups for the patch rings, and agreed maintenance windows for each.
4. Backups or VM checkpoints for systems that cannot tolerate a failed update.

## Steps

1. Run a search-only pass with the `infra.windows_ops.windows_manage_updates` role (`windows_manage_updates_state: searched`) to list pending updates per host without changing anything.
2. Check readiness before each ring: free space with `ansible.windows.win_disk_info`, pending reboot with `ansible.windows.win_reboot_info`. Reclaim space with `infra.windows_ops.windows_manage_disk_cleanup` if needed.
3. Install updates with `windows_manage_updates` in the `installed` state. Choose categories (for example critical and security), accept and reject lists by KB number, retry count and reboot timeout. The lower-level `ansible.windows.win_updates` module offers the same controls, including `server_selection`.
4. Reboot where required with the role's reboot option, or with `ansible.windows.win_reboot` when the play controls it.
5. Process rings in order: use `serial` to limit hosts at once, and add an approval node between the test ring and the production rings in a workflow.
6. Verify afterwards: run the search again to confirm nothing is pending, then check critical services with `ansible.windows.win_service_info`.
7. Schedule the workflow for each maintenance window and send the job result to the change record.

## Success Criteria

1. A report shows pending updates before the window and none that are in scope afterwards.
2. Hosts have rebooted when required and are back in service within the window.
3. Failed hosts are listed with the update that failed, and do not stop the rest of the ring.
4. Production rings only receive updates after the test ring has completed without errors.

## Notes

- Where MECM controls update deployment, use [Patch Windows with MECM](patch-windows-with-mecm.md) instead of installing updates directly on the servers.
- The role can compile .NET native images after updates that change the host (`windows_manage_updates_compile_assemblies`), which avoids a slow first start of .NET applications.
- Put monitored servers in maintenance mode while patching with [Respond to Windows alerts from SCOM](respond-to-windows-alerts-from-scom.md).
- Use `ansible.windows.win_hotfix` for a single standalone hotfix package that is not delivered through Windows Update.
