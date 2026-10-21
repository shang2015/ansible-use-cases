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

## Notes

- Follow with [Manage Automation Platform as code](manage-aap-as-code.md) and [Back up, restore and design HA and DR](back-up-restore-and-ha-dr.md).
- To move an existing RHEL-based deployment onto OpenShift, use [Move Automation Platform between installation types](move-aap-between-installation-types.md).
- Operator channels below 2.5 create separate controller, hub and Event-Driven Ansible resources; from 2.5 the single platform resource is used. Name the channel with a `major.minor` version so the role can tell them apart.
- Container groups on the same cluster can run jobs as pods; see [Scale and tune with automation mesh](scale-with-automation-mesh.md).
