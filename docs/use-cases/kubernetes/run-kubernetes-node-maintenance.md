---
title: Run Kubernetes node maintenance and cluster housekeeping
summary: Cordon, drain, taint and return nodes safely, and prune unused images, builds and stale references on OpenShift.
order: 50
personas: [Platform engineer, Cluster administrator, Operations lead]
collections: [kubernetes.core, redhat.openshift]
key_content:
  - kubernetes.core.k8s_drain
  - kubernetes.core.k8s_taint
  - kubernetes.core.k8s_info
  - kubernetes.core.k8s_cluster_info
  - redhat.openshift.openshift_adm_prune_images
  - redhat.openshift.openshift_adm_prune_builds
  - redhat.openshift.openshift_registry_info
---

# Run Kubernetes node maintenance and cluster housekeeping

## Description

Take cluster nodes out of service for patching, hardware work or replacement without disrupting applications, and keep the cluster tidy by pruning old images, builds and unused references. The same jobs run on a schedule or inside larger patching and firmware workflows.

## Prerequisites

1. Cluster-admin access (or a role that can cordon, drain and taint nodes) stored as a credential.
2. A maintenance policy: allowed windows, nodes drained one at a time or in batches, and the time to wait for pod eviction.
3. Applications that tolerate eviction, with PodDisruptionBudgets in place for critical workloads.
4. For pruning, agreed retention rules for images and builds.

## Steps

1. Check cluster health first with `kubernetes.core.k8s_cluster_info` and `kubernetes.core.k8s_info` (node conditions, cluster operators, pending pods).
2. Cordon and drain the node with `kubernetes.core.k8s_drain`, setting a timeout and the handling of daemon set and local-storage pods.
3. Perform the maintenance, for example an operating system update or firmware job, from the same workflow.
4. Return the node with `kubernetes.core.k8s_drain` in uncordon mode and wait for the node to be `Ready`.
5. Use `kubernetes.core.k8s_taint` to dedicate nodes to workloads, or to keep workloads off nodes that are in test.
6. Move to the next node only after the previous one is healthy and pods have rescheduled.
7. Run housekeeping on a schedule: report registry usage with `redhat.openshift.openshift_registry_info`, then prune with `redhat.openshift.openshift_adm_prune_images`, `redhat.openshift.openshift_adm_prune_builds` and `redhat.openshift.openshift_adm_prune_deployments`.

## Success Criteria

1. Nodes are drained, serviced and returned one at a time, with application availability maintained.
2. The workflow stops if the cluster is unhealthy before or after a node returns.
3. Image and build storage stays within agreed limits.
4. Each maintenance run has a job log that shows which nodes were touched and when.

## Notes

- On OpenShift, node operating system updates are normally managed by the platform itself; use this use case for the surrounding drain and hardware steps, or for non-OpenShift Kubernetes clusters.
- Pair with [Update server firmware and BIOS](../infrastructure/update-server-firmware-and-bios.md) for bare-metal nodes.
- `kubernetes.core.k8s_exec`, `k8s_log` and `k8s_cp` help with troubleshooting steps inside the same workflow.
- Event-Driven Ansible can react to node-not-ready events and start a diagnostic job.
