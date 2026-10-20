---
title: Build golden images with image builder
summary: Define OS images as code, compose them on an osbuild-composer server and publish them for installation.
order: 10
personas: [Linux administrator, Platform engineer]
collections: [infra.osbuild]
key_content:
  - infra.osbuild.setup_server
  - infra.osbuild.builder
  - infra.osbuild.create_blueprint
  - infra.osbuild.push_blueprint
  - infra.osbuild.start_compose
  - infra.osbuild.wait_compose
  - infra.osbuild.export_compose
  - infra.osbuild.inject_ks
examples:
  - title: infra.osbuild validated collection
    url: https://github.com/redhat-cop/infra.osbuild
    note: roles, modules and example playbooks for osbuild-composer
---

# Build golden images with image builder

## Description

Replace hand-built "gold" images with images that are defined as code, composed on a schedule and published to a known location. Every image is traceable to a blueprint in Git, so a rebuild after a security fix is one job run instead of a manual exercise.

## Prerequisites

1. A RHEL, CentOS Stream or Fedora host for the build server, reachable over SSH, with access to the package repositories the image needs (Red Hat CDN, Satellite or an internal mirror).
2. Blueprint definitions (packages, users, services, kernel options) stored in a Git repository used as an automation controller project.
3. A web location for the finished images, by default the Apache server that the build server role sets up.
4. Subscription credentials stored as automation controller credentials.

## Steps

1. Set up the build server with the `infra.osbuild.setup_server` role (osbuild-composer plus an HTTP server for images and kickstart files). If packages come from Satellite, use the role's Satellite variables.
2. Describe the image with `infra.osbuild.create_blueprint` and load it into the composer service with `infra.osbuild.push_blueprint`. Add custom package sources with `infra.osbuild.repository`.
3. Start the build with `infra.osbuild.start_compose` and wait for it with `infra.osbuild.wait_compose`. The `infra.osbuild.builder` role runs this whole flow in one call, selecting the image type with `builder_compose_type`.
4. Export the result with `infra.osbuild.export_compose`. For installer ISOs, embed a kickstart with `infra.osbuild.inject_ks`.
5. Publish the image and kickstart under the build server's web root, using one directory per blueprint and version.
6. Create job templates for server setup and image build, or load them with the `infra.osbuild.populate_aap` role, and run the build on a schedule or from a pipeline when blueprints change.
7. Chain build, test installation and publish in a workflow, with an approval step before the image is marked for production use.

## Success Criteria

1. The same blueprint in Git produces an equivalent image on every run.
2. Each published image is stored under a blueprint and version path and can be fetched over HTTP.
3. A system installed from the image boots and reports the expected packages and configuration.
4. A rebuild after a package update requires no manual steps on the build server.

## Notes

- The image types that the collection documents as tested are the RHEL for Edge types (`edge-commit`, `edge-container`, `edge-installer`, `edge-simplified-installer`, `edge-raw-image`). See [Build and update edge OS images](../edge/build-and-update-edge-os-images.md) for the edge-specific flow.
- Image-based installs pair with [Provision RHEL with Satellite](provision-rhel-with-satellite.md), which uses the same kickstart and host group concepts.
- Keep post-install configuration out of the image where possible and apply it with [Standardise RHEL configuration](standardise-rhel-configuration.md) after first boot, so one image serves many roles.
