---
title: Migrate on-premises VMs to AWS
summary: Convert a KVM virtual machine to an image, import it as an AMI and start it as an EC2 instance.
order: 90
personas: [Cloud engineer, Migration lead]
collections: [cloud.aws_ops, amazon.aws]
key_content:
  - cloud.aws_ops.move_vm_from_on_prem_to_aws.move_vm_from_on_prem_to_aws
  - cloud.aws_ops.clone_on_prem_vm
  - cloud.aws_ops.import_image_and_run_aws_instance
  - cloud.aws_ops.upload_file_to_s3
  - amazon.aws.ec2_import_image
---

# Migrate on-premises VMs to AWS

## Description

Move a virtual machine from an on-premises KVM hypervisor to AWS. The automation clones the VM, uploads the disk image to S3, imports it as an Amazon Machine Image and launches an EC2 instance from it.

## Notes

- The validated playbook targets KVM sources; other hypervisors need a different conversion step before the import.
- The same pattern exists for Google Cloud, see [Migrate on-premises VMs to Google Cloud](../gcp/migrate-on-prem-vms-to-google-cloud.md).
- Large images take time to upload; run the job on an execution node with good bandwidth to AWS.
