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

## Prerequisites

1. A backup solution installed on each cluster. This use case uses Trilio for Kubernetes through `trilio.trilio_kubernetes`; OpenShift API for Data Protection (OADP) can be installed with the `infra.automation_development_office.ocp_oadp` role.
2. A backup target (S3-compatible object storage or NFS) with credentials, and storage classes that support snapshots.
3. A list of namespaces or applications in scope, with backup frequency and retention requirements.
4. Cluster credentials in Automation Platform with rights to create the backup custom resources.

## Steps

1. Install the backup operator with the `trilio.trilio_kubernetes.trilio_kubernetes` role, or install OADP with the `ocp_oadp` role, and verify the pods with `kubernetes.core.k8s_info`.
2. Create the backup target and retention policy objects through the role variables, or apply them with `kubernetes.core.k8s`.
3. Define backup plans for each application namespace, including schedule and retention, and store them in Git.
4. Run on-demand backups before risky changes by adding a backup job as the first node of the change workflow.
5. Monitor results by checking the backup status objects with `kubernetes.core.k8s_info` and send failures to a notification channel.
6. Test recovery regularly: restore a chosen backup into a scratch namespace or a second cluster, run a smoke test and delete the test copy.
7. For migration between clusters, run the restore against the destination cluster with the same role.

## Success Criteria

1. Every in-scope application has a backup plan and a successful backup within its schedule window.
2. A restore into a test namespace completes and the application passes its smoke test.
3. Backup failures are reported within the job output and in a notification.
4. Recovery time from the last restore test is recorded and meets the agreed target.

## Notes

- Backup of VMs on OpenShift Virtualization is covered in [Operate VMs on OpenShift Virtualization](../virtualization/operate-vms-on-openshift-virtualization.md).
- Storage-level snapshots and replication can complement application backups; see [Manage snapshots, clones and replication](../storage/manage-snapshots-clones-and-replication.md).
- Back up the cluster configuration, such as the manifests applied in [Configure OpenShift cluster Day 2 settings](configure-openshift-cluster-day-2-settings.md), by keeping them in Git.
- Event-Driven Ansible can start an on-demand backup when a change request is approved or a maintenance window opens.
