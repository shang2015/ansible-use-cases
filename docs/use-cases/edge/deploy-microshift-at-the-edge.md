---
title: Deploy MicroShift at the edge
summary: Install or image-build MicroShift on RHEL edge nodes and deploy applications to them as Kubernetes manifests.
order: 20
personas: [Edge platform engineer, Application owner]
collections: [edge.microshift, infra.osbuild]
key_content:
  - edge.microshift.rpm_install
  - edge.microshift.image_builder
  - edge.microshift.app
  - edge.microshift.microshift_rpm_install
  - edge.microshift.microshift_image_build
  - edge.microshift.microshift_app
examples:
  - title: edge.microshift validated collection
    url: https://github.com/redhat-cop/edge.microshift
    note: install, image build and application roles for MicroShift
---

# Deploy MicroShift at the edge

## Description

Run a small, supported Kubernetes platform on single-node edge sites. The collection installs MicroShift on RHEL either directly from RPM packages or inside an rpm-ostree image, and deploys application manifests to the running node, so each site gets the same platform and workloads.

## Notes

- Combine with [Manage device fleets with Red Hat Edge Manager](manage-device-fleets-with-edge-manager.md) when the number of sites makes direct SSH access impractical.
- For Kubernetes workflows on larger clusters, see the Kubernetes use cases instead; MicroShift targets small single-node deployments.
- Keep the pull secret out of Git, and rotate it with the credential store.
