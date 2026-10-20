---
title: Install Automation Platform on OpenShift
summary: Deploy Ansible Automation Platform on OpenShift with the Operator, with the cluster connection and platform settings defined as code.
order: 30
personas: [Platform engineer, OpenShift administrator, Solution architect]
collections: [infra.aap_utilities, infra.automation_development_office, redhat.openshift]
key_content:
  - infra.aap_utilities.aap_ocp_install
  - infra.automation_development_office.install_aap
  - infra.automation_development_office.ocp_aap_hub_harden
examples:
  - title: infra.aap_utilities validated collection
    url: https://github.com/redhat-cop/aap_utilities/
    note: includes the aap_ocp_install role
---

# Install Automation Platform on OpenShift

## Description

Install Ansible Automation Platform on an OpenShift cluster using the Ansible Automation Platform Operator. Ansible subscribes the operator, creates the platform resource with the gateway, controller, hub and Event-Driven Ansible, and keeps the cluster settings in Git, so a new environment is a pull request and a job run.

## Prerequisites

1. An OpenShift cluster with cluster-admin or namespace-admin access, a default storage class and the Red Hat operator catalog available (or a mirrored catalog for disconnected clusters).
2. An Automation Platform subscription (manifest or credentials) and access to the Red Hat container registry through the cluster pull secret.
3. A target namespace, an operator channel (for example a `stable-2.x` channel; the channel decides whether the 2.5+ platform resource is used) and a decision on cluster-scoped or namespace-scoped install.
4. A control node or execution environment with `kubernetes.core` and `redhat.openshift`, and an API token for the cluster stored as a credential.
5. A hostname and certificate plan for the routes, and an external PostgreSQL decision if the operator-managed database is not used.

## Steps

1. Define the installation variables: connection, namespace, operator channel and the platform settings (which components to deploy, replicas, storage, route hostnames).
2. Run the `infra.aap_utilities.aap_ocp_install` role to create the namespace, subscribe the operator and deploy the platform resource.
3. Wait for the operator and the components to report ready, then read the generated admin credentials from the cluster secret.
4. Apply the subscription and replace the default route certificates with corporate certificates.
5. Wrap the role in `infra.automation_development_office.install_aap` with `install_aap_target: openshift` when the same install is repeated across clusters and also needs license attachment.
6. Optional: for deployments where hub shares the controller database, run `infra.automation_development_office.ocp_aap_hub_harden` to move hub to its own PostgreSQL.
7. Configure organizations, authentication, credentials and projects as code, and add the cluster to backup scope.

## Success Criteria

1. The operator shows a succeeded status and the platform resource reports all components running.
2. The platform URL resolves over HTTPS with a trusted certificate and the administrator can log in.
3. A test job template launches a pod on the cluster and completes.
4. The installation variables are in Git and the playbook can be re-run without changes.

## Notes

- Follow with [Manage Automation Platform as code](manage-aap-as-code.md) and [Back up, restore and design HA and DR](back-up-restore-and-ha-dr.md).
- To move an existing RHEL-based deployment onto OpenShift, use [Move Automation Platform between installation types](move-aap-between-installation-types.md).
- Operator channels below 2.5 create separate controller, hub and Event-Driven Ansible resources; from 2.5 the single platform resource is used. Name the channel with a `major.minor` version so the role can tell them apart.
- Container groups on the same cluster can run jobs as pods; see [Scale and tune with automation mesh](scale-with-automation-mesh.md).
