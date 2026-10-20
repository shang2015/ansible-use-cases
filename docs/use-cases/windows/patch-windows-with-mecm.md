---
title: Patch Windows with MECM
summary: Drive Microsoft Endpoint Configuration Manager patch deployments, emergency patches and health reports from Ansible.
order: 20
personas: [Windows administrator, Endpoint management engineer]
collections: [infra.mecm_ops, microsoft.mecm]
key_content:
  - infra.mecm_ops.patch_and_reboot
  - infra.mecm_ops.emergency_patch
  - infra.mecm_ops.health_check_report
  - microsoft.mecm.software_update_group
  - microsoft.mecm.software_update_deployment
  - microsoft.mecm.maintenance_windows
  - microsoft.mecm.install_updates
  - microsoft.mecm.software_update_adr
examples:
  - title: infra.mecm_ops validated collection
    url: https://github.com/redhat-cop/infra.mecm_ops
    note: patch and reboot, emergency patch and health check roles
---

# Patch Windows with MECM

## Description

Keep Microsoft Endpoint Configuration Manager (MECM, also known as SCCM or ConfigMgr) as the patch authority and use Ansible to orchestrate it. Automation checks the health of the MECM environment, creates and deploys update groups, runs patch-and-reboot cycles on target collections and handles out-of-band emergency patches with a report at the end.

## Prerequisites

1. An MECM site with software update point, WSUS synchronisation and distribution points working.
2. WinRM access to a host with the MECM console or PowerShell module (usually the site server), with an account that has the needed MECM roles.
3. The site code, and device collections that represent patch rings.
4. PowerShell 5.1 or later on the managed nodes.
5. For e-mailed reports, the `community.general` collection and an SMTP server.

## Steps

1. Check the environment before patch day with the `infra.mecm_ops.health_check_report` role, and query sync and distribution state with `microsoft.mecm.wsus_sync_status_info` and `microsoft.mecm.dp_status_info`.
2. Prepare the deployment: either define an automatic deployment rule with `microsoft.mecm.software_update_adr`, or build a software update group with `microsoft.mecm.software_update_group` and deploy it to a device collection with `microsoft.mecm.software_update_deployment`.
3. Set the patch windows on collections with `microsoft.mecm.maintenance_windows`.
4. Run `infra.mecm_ops.patch_and_reboot` for each ring. It installs the selected update categories (critical, security and update rollups by default) or specific KB numbers, reboots as needed and writes an HTML maintenance report. The `microsoft.mecm.install_updates` module installs deployed updates on clients and can be used directly for custom flows.
5. For a zero-day fix, run `infra.mecm_ops.emergency_patch` with the site code, target collection and article IDs. It creates a temporary update group and deployment. Run it again with `emergency_patch_state: absent` to remove them.
6. Trigger client policy evaluation with `microsoft.mecm.client_action` when clients are slow to pick up a deployment.
7. Collect reports from each run and attach them to the change record.

## Success Criteria

1. The health check passes before the window starts, and any failing component is reported.
2. Every device in the ring shows the update as installed after the run, with the reboot completed.
3. The maintenance report lists success and failure per host.
4. Emergency patch resources exist only as long as needed and are removed afterwards.

## Notes

- Where servers are not under MECM, use [Patch Windows servers](patch-windows-servers.md).
- `microsoft.mecm.wsus_server_config` and its info module manage WSUS settings if that is part of the scope.
- Put the same collections into a workflow: health check, deploy, patch, report. Add an approval before the production rings.
- Software deployment through MECM is covered in [Distribute software to Windows hosts](distribute-software-to-windows-hosts.md).
