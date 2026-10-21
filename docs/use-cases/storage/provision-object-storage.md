---
title: Provision object storage
summary: Create tenants, users, access keys and buckets with lifecycle rules on S3-compatible storage platforms.
order: 40
personas: [Storage administrator, Cloud platform engineer]
collections: [netapp.storagegrid, netapp.ontap, everpure.flashblade, dellemc.powerscale]
key_content:
  - netapp.storagegrid.na_sg_grid_tenant
  - netapp.storagegrid.na_sg_org_user
  - netapp.storagegrid.na_sg_org_user_s3_key
  - netapp.storagegrid.na_sg_org_bucket
  - netapp.storagegrid.na_sg_grid_ilm_policy
  - netapp.ontap.na_ontap_s3_buckets
  - everpure.flashblade.purefb_s3acc
  - everpure.flashblade.purefb_bucket
---

# Provision object storage

## Description

Give application teams an S3-compatible bucket with access keys and lifecycle rules without a storage ticket. Automation creates the tenant or account, the user, the keys and the bucket, and applies data placement and retention rules, then hands the endpoint and credentials to the requester through a secure channel.

## Notes

- Set `no_log` on tasks that return access keys.
- Object storage is a common target for backups; see [Manage snapshots, clones and replication](manage-snapshots-clones-and-replication.md) and [Back up Kubernetes applications](../kubernetes/back-up-kubernetes-applications.md).
- Pair with [Standardise storage system configuration](standardise-storage-system-configuration.md) for certificates, NTP and identity federation on the platform.
