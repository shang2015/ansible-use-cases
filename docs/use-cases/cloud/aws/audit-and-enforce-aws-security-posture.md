---
title: Audit and enforce AWS security posture
summary: Check IAM, network and audit-trail settings against policy, correct drift and restore deleted security controls.
order: 60
personas: [Cloud security engineer, Cloud engineer, Compliance officer]
collections: [amazon.aws, cloud.aws_ops]
key_content:
  - amazon.aws.cloudtrail
  - amazon.aws.kms_key
  - amazon.aws.iam_password_policy
  - amazon.aws.ec2_security_group
  - cloud.aws_ops.aws_restore_cloudtrail
  - cloud.aws_ops.aws_restore_kms_key
  - cloud.aws_ops.validate_security_group_rules
---

# Audit and enforce AWS security posture

## Description

Define the expected state of the account's security controls in code, such as the password policy, audit trails, encryption keys and security group rules, and use automation to report and correct differences. Controls that are disabled or deleted can be restored with a single job.

## Notes

- Pair with Event-Driven Ansible using the `amazon.aws.aws_cloudtrail` event source to react to events such as a trail being stopped or a security group being opened.
- Keep enforcement behind an approval step for production accounts.
- For secrets, `amazon.aws.secretsmanager_secret` and `amazon.aws.ssm_parameter` lookups keep credentials out of playbooks.
- Related: [Troubleshoot AWS connectivity and resources](troubleshoot-aws-connectivity.md).
