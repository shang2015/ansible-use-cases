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

## Prerequisites

1. SSH access to the KVM hypervisor and the VM to be migrated, stored in Automation Platform.
2. A Google Cloud project, a Cloud Storage bucket and a service account with rights to use them and to create images and instances.
3. A target network and firewall rules, see [Provision Google Cloud networking and compute](provision-google-cloud-networking-and-compute.md).
4. A migration plan with cutover windows and rollback steps.

## Steps

1. Review `cloud.gcp_ops.move_vm_from_on_prem_to_gcp.move_vm_from_on_prem_to_gcp` and copy it into a project.
2. Clone the source VM with the `cloud.gcp_ops.clone_on_prem_vm` role so the original keeps running.
3. Upload the image to the bucket using `cloud.gcp_ops.upload_file_to_cloud_storage.upload_file_to_cloud_storage`.
4. Import the image and start an instance with the `cloud.gcp_ops.import_image_and_run_gcp_instance` role. Use `google.cloud.gcp_compute_image` to inspect or manage the resulting image.
5. Test the application on the new instance and switch traffic at cutover.
6. Decommission the source VM after the agreed hold period.

## Success Criteria

1. The migrated instance boots in Google Cloud and passes the application tests.
2. The original VM is unchanged until cutover is approved.
3. The imported image and instance are recorded against the migration ticket.
4. The rollback path stays available until the hold period ends.

## Notes

- The validated playbook targets KVM sources.
- The same pattern for AWS is in [Migrate on-premises VMs to AWS](../aws/migrate-on-prem-vms-to-aws.md).
- Use `cloud.gcp_ops.manage_machine_image` to maintain reusable machine images after migration.
