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

## Prerequisites

1. A target OpenShift cluster with OpenShift Virtualization installed, cluster-admin access for the automation account, and the storage classes and networks the migrated VMs will use.
2. Source vCenter credentials with read access to the VMs and datastores in scope, and a VDDK image available to MTV.
3. Automation Platform (or a bootstrap VM) with an execution environment that contains `infra.openshift_virtualization_migration` and its dependencies.
4. A wave plan: which VMs move in which window, target namespaces, network and storage mappings, and owners.
5. Network connectivity between the source ESXi hosts, the migration pods and the target storage.

## Steps

1. Bootstrap the migration environment with the `infra.openshift_virtualization_migration.bootstrap` role, or the Migration Factory playbooks that install and seed Automation Platform with the migration job templates.
2. Check the target with the `cluster_healthcheck` and `operator_management` content, and install or verify the required operators.
3. Register the source and configure MTV with the `infra.openshift_virtualization_migration.mtv_management` role, including the VMware provider and VDDK settings.
4. Collect the source inventory with `infra.openshift_virtualization_migration.vm_collect` and, if needed, `vmware.vmware.vm_info`. Use the result to build the wave plan.
5. Define network and storage mappings and create the migration plan from the wave definition.
6. Run the migration with the `infra.openshift_virtualization_migration.mtv_migrate` role, in batches sized to the available bandwidth.
7. Validate each wave with `infra.openshift_virtualization_migration.validate_migration`: confirm the VMs are running on OpenShift, reachable and carry the expected network and storage configuration.
8. Apply post-migration settings such as MAC addresses, SSH keys and hot-plug resources with the `vm_mac_address`, `vm_ssh` and `vm_hot_plug` roles, then hand over to the operate process.
9. Clean up temporary migration artifacts with `infra.openshift_virtualization_migration.ocp_cleanup` once a wave is signed off.

## Success Criteria

1. The source inventory and the wave plan agree, with every in-scope VM assigned to a wave and a target namespace.
2. Each migrated VM runs on OpenShift Virtualization with the planned CPU, memory, disks and networks.
3. Validation results for each wave are stored and attached to the change record.
4. Temporary migration resources are removed after sign-off and the source VMs are retained or retired according to plan.

## Notes

- The same collection also supports RHV (oVirt) as a source through its oVirt provider configuration; check the collection documentation for the supported source and target versions.
- `os_migrate.vmware_migration_kit` is a separate certified kit that migrates VMware VMs to OpenStack (and OpenShift) using a conversion host. Use it when the target is OpenStack, or when MTV is not an option.
- Before moving a VM, snapshot or back it up on the source side. See [Manage VMware snapshots and VM lifecycle](manage-vmware-snapshots-and-vm-lifecycle.md).
- After cut-over, continue with [Operate VMs on OpenShift Virtualization](operate-vms-on-openshift-virtualization.md).
- Event-Driven Ansible is not required, but job template completion events can be sent to a ticketing system to track waves.
