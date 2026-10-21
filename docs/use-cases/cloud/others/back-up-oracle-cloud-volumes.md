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

## Notes

- Keep restore tests in a separate compartment to avoid conflicts with production names and quotas.
- Related: [Provision Oracle Cloud (OCI) resources](provision-oracle-cloud-resources.md).
