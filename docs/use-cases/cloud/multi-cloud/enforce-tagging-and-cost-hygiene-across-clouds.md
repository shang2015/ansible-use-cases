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

## Prerequisites

1. A tagging standard: required keys such as owner, cost center, environment and expiry date.
2. Credentials for each cloud with read access, and write access for the remediation job.
3. A notification channel or ticket queue, and an owner lookup (for example a CMDB).
4. Agreement on which resources may be removed automatically.

## Steps

1. Encode the required keys and allowed values as variables in a Git project.
2. Collect resources per cloud: `amazon.aws.ec2_instance_info` for AWS, and the matching `*_info` modules in `azure.azcollection` for Azure.
3. Compare each resource's tags to the standard, and build a report of missing or invalid tags.
4. Apply tags that can be derived (for example from the resource group or account) with `amazon.aws.ec2_tag` and `azure.azcollection.azure_rm_tags`.
5. For provisioning through HCP Terraform, define reserved tag keys with `hashicorp.terraform.reserved_tag_keys`, so new workspaces must carry them.
6. Notify owners of the remaining items, and after a grace period stop or remove expired resources, for example with the `cloud.aws_ops.ec2_instance_terminate_by_tag` role for AWS instances carrying an expiry tag.
7. Schedule the job weekly, and send a summary to the governance team.

## Success Criteria

1. The report shows the percentage of resources with all required tags per cloud and per team.
2. Resources with derivable tags are tagged automatically.
3. Expired temporary resources are removed only after the grace period and owner notice.
4. The compliance percentage rises between consecutive weekly runs.

## Notes

- Start in report-only mode, and enable removal only for resources with an explicit expiry tag.
- Google Cloud uses labels instead of tags; apply them through the resource modules in `google.cloud`.
- Pair with Event-Driven Ansible to tag new resources when they are created.
- Related: [Provision consistently across clouds](provision-consistently-across-clouds.md).
