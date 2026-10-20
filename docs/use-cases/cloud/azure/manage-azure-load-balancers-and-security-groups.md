---
title: Manage Azure load balancers and security groups
summary: Publish workloads behind Azure load balancers and keep network security group rules defined in code.
order: 20
personas: [Cloud engineer, Network engineer, Cloud security engineer]
collections: [cloud.azure_ops, azure.azcollection]
key_content:
  - cloud.azure_ops.azure_load_balancer_with_public_ip
  - cloud.azure_ops.azure_manage_security_group
  - azure.azcollection.azure_rm_loadbalancer
  - azure.azcollection.azure_rm_securitygroup
  - azure.azcollection.azure_rm_publicipaddress
  - azure.azcollection.azure_rm_appgateway
---

# Manage Azure load balancers and security groups

## Description

Expose Azure workloads through a load balancer and control access with network security groups, all from version-controlled definitions. Rule changes are requested through a pull request, applied by a job, and visible in history.

## Prerequisites

1. An Azure credential in Automation Platform with network contributor rights on the resource group.
2. An existing virtual network, subnets and the VMs or scale sets to put behind the load balancer.
3. An approved rule set: allowed sources, ports and priorities.
4. An execution environment with `cloud.azure_ops` and `azure.azcollection`.

## Steps

1. Keep the security group rules as structured variables in Git, one file per environment.
2. Apply rules with the `cloud.azure_ops.azure_manage_security_group` role, or `azure.azcollection.azure_rm_securitygroup`.
3. Create the public IP address and load balancer with the `cloud.azure_ops.azure_load_balancer_with_public_ip` role, or `azure.azcollection.azure_rm_publicipaddress` and `azure.azcollection.azure_rm_loadbalancer`.
4. For layer 7 routing, define an application gateway with `azure.azcollection.azure_rm_appgateway`.
5. Run a test request through the load balancer address as the last task of the job.
6. Run the playbook on a schedule in check mode to report manual changes that differ from Git.

## Success Criteria

1. Requests to the load balancer address reach the backend workloads.
2. Security group rules match the files in Git, and no unlisted inbound rule exists.
3. Rule changes go through a reviewed commit and a logged job run.
4. Drift reports show who or what changed rules outside automation, within the schedule interval.

## Notes

- Combine with [Provision Azure networking and virtual machines](provision-azure-networking-and-virtual-machines.md) for the underlying network.
- Pair with Event-Driven Ansible and the `azure.azcollection.azure_event_hub` event source to react to Azure activity log events.
- Apply a lock with `azure.azcollection.azure_rm_lock` to protect shared network resources from deletion.
