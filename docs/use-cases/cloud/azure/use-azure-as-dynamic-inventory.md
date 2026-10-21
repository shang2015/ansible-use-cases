---
title: Use Azure as a dynamic inventory source
summary: Build inventories from live Azure resources and onboard hybrid servers to Azure Arc.
order: 40
personas: [Cloud engineer, Automation architect]
collections: [azure.azcollection, cloud.azure_ops]
key_content:
  - azure.azcollection.azure_rm
  - azure.azcollection.azure_kql
  - azure.azcollection.azure_arc
  - cloud.azure_ops.archost_deploy
  - cloud.azure_ops.azure_configure_archost
---

# Use Azure as a dynamic inventory source

## Description

Let Azure supply the host list. Virtual machines in one or more subscriptions are synchronized into Automation Platform and grouped by resource group, location or tag, so job templates always target current machines. Servers outside Azure can be registered with Azure Arc to appear in the same view.

## Notes

- Use the `azure.azcollection.azure_service_bus` or `azure_event_hub` event source with Event-Driven Ansible to react when a VM is created.
- Restrict each service principal to the subscriptions it needs.
- See [Back up and manage Azure resources](back-up-and-manage-azure-resources.md) for a job that consumes this inventory.
