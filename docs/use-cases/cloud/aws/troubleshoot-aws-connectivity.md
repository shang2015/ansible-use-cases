---
title: Troubleshoot AWS connectivity and resources
summary: Find out why one AWS resource cannot reach another by evaluating routes, security groups and network ACLs automatically.
order: 50
personas: [Cloud engineer, Network engineer, Support engineer]
collections: [cloud.aws_troubleshooting]
key_content:
  - cloud.aws_troubleshooting.connectivity_troubleshooter
  - cloud.aws_troubleshooting.connectivity_troubleshooter_igw
  - cloud.aws_troubleshooting.connectivity_troubleshooter_nat
  - cloud.aws_troubleshooting.connectivity_troubleshooter_peering
  - cloud.aws_troubleshooting.troubleshoot_rds_connectivity
  - cloud.aws_troubleshooting.eval_security_groups
examples:
  - title: cloud.aws_troubleshooting validated collection
    url: https://github.com/redhat-cop/cloud.aws_troubleshooting
    note: roles and modules for connectivity diagnosis
---

# Troubleshoot AWS connectivity and resources

## Description

When a workload in AWS cannot reach a destination, the cause is usually spread across route tables, security groups, network ACLs, gateways or peering. Run a playbook that walks the path between a source and a destination and reports which rule blocks the traffic.

## Prerequisites

1. An AWS credential with read access to EC2, VPC and RDS metadata.
2. The source and destination identifiers, such as instance IDs, ENI IDs or IP addresses, and the port and protocol.
3. An execution environment with `cloud.aws_troubleshooting`.
4. A job template that support staff can launch with a survey.

## Steps

1. Add a survey for source, destination, port and protocol, and map them to the role variables.
2. Run the `cloud.aws_troubleshooting.connectivity_troubleshooter` role as the entry point for a source and destination pair.
3. For a specific path type, use the matching role: `connectivity_troubleshooter_igw`, `connectivity_troubleshooter_nat`, `connectivity_troubleshooter_peering` or `connectivity_troubleshooter_local`.
4. Use the `eval_security_groups`, `eval_network_acls` and `validate_route_tables` modules to inspect an individual layer.
5. For database access problems, run `cloud.aws_troubleshooting.troubleshoot_rds_connectivity`.
6. Attach the output to the incident ticket, and fix the identified rule in a separate, approved change job.

## Success Criteria

1. The report states pass or fail for each layer on the path.
2. A blocked path identifies the specific rule or missing route responsible.
3. Support staff can run the diagnosis from a survey without AWS console access.
4. The diagnosis job makes no changes to AWS resources.

## Notes

- The `cloud.aws_ops` collection also ships `validate_route_tables`, `validate_network_acls` and `validate_security_group_rules` modules for the same kind of checks.
- Pair with Event-Driven Ansible to run the diagnosis automatically when a monitoring alert reports a connection failure.
- To fix what is found, see [Provision AWS networking and compute](provision-aws-networking-and-compute.md).
