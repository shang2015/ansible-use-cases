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

## Prerequisites

1. An AWS account and an IAM user or role that can create network and EC2 resources, stored as an Automation Platform credential (Amazon Web Services type).
2. An execution environment that includes `amazon.aws` and `cloud.aws_ops` and the `boto3` and `botocore` libraries.
3. Agreed CIDR ranges, regions, instance sizes, AMI and tagging standards.
4. An EC2 key pair, or Systems Manager access, for later configuration of the instances.

## Steps

1. Define the target design as variables: region, VPC CIDR, subnets, security group rules, instance type and tags.
2. Create the network with the `cloud.aws_ops.ec2_networking_resources` role, or directly with `amazon.aws.ec2_vpc_net`, `amazon.aws.ec2_vpc_subnet` and `amazon.aws.ec2_security_group` when more control is needed.
3. Launch instances with the `cloud.aws_ops.manage_ec2_instance` role or `amazon.aws.ec2_instance`, using the same tags on every resource.
4. Connect multiple VPCs or accounts with the `cloud.aws_ops.manage_transit_gateway` role where a hub-and-spoke layout is required.
5. Add the new instances to the inventory (see [Use AWS as a dynamic inventory source](use-aws-as-dynamic-inventory.md)) and hand over to configuration jobs.
6. Create a job template for the playbook with a survey for environment name and region, and run it from a workflow so approvals can be added.
7. Add a teardown job that removes the resources, using the roles' delete operation or `state: absent` on the modules.

## Success Criteria

1. Running the job twice produces no changes the second time.
2. The VPC, subnets, security groups and instances exist with the expected CIDRs, rules and tags.
3. A teardown run removes every resource the build created.
4. Credentials are held only in Automation Platform and never appear in the job output.

## Notes

- Use the Terraform route instead when the organization already standardizes on Terraform for provisioning, see [Run Terraform from Automation Platform](../multi-cloud/run-terraform-from-automation-platform.md).
- Existing CloudFormation stacks can stay in place and be driven by Ansible, see [Manage CloudFormation stacks](manage-cloudformation-stacks.md).
- For a full application on top of this network, see [Deploy and operate a web application on AWS](deploy-web-application-on-aws.md).
