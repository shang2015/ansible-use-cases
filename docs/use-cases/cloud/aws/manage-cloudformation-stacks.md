---
title: Manage CloudFormation stacks with Ansible
summary: Drive existing CloudFormation templates from Automation Platform, or replace them step by step with native Ansible modules.
order: 80
personas: [Cloud engineer, Cloud architect]
collections: [amazon.aws]
key_content:
  - amazon.aws.cloudformation
  - amazon.aws.cloudformation_info
  - amazon.aws.s3_object
  - amazon.aws.ec2_vpc_net
  - amazon.aws.ec2_instance
---

# Manage CloudFormation stacks with Ansible

## Description

Many AWS estates already have CloudFormation templates (CFTs). Ansible can run those stacks as they are, so creation, updates and deletion go through the same job templates, approvals and credentials as the rest of the automation. Where templates become hard to maintain, the same resources can be moved to native `amazon.aws` modules over time.

## Prerequisites

1. Existing CloudFormation templates in Git or S3, and the parameters each one needs.
2. An AWS credential in Automation Platform with permission to create and update the resources in the stacks, including CloudFormation itself.
3. An execution environment containing `amazon.aws`.
4. A decision per stack: keep the template, or replace it with modules.

## Steps

1. Put the templates in a project, with parameter files per environment.
2. Call `amazon.aws.cloudformation` from a playbook to create or update a stack from the template, passing the stack name, parameters and tags.
3. Upload large templates to a bucket first with `amazon.aws.s3_object` and reference them by URL.
4. Read stack outputs with `amazon.aws.cloudformation_info` and pass them to later tasks, such as configuring the instances the stack created.
5. Preview changes with a change set before updating production stacks, and require approval in a workflow before the update runs.
6. For stacks to be retired, recreate the resources with native modules such as `amazon.aws.ec2_vpc_net` and `amazon.aws.ec2_instance`, validate them, then delete the stack.

## Success Criteria

1. Every managed stack is created, updated and deleted by a job template, not by hand.
2. Re-running with unchanged parameters reports no change.
3. Stack outputs are available to follow-on configuration jobs.
4. For each migrated stack, the replacement playbook produces the same resources and the old stack is removed.

## Notes

- Replacing templates with modules gives readable tasks and Ansible variables, and avoids maintaining a second template language; keep CloudFormation where a template is shared with teams that still depend on it.
- Be careful when deleting a stack, as it removes the resources it created. Use termination protection and a manual approval for production.
- Related: [Provision AWS networking and compute](provision-aws-networking-and-compute.md) shows the native-module approach.
