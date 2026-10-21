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

## Notes

- On OpenShift, node operating system updates are normally managed by the platform itself; use this use case for the surrounding drain and hardware steps, or for non-OpenShift Kubernetes clusters.
- Pair with [Update server firmware and BIOS](../infrastructure/update-server-firmware-and-bios.md) for bare-metal nodes.
- `kubernetes.core.k8s_exec`, `k8s_log` and `k8s_cp` help with troubleshooting steps inside the same workflow.
- Event-Driven Ansible can react to node-not-ready events and start a diagnostic job.
