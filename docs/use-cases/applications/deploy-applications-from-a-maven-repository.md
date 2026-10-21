---
title: Deploy applications from a Maven repository
summary: Download versioned build artifacts from Maven and deploy them to application servers in a repeatable job.
order: 40
personas: [Application owner, Release engineer, Middleware administrator]
collections: [redhat.runtimes_common, redhat.eap]
key_content:
  - redhat.runtimes_common.maven_artifact
  - redhat.eap.wildfly_app_deploy
  - redhat.eap.wildfly_validation
  - redhat.runtimes_common.tail_grep
---

# Deploy applications from a Maven repository

## Description

Build pipelines publish WAR and JAR files to a Maven repository such as Nexus or Artifactory. A job pulls an exact version from the repository and deploys it to the target servers, so any environment can be given any released version in the same way.

## Notes

- Use [Build and deploy a Quarkus application from Git](build-and-deploy-a-quarkus-application.md) when the application is built on the target from source.
- Do not store repository passwords in playbooks. Use a credential.
