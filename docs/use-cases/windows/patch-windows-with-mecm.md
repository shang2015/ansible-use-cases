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

## Notes

- Where servers are not under MECM, use [Patch Windows servers](patch-windows-servers.md).
- `microsoft.mecm.wsus_server_config` and its info module manage WSUS settings if that is part of the scope.
- Put the same collections into a workflow: health check, deploy, patch, report. Add an approval before the production rings.
- Software deployment through MECM is covered in [Distribute software to Windows hosts](distribute-software-to-windows-hosts.md).
