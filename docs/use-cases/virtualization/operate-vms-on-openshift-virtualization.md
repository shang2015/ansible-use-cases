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

## Notes

- `kubernetes.core.k8s` and `kubernetes.core.k8s_info` can manage any related object such as namespaces, network attachments and storage claims.
- `infra.openshift_virtualization_ops` is the validated collection dedicated to VM maintenance on OpenShift Virtualization; check its current content before relying on it.
- For migrations into the platform, see [Migrate VMs from VMware to OpenShift Virtualization](migrate-vmware-vms-to-openshift-virtualization.md).
- For application backup of the OpenShift cluster itself, see [Back up Kubernetes applications](../kubernetes/back-up-kubernetes-applications.md).
- Event-Driven Ansible can react to Kubernetes events from the cluster to start remediation jobs when a VM stops unexpectedly.
