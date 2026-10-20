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

## Prerequisites

1. A service principal with Reader rights on each subscription, as an Azure credential in Automation Platform.
2. A tagging convention for environment, application and owner.
3. Network access from the execution environment to the VMs, or an Arc SSH route.
4. An execution environment containing `azure.azcollection`.

## Steps

1. Create a project with an `azure.azcollection.azure_rm` inventory source file, listing subscriptions and filters.
2. Define `keyed_groups` for tags, resource group and location, and `conditional_groups` for operating system.
3. For large estates, or filters that need a query, use the `azure.azcollection.azure_kql` inventory plugin (Azure Resource Graph).
4. Create the inventory in Automation Platform, attach the project as a source and schedule updates.
5. To bring on-premises or other-cloud servers under Azure management, run the `cloud.azure_ops.archost_deploy` playbook, or use the `cloud.azure_ops.azure_configure_archost` or `azure.azcollection.azure_arc` role in a custom playbook.
6. Add `cloud.azure_ops.archost_proxy` when machines are reached through the Arc SSH proxy.

## Success Criteria

1. New Azure VMs appear in the inventory after the next sync, in the correct groups.
2. Deleted VMs disappear from the inventory.
3. Job templates target tag-based groups without a manual host list.
4. Arc-enabled servers show as connected in Azure and can be reached by jobs.

## Notes

- Use the `azure.azcollection.azure_service_bus` or `azure_event_hub` event source with Event-Driven Ansible to react when a VM is created.
- Restrict each service principal to the subscriptions it needs.
- See [Back up and manage Azure resources](back-up-and-manage-azure-resources.md) for a job that consumes this inventory.
