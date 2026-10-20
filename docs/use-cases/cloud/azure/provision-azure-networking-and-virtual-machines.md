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

## Prerequisites

1. An Azure subscription and a service principal with Contributor rights on the target scope, stored as a Microsoft Azure Resource Manager credential in Automation Platform.
2. An execution environment containing `azure.azcollection` and `cloud.azure_ops`.
3. Naming, region, address space, VM size and image standards.
4. An SSH key or administrator credential for the new VMs.

## Steps

1. Define the design as variables: subscription, region, resource group, address space, subnets, VM size and tags.
2. Create the resource group with the `cloud.azure_ops.azure_manage_resource_group` role.
3. Create the virtual network, subnets and related resources with the `cloud.azure_ops.azure_manage_networking_stack` role, or `azure.azcollection.azure_rm_virtualnetwork` and `azure.azcollection.azure_rm_subnet`.
4. Create virtual machines with the `cloud.azure_ops.azure_virtual_machine_with_public_ip` role or `azure.azcollection.azure_rm_virtualmachine`, adding network interfaces with `cloud.azure_ops.azure_manage_network_interface` where needed.
5. Publish the playbook as a job template with a survey for environment and size, and place it in a workflow with an approval step.
6. Add the VMs to the inventory (see [Use Azure as a dynamic inventory source](use-azure-as-dynamic-inventory.md)) and run configuration jobs.
7. Add a teardown job that deletes the resource group contents when the environment expires.

## Success Criteria

1. Resource group, network and VMs exist with the requested addresses, sizes and tags.
2. Re-running the job reports no changes.
3. A teardown run leaves no billable resources in the resource group.
4. Service principal secrets are held only in Automation Platform credentials.

## Notes

- Add load balancing and network rules with [Manage Azure load balancers and security groups](manage-azure-load-balancers-and-security-groups.md).
- The `azure_rm_deployment` module in `azure.azcollection` can run existing ARM templates when a template is already the standard.
- If Terraform is the standard provisioner, see [Run Terraform from Automation Platform](../multi-cloud/run-terraform-from-automation-platform.md).
