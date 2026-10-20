---
title: Operate VMs on OpenShift Virtualization
summary: Create, inventory, patch, back up and restore virtual machines running on OpenShift Virtualization using the same Ansible workflows as other platforms.
order: 50
personas: [Virtualization administrator, Platform engineer]
collections: [redhat.openshift_virtualization, infra.openshift_virtualization_migration, infra.openshift_virtualization_ops, kubernetes.core]
key_content:
  - redhat.openshift_virtualization.kubevirt_vm
  - redhat.openshift_virtualization.kubevirt_vm_info
  - redhat.openshift_virtualization.kubevirt
  - infra.openshift_virtualization_migration.vm_lifecycle
  - infra.openshift_virtualization_migration.vm_patching
  - infra.openshift_virtualization_migration.vm_backup_restore
  - infra.openshift_virtualization_migration.vm_networking
examples:
  - title: kubevirt.core (redhat.openshift_virtualization)
    url: https://github.com/kubevirt/kubevirt.core
---

# Operate VMs on OpenShift Virtualization

## Description

Run day-2 operations for VMs hosted on OpenShift Virtualization: define VMs as code, discover them as inventory, patch the guests, take backups and restore them. Teams that came from VMware or RHV keep the same workflows, and use the OpenShift API underneath.

## Prerequisites

1. An OpenShift cluster with OpenShift Virtualization, and a service account or token with permission to manage `VirtualMachine` resources in the target namespaces.
2. An execution environment containing `redhat.openshift_virtualization`, `kubernetes.core` and `infra.openshift_virtualization_migration`.
3. Credentials (SSH keys or Windows credentials) for configuring the guests after they start.
4. For backup and restore, a backup operator or storage that supports VM snapshots in the cluster.

## Steps

1. Define the VM as code and create it with `redhat.openshift_virtualization.kubevirt_vm`, setting running state, instance type, disks and networks. The `infra.openshift_virtualization_migration.vm_lifecycle` role covers start, stop, restart and related actions.
2. Discover running VMs with the `redhat.openshift_virtualization.kubevirt` inventory plugin, and report on them with `redhat.openshift_virtualization.kubevirt_vm_info` and `redhat.openshift_virtualization.kubevirt_vmi_info`.
3. Configure the guest operating systems by running the normal RHEL or Windows configuration job templates against the discovered inventory.
4. Patch the guests with the `infra.openshift_virtualization_migration.vm_patching` role, which handles patching activities for VMs.
5. Adjust resources and networks as needs change using `vm_hot_plug` and `vm_networking`, and manage access with `vm_ssh`.
6. Back up and restore VMs with `infra.openshift_virtualization_migration.vm_backup_restore`, and schedule it for production namespaces.
7. Report on the state of VMs, backups and patch levels on a schedule.

## Success Criteria

1. VMs defined in Git are created on the cluster and match their definitions on re-run.
2. The Automation Platform inventory shows all running VMs in the managed namespaces.
3. Guest patching completes by schedule and exceptions are reported.
4. A VM can be restored from backup using a documented job template.

## Notes

- `kubernetes.core.k8s` and `kubernetes.core.k8s_info` can manage any related object such as namespaces, network attachments and storage claims.
- `infra.openshift_virtualization_ops` is the validated collection dedicated to VM maintenance on OpenShift Virtualization; check its current content before relying on it.
- For migrations into the platform, see [Migrate VMs from VMware to OpenShift Virtualization](migrate-vmware-vms-to-openshift-virtualization.md).
- For application backup of the OpenShift cluster itself, see [Back up Kubernetes applications](../kubernetes/back-up-kubernetes-applications.md).
- Event-Driven Ansible can react to Kubernetes events from the cluster to start remediation jobs when a VM stops unexpectedly.
