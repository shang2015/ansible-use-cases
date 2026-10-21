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

## Notes

- Combine with [Provision Azure networking and virtual machines](provision-azure-networking-and-virtual-machines.md) for the underlying network.
- Pair with Event-Driven Ansible and the `azure.azcollection.azure_event_hub` event source to react to Azure activity log events.
- Apply a lock with `azure.azcollection.azure_rm_lock` to protect shared network resources from deletion.
