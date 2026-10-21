---
title: Enforce tagging and cost hygiene across clouds
summary: Find untagged or expired resources in each cloud, apply required tags and stop or remove what is no longer needed.
order: 30
personas: [FinOps practitioner, Cloud engineer, Cloud governance lead]
collections: [amazon.aws, cloud.aws_ops, azure.azcollection, hashicorp.terraform]
key_content:
  - amazon.aws.ec2_instance_info
  - amazon.aws.ec2_tag
  - cloud.aws_ops.ec2_instance_terminate_by_tag
  - azure.azcollection.azure_rm_tags
  - hashicorp.terraform.reserved_tag_keys
---

# Enforce tagging and cost hygiene across clouds

## Description

Cost reports and ownership depend on consistent tags. Run a recurring job in every cloud that finds resources missing required tags, applies tags or notifies owners, and removes temporary resources once they have expired.

## Notes

- Start in report-only mode, and enable removal only for resources with an explicit expiry tag.
- Google Cloud uses labels instead of tags; apply them through the resource modules in `google.cloud`.
- Pair with Event-Driven Ansible to tag new resources when they are created.
- Related: [Provision consistently across clouds](provision-consistently-across-clouds.md).
