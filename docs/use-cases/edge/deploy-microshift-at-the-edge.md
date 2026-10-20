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

## Prerequisites

1. RHEL systems for the MicroShift nodes. The collection README names RHEL 9.2 as the tested platform; check the MicroShift documentation for current supported versions.
2. A Red Hat pull secret, stored as an automation controller credential or secret variable.
3. For image-based installs, an osbuild-composer build server with access to the MicroShift repositories.
4. Application manifests (Kubernetes YAML) in a Git project.

## Steps

1. Choose the install method. For package-based nodes, run `edge.microshift.rpm_install` with the pull secret and the MicroShift version. For image-based nodes, build an image with `edge.microshift.image_builder`.
2. Use the playbooks `edge.microshift.microshift_rpm_install` or `edge.microshift.microshift_image_build` as job template playbooks to run the roles.
3. For image builds, set the Red Hat repositories (`microshift_rhsm_repos`) or custom repositories (`microshift_image_custom_repos`) that the image needs, then distribute the image as in [Build and update edge OS images](build-and-update-edge-os-images.md).
4. Deploy the workload with `edge.microshift.app`, providing the pull secret and the list of manifest files in `microshift_app_manifests`, or use the playbook `edge.microshift.microshift_app`.
5. Schedule the application job for each site group, and use labels or inventory groups for site-specific settings.
6. Verify the node and workloads after each run with a health check that lists pods and node status.

## Success Criteria

1. MicroShift is running on every target node at the intended version.
2. The application manifests are applied on every node, and its pods are running.
3. Re-running the job on an unchanged node makes no changes.
4. A node rebuilt from the same image and manifests returns to the same state.

## Notes

- Combine with [Manage device fleets with Red Hat Edge Manager](manage-device-fleets-with-edge-manager.md) when the number of sites makes direct SSH access impractical.
- For Kubernetes workflows on larger clusters, see the Kubernetes use cases instead; MicroShift targets small single-node deployments.
- Keep the pull secret out of Git, and rotate it with the credential store.
