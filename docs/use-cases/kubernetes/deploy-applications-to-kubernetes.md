---
title: Deploy applications to Kubernetes and OpenShift
summary: Roll out applications from manifests, Kustomize overlays, Helm charts or OpenShift templates, with scaling, routes and rollback built into the job.
order: 10
personas: [Platform engineer, DevOps engineer, Application owner]
collections: [kubernetes.core, redhat.openshift]
key_content:
  - kubernetes.core.k8s
  - kubernetes.core.helm
  - kubernetes.core.helm_repository
  - kubernetes.core.kustomize
  - kubernetes.core.k8s_info
  - kubernetes.core.k8s_rollback
  - redhat.openshift.openshift_process
  - redhat.openshift.openshift_route
examples:
  - title: kubernetes.core collection
    url: https://github.com/ansible-collections/kubernetes.core
  - title: redhat.openshift collection
    url: https://github.com/openshift/community.okd
---

# Deploy applications to Kubernetes and OpenShift

## Description

Deploy and update applications on Kubernetes or OpenShift from a single, auditable job template. The job applies manifests, Kustomize overlays or Helm charts, waits for the rollout to become healthy and rolls back if it does not. Environment differences are variables, so the same content promotes through development, test and production clusters.

## Notes

- Use `kubernetes.core.k8s_info` with `wait` conditions rather than fixed sleeps to keep jobs fast and reliable.
- Keep secrets out of Git. Retrieve them at run time from a vault or Automation Platform credentials.
- If an in-cluster GitOps tool already reconciles the cluster, use Ansible for the surrounding steps (namespace setup, secrets, approvals) rather than competing with it.
- Pair with [Onboard OpenShift projects and quotas](onboard-openshift-projects-and-quotas.md) for the namespace preparation and [Back up Kubernetes applications](back-up-kubernetes-applications.md) for protection.
- Event-Driven Ansible: a Git or registry webhook can trigger the deployment job when a new image or chart version is published.
