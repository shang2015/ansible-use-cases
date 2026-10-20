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

## Prerequisites

1. A Maven repository with the artifact published, and a read-only account.
2. Target application servers already installed, see [Deploy and patch JBoss EAP](deploy-and-patch-jboss-eap.md).
3. A naming and versioning scheme for artifacts (group, artifact, version, packaging).
4. A job template survey or pipeline variable that selects the environment and version.

## Steps

1. Define the artifact coordinates and the repository URL as variables, with the repository credentials stored in Automation Platform.
2. Download the artifact with `redhat.runtimes_common.maven_artifact`, and verify the checksum.
3. Deploy it to the server with the `redhat.eap.wildfly_app_deploy` role, setting the application name and context.
4. Wait for the deployment to finish by checking the server log with `redhat.runtimes_common.tail_grep`.
5. Run `redhat.eap.wildfly_validation` and an application-level test request.
6. On failure, redeploy the previous version, which is a normal run with the earlier version number.
7. Trigger the job from the CI pipeline with the automation controller API, or from a ServiceNow change.

## Success Criteria

1. The deployed version on each server equals the requested version.
2. Re-running a deployment with the same version makes no change.
3. A rollback is a single job run with the older version number.

## Notes

- Use [Build and deploy a Quarkus application from Git](build-and-deploy-a-quarkus-application.md) when the application is built on the target from source.
- Do not store repository passwords in playbooks. Use a credential.
