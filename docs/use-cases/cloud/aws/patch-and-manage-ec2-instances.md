---
title: Patch and manage EC2 instances
summary: Patch EC2 instances without SSH through Systems Manager, or bake patched AMIs and roll them out.
order: 40
personas: [Cloud engineer, Linux administrator, Operations lead]
collections: [amazon.aws, cloud.aws_ops]
key_content:
  - amazon.aws.aws_ssm
  - amazon.aws.aws_ec2
  - amazon.aws.ec2_instance
  - amazon.aws.ec2_ami
  - cloud.aws_ops.customized_ami
  - amazon.aws.autoscaling_instance_refresh
---

# Patch and manage EC2 instances

## Description

Keep EC2 instances patched and consistently configured. Existing servers are updated in place over AWS Systems Manager, so no inbound SSH is needed, and fleets built from AMIs are updated by baking a new image and replacing instances.

## Notes

- Operating-system patching tasks are covered in more depth under the Linux use cases, for example Red Hat Enterprise Linux with the standard package modules.
- Use `amazon.aws.ec2_instance` with a stopped state before resizing or changing attached volumes.
- Pair with [Back up and restore AWS resources](back-up-and-restore-aws-resources.md) to take snapshots before patching.
