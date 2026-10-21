---
title: Provision AWS networking and compute
summary: Create VPCs, subnets, security groups and EC2 instances from code, repeatably and with a clean teardown path.
order: 10
personas: [Cloud engineer, Platform engineer]
collections: [amazon.aws, cloud.aws_ops]
key_content:
  - cloud.aws_ops.ec2_networking_resources
  - cloud.aws_ops.manage_ec2_instance
  - cloud.aws_ops.manage_transit_gateway
  - amazon.aws.ec2_vpc_net
  - amazon.aws.ec2_vpc_subnet
  - amazon.aws.ec2_security_group
  - amazon.aws.ec2_instance
examples:
  - title: cloud.aws_ops validated collection
    url: https://github.com/ansible-collections/cloud.aws_ops
    note: roles and playbooks for common AWS operations
---

# Provision AWS networking and compute

## Description

Build the base of an AWS environment, a VPC with subnets, routing, security groups and EC2 instances, with a playbook instead of console clicks. The same job template creates a development copy or a production copy, and can remove it again when it is no longer needed.

## Notes

- Use the Terraform route instead when the organization already standardizes on Terraform for provisioning, see [Run Terraform from Automation Platform](../multi-cloud/run-terraform-from-automation-platform.md).
- Existing CloudFormation stacks can stay in place and be driven by Ansible, see [Manage CloudFormation stacks](manage-cloudformation-stacks.md).
- For a full application on top of this network, see [Deploy and operate a web application on AWS](deploy-web-application-on-aws.md).
