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

## Notes

- Replacing templates with modules gives readable tasks and Ansible variables, and avoids maintaining a second template language; keep CloudFormation where a template is shared with teams that still depend on it.
- Be careful when deleting a stack, as it removes the resources it created. Use termination protection and a manual approval for production.
- Related: [Provision AWS networking and compute](provision-aws-networking-and-compute.md) shows the native-module approach.
