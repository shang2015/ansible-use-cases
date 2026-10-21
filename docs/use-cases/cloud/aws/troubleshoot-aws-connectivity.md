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

## Notes

- The `cloud.aws_ops` collection also ships `validate_route_tables`, `validate_network_acls` and `validate_security_group_rules` modules for the same kind of checks.
- Pair with Event-Driven Ansible to run the diagnosis automatically when a monitoring alert reports a connection failure.
- To fix what is found, see [Provision AWS networking and compute](provision-aws-networking-and-compute.md).
