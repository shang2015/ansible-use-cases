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

## Notes

- Cluster installation itself and the Red Hat Advanced Cluster Security configuration are outside this use case; see the Security use cases for RHACS.
- The `infra.automation_development_office` roles are validated content; their descriptions vary in detail, so read each role's documentation and defaults first.
- Use [Onboard OpenShift projects and quotas](onboard-openshift-projects-and-quotas.md) after identity and operators are in place.
- Event-Driven Ansible can trigger a drift correction job when a configuration object such as an operator subscription is changed outside Git.
