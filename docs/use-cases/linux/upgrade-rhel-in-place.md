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

## Prerequisites

1. Hosts at a supported starting release and a supported upgrade path. The collection covers RHEL 7 to 8, 8 to 9 and 9 to 10 with Leapp, and 6 to 7 with the Preupgrade Assistant and Red Hat Upgrade Tool. Check Red Hat support policy for the current paths.
2. Repositories for both the current and the target release, from Red Hat CDN, RHUI, Satellite (an activation key for a content view that has both releases) or custom repositories.
3. Free space in the volume group for snapshots and enough space in `/boot`.
4. A maintenance window per batch, application owners for validation, and SSH access with privilege escalation.

## Steps

1. Run `infra.leapp.analysis` on all hosts. It installs the Leapp packages if needed, creates the pre-upgrade report, and generates a `remediate.yml` playbook and per-host variables for known inhibitors.
2. Review the reports and run `infra.leapp.remediate`, then analyse again until no inhibitors remain. Some inhibitors need manual fixes.
3. Check snapshot space with `infra.lvm_snapshots.snapshot_create` and `snapshot_create_check_only: true`. Free space with `infra.lvm_snapshots.shrink_lv`, or enlarge a small boot partition with `infra.lvm_snapshots.bigboot`.
4. Create the snapshot set with `infra.lvm_snapshots.snapshot_create`, including the boot backup option, and enable autoextend so a snapshot does not fill up.
5. Run `infra.leapp.upgrade`. The host reboots more than once. Set `leapp_upgrade_type` to match the repository source and give the Satellite organization and activation key when Satellite is used.
6. Validate the operating system and the application with automated checks and application owner tests.
7. If the checks pass, remove the snapshots with `infra.lvm_snapshots.snapshot_remove`. If they fail, revert with `infra.lvm_snapshots.snapshot_revert` and reboot to complete the revert.
8. Move the host to the new release's content view and apply the standard configuration.

## Success Criteria

1. Hosts report the target RHEL release, and the Leapp upgrade finished without remaining inhibitors.
2. A failed batch can be reverted to its pre-upgrade state in one job run.
3. Pre-upgrade reports for every host are retained.
4. Snapshots are removed after sign-off, so no host keeps a growing snapshot.

## Notes

- Build the flow as a workflow: analysis, remediation, approval, snapshot, upgrade, validation, then remove or revert as separate nodes with an approval before the destructive branch.
- Do not migrate GRUB to GRUB 2 (`leapp_update_grub_to_grub_2`) in the same run as a snapshot. The snapshot role warns that it invalidates the boot backup and breaks a later revert.
- `redhat.leapp` is the certified build of the same roles and is distributed through automation hub; `infra.leapp` is the validated-content build. `redhat.rhel_system_roles.snapshot` is a supported alternative for creating snapshots.
- The `upgrade` role does not upgrade third-party products or non-RHEL repository content. Clustered storage, databases and agents may need separate automation. A rolling upgrade playbook for HA clusters, `infra.leapp.rolling_upgrade_ha_cluster`, is provided for HA clusters; it upgrades the Pacemaker CIB.
- Related: [Convert CentOS and Oracle Linux to RHEL](convert-centos-and-oracle-linux-to-rhel.md) and [Patch RHEL at scale](patch-rhel-at-scale.md).
