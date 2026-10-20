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

## Prerequisites

1. Administrative access to the object platform (StorageGRID Grid Manager, ONTAP S3 service, FlashBlade or PowerScale), stored as an Automation Platform credential.
2. An S3 endpoint with a valid certificate and DNS name, and load balancing already configured on the platform.
3. A tenant, bucket naming and quota standard, plus a data protection policy (versioning, replication, retention).
4. A secrets store or credential delivery method for access keys.

## Steps

1. Create the tenant or account:
   - StorageGRID `netapp.storagegrid.na_sg_grid_tenant`;
   - FlashBlade `everpure.flashblade.purefb_s3acc`;
   - ONTAP `na_ontap_s3_services` for the S3 server on an SVM.
2. Create users, groups and keys: StorageGRID `na_sg_org_user`, `na_sg_org_group` and `na_sg_org_user_s3_key`; ONTAP `na_ontap_s3_users`, `na_ontap_s3_groups` and `na_ontap_s3_policies`; FlashBlade `purefb_s3user`; PowerScale `dellemc.powerscale.s3_key`.
3. Create the bucket: `netapp.storagegrid.na_sg_org_bucket`, `netapp.ontap.na_ontap_s3_buckets`, `everpure.flashblade.purefb_bucket` or `dellemc.powerscale.s3_bucket`.
4. Apply data management rules, such as StorageGRID ILM policies (`na_sg_grid_ilm_rule`, `na_sg_grid_ilm_policy`), FlashBlade `purefb_lifecycle` and bucket replication with `purefb_bucket_replica` or `na_sg_org_cloud_mirror_replication`.
5. Test the endpoint with an S3 client: write, read and delete an object using the new key.
6. Store the access key in the secrets store and notify the requester with the endpoint and bucket name.
7. Report tenant and bucket usage with the info modules `na_sg_grid_info`, `na_sg_org_info` and `purefb_info`.

## Success Criteria

1. The tenant, user, key and bucket exist with the requested names and quotas.
2. An S3 test using the issued key succeeds and a key from another tenant is rejected.
3. Lifecycle, retention and replication rules match the standard.
4. Access keys are delivered through the secrets store and not stored in job output.

## Notes

- Set `no_log` on tasks that return access keys.
- Object storage is a common target for backups; see [Manage snapshots, clones and replication](manage-snapshots-clones-and-replication.md) and [Back up Kubernetes applications](../kubernetes/back-up-kubernetes-applications.md).
- Pair with [Standardise storage system configuration](standardise-storage-system-configuration.md) for certificates, NTP and identity federation on the platform.
