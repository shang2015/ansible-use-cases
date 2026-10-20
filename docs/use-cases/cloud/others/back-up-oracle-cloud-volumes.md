---
title: Back up Oracle Cloud block and boot volumes
summary: Apply backup policies to OCI volumes and take on-demand backups before changes.
order: 20
personas: [Cloud engineer, Backup administrator]
collections: [ansible.oci]
key_content:
  - ansible.oci.oci_volume_backup_policy
  - ansible.oci.oci_volume_backup_policy_assignment
  - ansible.oci.oci_volume_backup
  - ansible.oci.oci_boot_volume_backup
  - ansible.oci.oci_volume_group_backup
---

# Back up Oracle Cloud block and boot volumes

## Description

Make sure every OCI block volume, boot volume and volume group has a backup schedule, and take extra backups before maintenance. Policies are defined in code and assigned to volumes automatically, so new volumes are not left unprotected.

## Prerequisites

1. An OCI credential with rights to manage volumes and backups in the target compartments.
2. Backup schedule and retention requirements per workload class.
3. An inventory of the volumes in scope, for example from `ansible.oci.oci_blockstorage_volume_info`.
4. An execution environment containing `ansible.oci`.

## Steps

1. Create custom schedules with `ansible.oci.oci_volume_backup_policy`.
2. Assign the policy to volumes with `ansible.oci.oci_volume_backup_policy_assignment`.
3. List volumes and existing assignments, and report volumes with no policy.
4. Take on-demand backups before changes with `ansible.oci.oci_volume_backup`, `ansible.oci.oci_boot_volume_backup` or `ansible.oci.oci_volume_group_backup`.
5. Schedule the job daily and notify owners of volumes that were missing a policy.
6. Test a restore by creating a volume from a backup with `ansible.oci.oci_blockstorage_volume` in a test compartment.

## Success Criteria

1. Every volume in scope has a policy assigned.
2. Scheduled backups appear in the expected number for the retention period.
3. An on-demand backup exists before each approved change.
4. A restore test produces a usable volume.

## Notes

- Keep restore tests in a separate compartment to avoid conflicts with production names and quotas.
- Related: [Provision Oracle Cloud (OCI) resources](provision-oracle-cloud-resources.md).
