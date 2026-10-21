---
title: Upgrade RHEL in place with snapshot rollback
summary: Analyse, remediate and upgrade RHEL hosts with Leapp, with LVM snapshots for a fast rollback.
order: 100
personas: [Linux administrator, Operations lead, Application owner]
collections: [infra.leapp, redhat.leapp, infra.lvm_snapshots, redhat.rhel_system_roles]
key_content:
  - infra.leapp.analysis
  - infra.leapp.remediate
  - infra.leapp.upgrade
  - infra.lvm_snapshots.snapshot_create
  - infra.lvm_snapshots.snapshot_revert
  - infra.lvm_snapshots.snapshot_remove
  - infra.lvm_snapshots.bigboot
  - infra.lvm_snapshots.shrink_lv
examples:
  - title: infra.leapp validated collection
    url: https://github.com/redhat-cop/infra.leapp
    note: analysis, remediate and upgrade roles and playbooks
  - title: infra.lvm_snapshots validated collection
    url: https://github.com/redhat-cop/infra.lvm_snapshots
    note: snapshot create, revert and remove roles
---

# Upgrade RHEL in place with snapshot rollback

## Description

Move RHEL hosts to the next major release without rebuilding them. Leapp analyses each host, Ansible fixes known blockers, takes an LVM snapshot, runs the upgrade and either removes the snapshot after sign-off or reverts to it if the application fails.

## Notes

- Build the flow as a workflow: analysis, remediation, approval, snapshot, upgrade, validation, then remove or revert as separate nodes with an approval before the destructive branch.
- Do not migrate GRUB to GRUB 2 (`leapp_update_grub_to_grub_2`) in the same run as a snapshot. The snapshot role warns that it invalidates the boot backup and breaks a later revert.
- `redhat.leapp` is the certified build of the same roles and is distributed through automation hub; `infra.leapp` is the validated-content build. `redhat.rhel_system_roles.snapshot` is a supported alternative for creating snapshots.
- The `upgrade` role does not upgrade third-party products or non-RHEL repository content. Clustered storage, databases and agents may need separate automation. A rolling upgrade playbook for HA clusters, `infra.leapp.rolling_upgrade_ha_cluster`, is provided for HA clusters; it upgrades the Pacemaker CIB.
- Related: [Convert CentOS and Oracle Linux to RHEL](convert-centos-and-oracle-linux-to-rhel.md) and [Patch RHEL at scale](patch-rhel-at-scale.md).
