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

## Notes

- The image types that the collection documents as tested are the RHEL for Edge types (`edge-commit`, `edge-container`, `edge-installer`, `edge-simplified-installer`, `edge-raw-image`). See [Build and update edge OS images](../edge/build-and-update-edge-os-images.md) for the edge-specific flow.
- Image-based installs pair with [Provision RHEL with Satellite](provision-rhel-with-satellite.md), which uses the same kickstart and host group concepts.
- Keep post-install configuration out of the image where possible and apply it with [Standardise RHEL configuration](standardise-rhel-configuration.md) after first boot, so one image serves many roles.
