---
title: Back up and restore AWS resources
summary: Define AWS Backup plans, vaults and resource selections as code, take on-demand snapshots and rehearse restores.
order: 30
personas: [Cloud engineer, Backup administrator]
collections: [amazon.aws, cloud.aws_ops]
key_content:
  - cloud.aws_ops.backup_create_plan
  - cloud.aws_ops.backup_select_resources
  - amazon.aws.backup_vault
  - amazon.aws.backup_restore_job_info
  - amazon.aws.ec2_snapshot
  - amazon.aws.rds_instance_snapshot
---

# Back up and restore AWS resources

## Description

Make backup policy a version-controlled part of the AWS environment. Plans, vaults and the resources they cover are created by automation, snapshots can be taken before risky changes, and restores are rehearsed so recovery is a known procedure.

## Prerequisites

1. An AWS credential with AWS Backup, EC2 and RDS permissions, and an IAM role that AWS Backup can use.
2. Retention and schedule requirements per workload class (for example daily for 30 days).
3. A tagging convention that identifies which resources need which plan.
4. A target region and, if required, a second region or account for copies.

## Steps

1. Create a vault with `amazon.aws.backup_vault`, optionally with encryption keys managed through `amazon.aws.kms_key`.
2. Create the plan and schedule with the `cloud.aws_ops.backup_create_plan` role, or `amazon.aws.backup_plan`.
3. Assign resources to the plan with the `cloud.aws_ops.backup_select_resources` role, or `amazon.aws.backup_selection`, selecting by tag.
4. Take on-demand snapshots before changes with `amazon.aws.ec2_snapshot` and `amazon.aws.rds_instance_snapshot`.
5. Report the state of restore jobs with `amazon.aws.backup_restore_job_info` and recent plans with `amazon.aws.backup_plan_info`.
6. Schedule a restore drill that rebuilds a volume from a snapshot with `amazon.aws.ec2_vol` into an isolated subnet, then checks the data.

## Success Criteria

1. Every resource carrying the agreed tag is covered by a backup selection.
2. Recovery points appear in the vault on the expected schedule.
3. A restore drill completes within the agreed recovery time and the restored data is verified.
4. Pre-change snapshots exist for each change window and are cleaned up after retention expires.

## Notes

- Related restore playbooks for audit trails and encryption keys are described in [Audit and enforce AWS security posture](audit-and-enforce-aws-security-posture.md).
- Pair with Event-Driven Ansible to take an on-demand snapshot when a change request is approved.
- Backup tags can be audited with `amazon.aws.backup_tag_info`.
