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

## Prerequisites

1. Read access to each source system, with a service account or API token stored as a platform credential.
2. A decision on which source is authoritative for which attribute, so that two sources do not describe the same host differently.
3. Network paths from the execution nodes to the sources, and to the managed hosts.
4. An organization and an inventory per scope, for example per business unit or per environment.
5. Naming rules for groups and host variables (for example `env_prod`, `role_web`).

## Steps

1. Create the inventories in the right organizations, as code or in the UI, with `ansible.controller.inventory`.
2. Add one inventory source per system with `ansible.controller.inventory_source`, choosing the built-in source type where one exists (cloud, VMware, Satellite) or an inventory plugin file in a project, such as `servicenow.itsm.now`, `netbox.netbox.nb_inventory`, `redhat.satellite.foreman` or `vmware.vmware.vms`.
3. Use the matching cloud plugin for each cloud account: `amazon.aws.aws_ec2` for AWS and `azure.azcollection.azure_rm` for Azure.
4. Build groups and host variables with plugin options such as `keyed_groups`, `compose` and filters, so that the inventory reflects role, environment and owner.
5. Set the sources to update on project update or on a schedule, with overwrite enabled where the source is authoritative.
6. Trigger an immediate refresh from workflows or pipelines with `ansible.controller.inventory_source_update` before a change that depends on current data.
7. Verify counts against the source system, and add an alert when a sync fails or when the host count drops sharply.

## Success Criteria

1. Each inventory shows the same number of hosts as its source system, within the agreed tolerance.
2. A host added or decommissioned in the source appears or disappears in the next sync with no manual edit.
3. Groups and variables are identical across runs, so limits and survey choices behave consistently.
4. Sync failures notify the owning team.
5. Credentials for the sources are stored in the platform, not in the repository.

## Notes

- Define inventories, sources and schedules in Git with [Manage Automation Platform as code](manage-aap-as-code.md).
- Constructed inventories can combine several sources, for example ServiceNow ownership data with Satellite content data.
- Use Event-Driven Ansible with `servicenow.itsm.records` or cloud event sources to refresh inventory when records change instead of waiting for the schedule.
- Large inventories benefit from caching in the plugin, filtered queries at the source and splitting by scope; see [Scale and tune with automation mesh](scale-with-automation-mesh.md).
- Red Hat Insights (`redhat.insights.insights`) can serve as an additional source for RHEL systems that are registered with it but not in Satellite.
