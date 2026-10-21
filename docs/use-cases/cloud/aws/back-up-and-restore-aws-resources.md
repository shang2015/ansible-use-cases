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

## Notes

- Related restore playbooks for audit trails and encryption keys are described in [Audit and enforce AWS security posture](audit-and-enforce-aws-security-posture.md).
- Pair with Event-Driven Ansible to take an on-demand snapshot when a change request is approved.
- Backup tags can be audited with `amazon.aws.backup_tag_info`.
