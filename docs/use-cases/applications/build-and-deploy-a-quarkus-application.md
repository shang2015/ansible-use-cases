---
title: Build and deploy a Quarkus application from Git
summary: Build a Quarkus application from a Git repository and run it as a service on RHEL.
order: 50
personas: [Application developer, Middleware administrator]
collections: [redhat.quarkus, redhat.runtimes_common]
key_content:
  - redhat.quarkus.quarkus
  - redhat.quarkus.playbook
  - redhat.runtimes_common.tail_grep
---

# Build and deploy a Quarkus application from Git

## Description

Teams that run Quarkus applications on virtual machines or bare metal can have the build, install and service setup done by Ansible. The role clones the repository, builds the application and starts it as a systemd service, so a new environment needs one job run.

## Notes

- For container deployments use the Kubernetes and OpenShift use cases instead.
- For pre-built artifacts see [Deploy applications from a Maven repository](deploy-applications-from-a-maven-repository.md).
