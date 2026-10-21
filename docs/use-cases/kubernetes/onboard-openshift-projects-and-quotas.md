---
title: Onboard OpenShift projects and quotas
summary: Create namespaces with quotas, limit ranges, network policies, role bindings and synced groups from a team request.
order: 20
personas: [Platform engineer, Cluster administrator]
collections: [kubernetes.core, redhat.openshift, infra.automation_development_office]
key_content:
  - kubernetes.core.k8s
  - kubernetes.core.k8s_info
  - redhat.openshift.openshift_adm_groups_sync
  - redhat.openshift.openshift_adm_prune_auth
  - infra.automation_development_office.ocp_namespace
  - infra.automation_development_office.ocp_service_accounts
  - infra.automation_development_office.ocp_network_policy
---

# Onboard OpenShift projects and quotas

## Description

Give new application teams a ready-to-use OpenShift project in minutes: namespace, resource quota, default limits, network isolation, role bindings and group membership are all created from one request. Doing this with Ansible keeps every project to the same standard and leaves a record of who asked for what.

## Notes

- Quota changes are a common follow-up request; reuse the same job template with a new tier value.
- Combine with [Configure OpenShift cluster Day 2 settings](configure-openshift-cluster-day-2-settings.md) so that identity providers exist before groups are synchronised.
- The `infra.automation_development_office` roles are validated content from Red Hat consulting; review their variables before using them in production.
- Event-Driven Ansible can trigger the same job from a ServiceNow or Git event when a project request is approved.
