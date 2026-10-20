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

## Prerequisites

1. One or more clusters and a service account or token for each environment, stored as an Automation Platform credential (kubeconfig or API token).
2. An execution environment with `kubernetes.core`, `redhat.openshift`, the Kubernetes Python client and, if used, the Helm binary.
3. Application content in Git: manifests, Kustomize directories, Helm charts or OpenShift templates.
4. Agreed namespaces, image registry access and pull secrets.

## Steps

1. Authenticate to the cluster, using a token credential or `redhat.openshift.openshift_auth` when an explicit login is required.
2. Create or update the namespace and supporting objects with `kubernetes.core.k8s`.
3. Render and apply the application:
   - for plain manifests or rendered Kustomize output, use `kubernetes.core.k8s` with the `kubernetes.core.kustomize` lookup;
   - for Helm, add a chart source with `kubernetes.core.helm_repository` and install or upgrade with `kubernetes.core.helm`, optionally previewing with `kubernetes.core.helm_template`;
   - for OpenShift templates, use `redhat.openshift.openshift_process`.
4. Expose the service with `kubernetes.core.k8s_service` or `redhat.openshift.openshift_route`.
5. Wait for readiness with `kubernetes.core.k8s_info`, checking Deployment status and Pod conditions, and run a smoke test.
6. On failure, restore the previous revision with `kubernetes.core.k8s_rollback` (Deployments and DaemonSets), or redeploy the previous chart version with `kubernetes.core.helm`.
7. Scale as needed with `kubernetes.core.k8s_scale`, and record the deployed revision in the release record.
8. Chain deployments into a workflow that promotes the same version from test to production with an approval node.

## Success Criteria

1. The application version in Git is the version running in the target namespace.
2. A failed rollout does not leave the environment in a broken state.
3. Re-running with unchanged content reports no changes.
4. Each deployment has a job record showing who deployed what, where and when.

## Notes

- Use `kubernetes.core.k8s_info` with `wait` conditions rather than fixed sleeps to keep jobs fast and reliable.
- Keep secrets out of Git. Retrieve them at run time from a vault or Automation Platform credentials.
- If an in-cluster GitOps tool already reconciles the cluster, use Ansible for the surrounding steps (namespace setup, secrets, approvals) rather than competing with it.
- Pair with [Onboard OpenShift projects and quotas](onboard-openshift-projects-and-quotas.md) for the namespace preparation and [Back up Kubernetes applications](back-up-kubernetes-applications.md) for protection.
- Event-Driven Ansible: a Git or registry webhook can trigger the deployment job when a new image or chart version is published.
