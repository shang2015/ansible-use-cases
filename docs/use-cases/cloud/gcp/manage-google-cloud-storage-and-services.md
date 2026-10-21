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

## Notes

- Do not store service account keys in Git; prefer short-lived credentials or credentials held in Automation Platform.
- The `google.cloud.gcp_secret_manager` lookup can fetch a secret at run time.
- Related: [Provision Google Cloud networking and compute](provision-google-cloud-networking-and-compute.md).
