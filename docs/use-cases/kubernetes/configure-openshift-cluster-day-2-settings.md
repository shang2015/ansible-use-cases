---
title: Configure OpenShift cluster Day 2 settings
summary: "Apply and keep consistent the post-install configuration of OpenShift clusters: identity, certificates, operators, networking and logging."
order: 30
personas: [Platform engineer, Cluster administrator]
collections: [kubernetes.core, redhat.openshift, infra.automation_development_office]
key_content:
  - kubernetes.core.k8s
  - kubernetes.core.k8s_cluster_info
  - infra.automation_development_office.ocp_ldap_auth
  - infra.automation_development_office.ocp_oidc_auth
  - infra.automation_development_office.ocp_cert_manager
  - infra.automation_development_office.ocp_operator_subscription
  - infra.automation_development_office.ocp_nmstate_install
  - infra.automation_development_office.ocp_metallb_install
  - infra.automation_development_office.ocp_logging
---

# Configure OpenShift cluster Day 2 settings

## Description

After a cluster is installed, every cluster still needs the same set of settings: identity providers, certificates, operators, node networking, load balancing and logging. Capture them as Ansible content in Git and apply them to every cluster, so new clusters are brought to standard quickly and existing clusters can be checked for drift.

## Prerequisites

1. Cluster-admin access to each OpenShift cluster, stored as a credential in Automation Platform.
2. A written baseline that lists the operators, identity providers, certificate authority, networks and logging targets expected on every cluster.
3. Access to the operator catalogs the cluster uses (including mirrored catalogs for disconnected environments).
4. A Git repository holding per-cluster and per-environment variable files.

## Steps

1. Record the starting point with `kubernetes.core.k8s_cluster_info` and `kubernetes.core.k8s_info`, and confirm the cluster version and available APIs.
2. Configure authentication with `infra.automation_development_office.ocp_ldap_auth` or `ocp_oidc_auth`, and a break-glass administrator with `ocp_htpasswd_admin` if the standard calls for it.
3. Install operators declaratively with `infra.automation_development_office.ocp_operator_subscription` and wait for readiness using `ocp_wait_operator`.
4. Configure certificates with `infra.automation_development_office.ocp_cert_manager` and `ocp_default_ingress_cert`.
5. Configure node and service networking: `ocp_nmstate_install` for node network policies and `ocp_metallb_install` for load balancer address pools.
6. Configure cluster logging with `infra.automation_development_office.ocp_logging`, and set the console banner with `ocp_console_banner`.
7. For any setting without a ready-made role, apply the manifest with `kubernetes.core.k8s` from the Git repository.
8. Run the same job in check mode on a schedule and report differences from the baseline.

## Success Criteria

1. A newly installed cluster reaches the baseline by running one workflow.
2. All clusters report the same identity providers, operators and certificates as the baseline.
3. Drift checks are scheduled and differences raise a ticket.
4. Cluster changes are traceable to commits in Git and to job runs.

## Notes

- Cluster installation itself and the Red Hat Advanced Cluster Security configuration are outside this use case; see the Security use cases for RHACS.
- The `infra.automation_development_office` roles are validated content; their descriptions vary in detail, so read each role's documentation and defaults first.
- Use [Onboard OpenShift projects and quotas](onboard-openshift-projects-and-quotas.md) after identity and operators are in place.
- Event-Driven Ansible can trigger a drift correction job when a configuration object such as an operator subscription is changed outside Git.
