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

## Prerequisites

1. Instances with the SSM agent running and an instance profile that allows Systems Manager access.
2. An AWS credential in Automation Platform, and an S3 bucket for the SSM connection file transfer.
3. An execution environment with `amazon.aws`, `cloud.aws_ops`, and the AWS CLI and Session Manager plugin.
4. Maintenance windows, a test group and an approval path.

## Steps

1. Build the inventory with `amazon.aws.aws_ec2`, grouping instances by tag such as environment and patch group.
2. Set `ansible_connection` to `amazon.aws.aws_ssm` for the groups to be patched, so Ansible reaches the hosts through Systems Manager.
3. Patch the test group first with the operating system package modules, then run health checks.
4. Promote to production groups in batches through a workflow with an approval node.
5. For auto-scaled fleets, build a new image with the `cloud.aws_ops.customized_ami` role or `amazon.aws.ec2_ami`, then roll it out with `amazon.aws.autoscaling_instance_refresh`.
6. Report instances that failed or were unreachable, and retire old AMIs after the rollout.

## Success Criteria

1. Patched instances report the target package versions and pass the health check.
2. No inbound SSH rule is needed for the patching job.
3. Production batches are updated only after the test group passes.
4. The rollout leaves a report of updated, skipped and failed instances.

## Notes

- Operating-system patching tasks are covered in more depth under the Linux use cases, for example Red Hat Enterprise Linux with the standard package modules.
- Use `amazon.aws.ec2_instance` with a stopped state before resizing or changing attached volumes.
- Pair with [Back up and restore AWS resources](back-up-and-restore-aws-resources.md) to take snapshots before patching.
