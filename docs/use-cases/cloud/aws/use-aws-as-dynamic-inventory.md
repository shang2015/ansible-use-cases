---
title: Use AWS as a dynamic inventory source
summary: Build Automation Platform inventories from live EC2 and RDS resources, grouped by tags, region and account.
order: 70
personas: [Cloud engineer, Automation architect]
collections: [amazon.aws]
key_content:
  - amazon.aws.aws_ec2
  - amazon.aws.aws_rds
  - amazon.aws.sts_assume_role
  - amazon.aws.aws_ssm
---

# Use AWS as a dynamic inventory source

## Description

Let AWS itself be the source of truth for which servers exist. An inventory source syncs EC2 instances, and optionally RDS databases, into Automation Platform, so job templates always target current resources grouped by tag, region or account.

## Prerequisites

1. An AWS credential with read access to EC2 and RDS (and `sts:AssumeRole` for multi-account setups).
2. A tagging standard that identifies application, environment and owner.
3. Network or Systems Manager access from the execution environment to the instances.
4. An execution environment containing `amazon.aws`, `boto3` and `botocore`.

## Steps

1. Create a project containing an inventory source file for `amazon.aws.aws_ec2`, with the regions to scan.
2. Define `keyed_groups` and `filters` to group instances by tag, such as environment and role, and to exclude terminated instances.
3. Add a second source for `amazon.aws.aws_rds` if databases need inventory entries.
4. In Automation Platform create an inventory, add the project as an inventory source with the AWS credential, and set it to update on a schedule.
5. For several accounts, create one source per account, using a separate credential or an assumed role per account (see `amazon.aws.sts_assume_role`).
6. Set the connection variable per group, either SSH or the `amazon.aws.aws_ssm` connection plugin.

## Success Criteria

1. New EC2 instances appear in the inventory after the next sync, in the expected groups.
2. Terminated instances disappear from the inventory.
3. Job templates can target a group such as `env_prod` without a hand-maintained host list.
4. Every account in scope has a working inventory source.

## Notes

- Pair with Event-Driven Ansible and the `amazon.aws.aws_sqs_queue` or `amazon.aws.aws_cloudtrail` event source to run a configuration job when a new instance launches.
- Use `compose` options to set `ansible_host` to the private or public address, depending on how the execution environment reaches AWS.
- See [Patch and manage EC2 instances](patch-and-manage-ec2-instances.md) for an example consumer of this inventory.
