---
title: Migrate on-premises VMs to Google Cloud
summary: Clone a KVM virtual machine, import its image and start it as a Compute Engine instance.
order: 40
personas: [Cloud engineer, Migration lead]
collections: [cloud.gcp_ops, google.cloud]
key_content:
  - cloud.gcp_ops.move_vm_from_on_prem_to_gcp.move_vm_from_on_prem_to_gcp
  - cloud.gcp_ops.clone_on_prem_vm
  - cloud.gcp_ops.import_image_and_run_gcp_instance
  - cloud.gcp_ops.upload_file_to_cloud_storage.upload_file_to_cloud_storage
  - google.cloud.gcp_compute_image
---

# Migrate on-premises VMs to Google Cloud

## Description

Move a virtual machine from an on-premises KVM hypervisor to Google Cloud with a validated playbook. The automation clones the VM, uploads the image to Cloud Storage, imports it as a Compute Engine image and starts an instance from it.

## Notes

- The validated playbook targets KVM sources.
- The same pattern for AWS is in [Migrate on-premises VMs to AWS](../aws/migrate-on-prem-vms-to-aws.md).
- Use `cloud.gcp_ops.manage_machine_image` to maintain reusable machine images after migration.
