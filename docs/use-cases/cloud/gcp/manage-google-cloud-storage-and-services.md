---
title: Manage Google Cloud storage and services
summary: Create and configure buckets, Cloud SQL databases, messaging, service accounts, keys and secrets as code.
order: 20
personas: [Cloud engineer, Platform engineer, Cloud security engineer]
collections: [google.cloud, cloud.gcp_ops]
key_content:
  - google.cloud.gcp_storage_bucket
  - google.cloud.gcp_sql_instance
  - google.cloud.gcp_pubsub_topic
  - google.cloud.gcp_iam_service_account
  - google.cloud.gcp_kms_key_ring
  - google.cloud.gcp_secret_manager
  - cloud.gcp_ops.upload_file_to_cloud_storage.upload_file_to_cloud_storage
---

# Manage Google Cloud storage and services

## Description

Define the supporting services of a Google Cloud project in code: storage buckets, managed databases, messaging topics, service accounts, encryption keys and secrets. Teams request services through a job template, and the configuration is the same across projects.

## Prerequisites

1. A Google Cloud credential in Automation Platform with permissions for the services in scope.
2. APIs enabled in the project for each service (Storage, Cloud SQL, Pub/Sub, IAM, KMS, Secret Manager).
3. Standards for bucket location, database tier, retention and key rotation.
4. An execution environment with `google.cloud` and `cloud.gcp_ops`.

## Steps

1. Create service accounts with `google.cloud.gcp_iam_service_account`, granting only the roles each workload needs.
2. Create buckets with `google.cloud.gcp_storage_bucket`, and upload content with `google.cloud.gcp_storage_object` or the `cloud.gcp_ops.upload_file_to_cloud_storage.upload_file_to_cloud_storage` playbook.
3. Create encryption keys with `google.cloud.gcp_kms_key_ring` and `google.cloud.gcp_kms_crypto_key`.
4. Create databases with `google.cloud.gcp_sql_instance`, `google.cloud.gcp_sql_database` and `google.cloud.gcp_sql_user`.
5. Create messaging with `google.cloud.gcp_pubsub_topic` and `google.cloud.gcp_pubsub_subscription`.
6. Store and read secrets with `google.cloud.gcp_secret_manager`, so playbooks and applications do not carry plain-text credentials.
7. Run the playbook on a schedule to confirm that the services still match the definition.

## Success Criteria

1. Buckets, databases, topics, keys and service accounts exist with the defined settings.
2. Secrets are stored in Secret Manager and not in the project or job output.
3. A repeat run reports no changes unless a setting was changed outside automation.
4. Each service has an owner label recorded in its definition.

## Notes

- Do not store service account keys in Git; prefer short-lived credentials or credentials held in Automation Platform.
- The `google.cloud.gcp_secret_manager` lookup can fetch a secret at run time.
- Related: [Provision Google Cloud networking and compute](provision-google-cloud-networking-and-compute.md).
