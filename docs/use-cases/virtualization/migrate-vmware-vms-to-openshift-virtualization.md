---
title: Migrate VMs from VMware to OpenShift Virtualization
summary: Plan, run and validate waves of VM migrations from vSphere (or RHV) to OpenShift Virtualization using the Migration Toolkit for Virtualization driven by Automation Platform.
order: 40
personas: [Migration lead, Virtualization architect, Platform engineer]
collections: [infra.openshift_virtualization_migration, vmware.vmware, os_migrate.vmware_migration_kit]
key_content:
  - infra.openshift_virtualization_migration.bootstrap
  - infra.openshift_virtualization_migration.mtv_management
  - infra.openshift_virtualization_migration.vm_collect
  - infra.openshift_virtualization_migration.mtv_migrate
  - infra.openshift_virtualization_migration.validate_migration
  - infra.openshift_virtualization_migration.ocp_cleanup
  - vmware.vmware.vm_info
examples:
  - title: infra.openshift_virtualization_migration validated collection
    url: https://github.com/redhat-cop/openshift_virtualization_migration
    note: Migration Factory content for AAP, MTV management and VM operations
---

# Migrate VMs from VMware to OpenShift Virtualization

## Description

Move virtual machine workloads from VMware vSphere to Red Hat OpenShift Virtualization in controlled waves. Automation Platform drives the Migration Toolkit for Virtualization (MTV): it prepares the target cluster, registers the source provider, maps networks and storage, migrates VMs at scale and validates the result, so migration becomes a repeatable factory process rather than a series of manual console steps.

## Notes

- The same collection also supports RHV (oVirt) as a source through its oVirt provider configuration; check the collection documentation for the supported source and target versions.
- `os_migrate.vmware_migration_kit` is a separate certified kit that migrates VMware VMs to OpenStack (and OpenShift) using a conversion host. Use it when the target is OpenStack, or when MTV is not an option.
- Before moving a VM, snapshot or back it up on the source side. See [Manage VMware snapshots and VM lifecycle](manage-vmware-snapshots-and-vm-lifecycle.md).
- After cut-over, continue with [Operate VMs on OpenShift Virtualization](operate-vms-on-openshift-virtualization.md).
- Event-Driven Ansible is not required, but job template completion events can be sent to a ticketing system to track waves.
