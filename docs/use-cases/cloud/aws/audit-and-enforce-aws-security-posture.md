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

## Prerequisites

1. An AWS credential with read access for audits and a separate, more privileged credential for remediation.
2. A written baseline, for example required CloudTrail settings, KMS key use and prohibited open ports.
3. A project holding the baseline variables and playbooks under version control.
4. A notification channel or ticket queue for findings.

## Steps

1. Encode the baseline as variables, and keep read-only audit jobs apart from remediation jobs.
2. Audit with the `*_info` modules, such as `amazon.aws.cloudtrail_info`, `amazon.aws.iam_role_info`, `amazon.aws.ec2_security_group_info` and `amazon.aws.s3_bucket_info`, and compare the results to the baseline.
3. Check security group rules with the `cloud.aws_ops.validate_security_group_rules` module.
4. Enforce the account settings with `amazon.aws.iam_password_policy`, `amazon.aws.cloudtrail`, `amazon.aws.kms_key` and `amazon.aws.ec2_security_group`.
5. Restore deleted controls with the `cloud.aws_ops.aws_restore_cloudtrail`, `aws_restore_cloudtrail_encryption` and `aws_restore_kms_key` playbooks.
6. Schedule the audit and send the findings to the ticketing or chat system.

## Success Criteria

1. Each audit run produces a list of deviations from the baseline, or an explicit pass.
2. Remediation jobs bring approved items back to the baseline and record what changed.
3. A deleted trail or a KMS key scheduled for deletion is restored by a single job run.
4. No security group exposes the prohibited ports after the enforcement run.

## Notes

- Pair with Event-Driven Ansible using the `amazon.aws.aws_cloudtrail` event source to react to events such as a trail being stopped or a security group being opened.
- Keep enforcement behind an approval step for production accounts.
- For secrets, `amazon.aws.secretsmanager_secret` and `amazon.aws.ssm_parameter` lookups keep credentials out of playbooks.
- Related: [Troubleshoot AWS connectivity and resources](troubleshoot-aws-connectivity.md).
