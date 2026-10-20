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

## Prerequisites

1. SSH access to the KVM hypervisor and to the VM to be migrated, with credentials in Automation Platform.
2. An S3 bucket and an IAM service role that allows VM import, and an AWS credential with rights to use them.
3. A target VPC, subnet and security group, see [Provision AWS networking and compute](provision-aws-networking-and-compute.md).
4. A migration plan listing the VMs, owners, cutover windows and rollback steps.

## Steps

1. Review the `cloud.aws_ops.move_vm_from_on_prem_to_aws.move_vm_from_on_prem_to_aws` playbook, which chains the roles below, and copy it into a project.
2. Clone the source VM with the `cloud.aws_ops.clone_on_prem_vm` role, so the original keeps running.
3. Upload the image to the bucket with `cloud.aws_ops.upload_file_to_s3`, or `amazon.aws.s3_object`.
4. Import the image and start an instance with the `cloud.aws_ops.import_image_and_run_aws_instance` role, which uses `amazon.aws.ec2_import_image`.
5. Run application checks on the new instance, then switch DNS or load balancer targets at cutover.
6. Record the result for each VM and decommission the source after the agreed hold period.

## Success Criteria

1. The migrated instance boots in AWS and passes the application's smoke tests.
2. The source VM is unchanged until cutover is approved.
3. The import task and its AMI are recorded against the migration ticket.
4. A rollback path (the original VM) exists until the hold period ends.

## Notes

- The validated playbook targets KVM sources; other hypervisors need a different conversion step before the import.
- The same pattern exists for Google Cloud, see [Migrate on-premises VMs to Google Cloud](../gcp/migrate-on-prem-vms-to-google-cloud.md).
- Large images take time to upload; run the job on an execution node with good bandwidth to AWS.
