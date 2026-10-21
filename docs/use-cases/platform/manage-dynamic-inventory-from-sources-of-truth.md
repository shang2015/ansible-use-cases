---
title: Manage dynamic inventory from sources of truth
summary: Keep controller inventories current by syncing them from ServiceNow, Satellite, VMware, NetBox and the public clouds.
order: 70
personas: [Platform engineer, Automation lead, CMDB owner]
collections: [ansible.controller, infra.aap_configuration, servicenow.itsm, redhat.insights, redhat.satellite, vmware.vmware, netbox.netbox, amazon.aws, azure.azcollection]
key_content:
  - ansible.controller.inventory_source
  - ansible.controller.inventory_source_update
  - servicenow.itsm.now
  - redhat.satellite.foreman
  - vmware.vmware.vms
  - netbox.netbox.nb_inventory
  - amazon.aws.aws_ec2
  - azure.azcollection.azure_rm
---

# Manage dynamic inventory from sources of truth

## Description

Stop maintaining host lists by hand. Automation Platform reads hosts and their attributes from the systems that already know them (a CMDB, a lifecycle manager, a hypervisor manager, an IPAM or a cloud API), groups them by role, environment or location, and refreshes them on a schedule. Job templates then always run against the current estate.

## Notes

- Define inventories, sources and schedules in Git with [Manage Automation Platform as code](manage-aap-as-code.md).
- Constructed inventories can combine several sources, for example ServiceNow ownership data with Satellite content data.
- Use Event-Driven Ansible with `servicenow.itsm.records` or cloud event sources to refresh inventory when records change instead of waiting for the schedule.
- Large inventories benefit from caching in the plugin, filtered queries at the source and splitting by scope; see [Scale and tune with automation mesh](scale-with-automation-mesh.md).
- Red Hat Insights (`redhat.insights.insights`) can serve as an additional source for RHEL systems that are registered with it but not in Satellite.
