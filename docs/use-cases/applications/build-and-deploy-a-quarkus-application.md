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

## Prerequisites

1. A Git repository with the Quarkus project and read credentials.
2. Target RHEL hosts with SSH access, a supported JDK and, for builds on the host, Maven and network access to the Maven repositories.
3. Decisions on the service user, ports and configuration properties per environment.

## Steps

1. Set the repository URL, branch or tag, and the application settings as variables.
2. Run the `redhat.quarkus.quarkus` role, or the collection playbook `redhat.quarkus.playbook`, to build and deploy the application.
3. Provide environment-specific properties through inventory or group variables, not through changes to the repository.
4. Wait for the application to report a successful start with `redhat.runtimes_common.tail_grep`.
5. Check the application health endpoint and a sample request.
6. Create a job template with a survey for the tag to deploy, and run it from the CI pipeline.

## Success Criteria

1. The application runs as a service on the target host and answers a health check.
2. The deployed version corresponds to the Git tag requested.
3. A second run with the same tag changes nothing.

## Notes

- For container deployments use the Kubernetes and OpenShift use cases instead.
- For pre-built artifacts see [Deploy applications from a Maven repository](deploy-applications-from-a-maven-repository.md).
