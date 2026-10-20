---
title: Build and update edge OS images
summary: Compose RHEL for Edge images with osbuild-composer, host them, and update rpm-ostree systems to new versions.
order: 30
personas: [Edge platform engineer, Linux administrator]
collections: [infra.osbuild, ansible.posix]
key_content:
  - infra.osbuild.setup_server
  - infra.osbuild.builder
  - infra.osbuild.populate_aap
  - infra.osbuild.update_system
  - infra.osbuild.system_info
  - ansible.posix.rpm_ostree_upgrade
  - ansible.posix.rhel_rpm_ostree
examples:
  - title: infra.osbuild validated collection
    url: https://github.com/redhat-cop/infra.osbuild
    note: build server, image build and update roles for rpm-ostree systems
---

# Build and update edge OS images

## Description

Build the operating system for edge devices as a versioned image, publish it, and move devices to the next version in a controlled way. Updates are image-based (rpm-ostree), so devices change in one step to a known version.

## Prerequisites

1. A RHEL build server with osbuild-composer, subscriptions and access to the package repositories.
2. A Git project with blueprint and variable files for each device type.
3. Network access from devices to the image host (the HTTP server on the build server or an internal mirror).
4. SSH access to rpm-ostree devices, or enrollment into a fleet manager for larger estates.

## Steps

1. Set up the build server with `infra.osbuild.setup_server`. It also installs an HTTP server for images and kickstart files.
2. Build the image with the `infra.osbuild.builder` role. Select the image type with `builder_compose_type`: `edge-commit`, `edge-container`, `edge-installer`, `edge-simplified-installer` or `edge-raw-image` are the tested types.
3. Publish the output. Images are served from `/var/www/html/<blueprint_name>/images` in version sub-directories, and the kickstart file at `<blueprint_name>/kickstart.ks`.
4. Install new devices from the installer image or kickstart. For consistent job templates, load the build and update jobs with `infra.osbuild.populate_aap`.
5. Record the current state with `infra.osbuild.system_info`, which gathers information from rpm-ostree based systems.
6. Move devices to the new image with `infra.osbuild.update_system` or with the `ansible.posix.rpm_ostree_upgrade` module, in waves, and reboot when the new deployment is ready.
7. Where a package must be layered onto a device, add it with `ansible.posix.rhel_rpm_ostree`, and treat this as an exception.
8. Re-run `infra.osbuild.system_info` after each wave to confirm the version.

## Success Criteria

1. A new image version is built from Git-tracked inputs and published under its blueprint and version.
2. Devices report the new image version after the update wave.
3. A failed device is identified by the version check and does not block the remaining waves.
4. Image content can be reproduced from the repository.

## Notes

- The previous deployment stays on an rpm-ostree system after an update, so a device can be returned to it. Test the rollback on a spare device before the first production wave.
- Build MicroShift into the image with [Deploy MicroShift at the edge](deploy-microshift-at-the-edge.md).
- For large fleets, define the image in [Manage device fleets with Red Hat Edge Manager](manage-device-fleets-with-edge-manager.md) and let Edge Manager roll it out.
- General-purpose image builds are described in [Build golden images with image builder](../linux/build-golden-images.md).
