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

## Notes

- Pair with Event-Driven Ansible and the `amazon.aws.aws_sqs_queue` or `amazon.aws.aws_cloudtrail` event source to run a configuration job when a new instance launches.
- Use `compose` options to set `ansible_host` to the private or public address, depending on how the execution environment reaches AWS.
- See [Patch and manage EC2 instances](patch-and-manage-ec2-instances.md) for an example consumer of this inventory.
