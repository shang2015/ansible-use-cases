---
title: Back up Kubernetes applications
summary: Orchestrate application-aware backup, recovery and migration of Kubernetes workloads and their data with Trilio and Ansible.
order: 40
personas: [Platform engineer, Backup administrator]
collections: [trilio.trilio_kubernetes, kubernetes.core, infra.automation_development_office]
key_content:
  - trilio.trilio_kubernetes.trilio_kubernetes
  - kubernetes.core.k8s
  - kubernetes.core.k8s_info
  - infra.automation_development_office.ocp_oadp
---

# Back up Kubernetes applications

## Description

Protect Kubernetes and OpenShift applications with application-consistent backups of their objects and persistent data. Automation Platform schedules the backups, verifies them, runs test restores and can move an application to another cluster, replacing ad-hoc scripts with a tested recovery process.

## Notes

- Backup of VMs on OpenShift Virtualization is covered in [Operate VMs on OpenShift Virtualization](../virtualization/operate-vms-on-openshift-virtualization.md).
- Storage-level snapshots and replication can complement application backups; see [Manage snapshots, clones and replication](../storage/manage-snapshots-clones-and-replication.md).
- Back up the cluster configuration, such as the manifests applied in [Configure OpenShift cluster Day 2 settings](configure-openshift-cluster-day-2-settings.md), by keeping them in Git.
- Event-Driven Ansible can start an on-demand backup when a change request is approved or a maintenance window opens.
