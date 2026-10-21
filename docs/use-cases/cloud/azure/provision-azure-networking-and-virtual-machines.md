---
title: Provision Azure networking and virtual machines
summary: Create resource groups, virtual networks and virtual machines from code, with a matching teardown.
order: 10
personas: [Cloud engineer, Platform engineer]
collections: [azure.azcollection, cloud.azure_ops]
key_content:
  - cloud.azure_ops.azure_manage_resource_group
  - cloud.azure_ops.azure_manage_networking_stack
  - cloud.azure_ops.azure_virtual_machine_with_public_ip
  - azure.azcollection.azure_rm_virtualnetwork
  - azure.azcollection.azure_rm_subnet
  - azure.azcollection.azure_rm_virtualmachine
examples:
  - title: cloud.azure_ops validated collection
    url: https://github.com/redhat-cop/cloud.azure_ops
    note: roles and playbooks for Azure operations
---

# Provision Azure networking and virtual machines

## Description

Create the base of an Azure environment, a resource group, virtual network, subnets and virtual machines, with a playbook. Environments are built the same way each time, and the same automation can remove them when a project ends.

## Notes

- Add load balancing and network rules with [Manage Azure load balancers and security groups](manage-azure-load-balancers-and-security-groups.md).
- The `azure_rm_deployment` module in `azure.azcollection` can run existing ARM templates when a template is already the standard.
- If Terraform is the standard provisioner, see [Run Terraform from Automation Platform](../multi-cloud/run-terraform-from-automation-platform.md).
