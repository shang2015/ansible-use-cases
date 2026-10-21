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

## Notes

- The previous deployment stays on an rpm-ostree system after an update, so a device can be returned to it. Test the rollback on a spare device before the first production wave.
- Build MicroShift into the image with [Deploy MicroShift at the edge](deploy-microshift-at-the-edge.md).
- For large fleets, define the image in [Manage device fleets with Red Hat Edge Manager](manage-device-fleets-with-edge-manager.md) and let Edge Manager roll it out.
- General-purpose image builds are described in [Build golden images with image builder](../linux/build-golden-images.md).
