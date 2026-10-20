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

## Prerequisites

1. Cluster-admin or a delegated onboarding role on each OpenShift cluster, held as an Automation Platform credential.
2. A project standard that defines quota tiers (small, medium, large), default limit ranges, network policies, labels and naming.
3. An identity source already connected to OpenShift (LDAP, OIDC or similar), and the group names that map to teams.
4. An intake method: a survey, a service catalog item or a Git file per team.

## Steps

1. Capture the request: team name, environment, quota tier, owners and cost centre.
2. Create the namespace with labels and annotations using `kubernetes.core.k8s`, or the `infra.automation_development_office.ocp_namespace` role.
3. Apply a `ResourceQuota` and `LimitRange` for the chosen tier with `kubernetes.core.k8s`.
4. Add default network isolation with `kubernetes.core.k8s`, or the `infra.automation_development_office.ocp_network_policy` role for NetworkPolicy and related objects.
5. Synchronise groups from the external identity provider with `redhat.openshift.openshift_adm_groups_sync`, then grant the team groups their roles through `RoleBinding` objects.
6. Create service accounts for pipelines with `infra.automation_development_office.ocp_service_accounts` or `kubernetes.core.k8s`.
7. Verify the result with `kubernetes.core.k8s_info` and notify the team with the project details.
8. For offboarding, remove stale role and group references with `redhat.openshift.openshift_adm_prune_auth` and delete the namespace after an approval step.

## Success Criteria

1. A new project exists with the correct quota, limits, labels and network policy.
2. Team members can log in and see only their own namespaces.
3. All projects of the same tier share the same settings, and the quota report shows usage against limits.
4. Offboarded teams leave no orphaned bindings or groups.

## Notes

- Quota changes are a common follow-up request; reuse the same job template with a new tier value.
- Combine with [Configure OpenShift cluster Day 2 settings](configure-openshift-cluster-day-2-settings.md) so that identity providers exist before groups are synchronised.
- The `infra.automation_development_office` roles are validated content from Red Hat consulting; review their variables before using them in production.
- Event-Driven Ansible can trigger the same job from a ServiceNow or Git event when a project request is approved.
