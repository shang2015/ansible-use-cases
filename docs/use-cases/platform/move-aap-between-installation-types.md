---
title: Move Automation Platform between installation types
summary: Export a running platform to a portable artifact and import it into a containerized or OpenShift deployment.
order: 100
personas: [Platform engineer, Solution architect, OpenShift administrator]
collections: [ansible.aap_snapshot]
key_content:
  - ansible.aap_snapshot.artifact_export
  - ansible.aap_snapshot.artifact_import
  - ansible.aap_snapshot.artifact_verify
  - ansible.aap_snapshot.aap_component_info
  - ansible.aap_snapshot.validate_migration_artifact
  - ansible.aap_snapshot.preflight
examples:
  - title: ansible.aap_snapshot collection
    url: https://github.com/ansible-collections/aap-snapshot-collection
    note: export, verify and import playbooks and workflow documentation
---

# Move Automation Platform between installation types

## Description

Re-platform a running Automation Platform deployment without rebuilding it by hand, for example from the RPM installer to the containerized installer or to OpenShift. Ansible exports the data of the controller, hub (with its content), gateway and Event-Driven Ansible into one artifact, checks it, and imports it into a prepared target of the same version.

## Prerequisites

1. A source deployment on Automation Platform 2.6 or later, installed with the RPM or containerized installer, with SSH and `become` access to its component hosts.
2. A target deployment of the same major.minor version, already installed and configured: authentication, TLS certificates, remote execution environments, networking and firewall rules. The import moves data but does not replace target settings.
3. A supported path: RPM to OpenShift Operator, RPM to containerized, containerized to OpenShift Operator, or containerized to containerized. OpenShift to OpenShift is not supported yet.
4. Enough disk space on the execution host and the component hosts for the database dump and hub content, and `rsync` on both ends.
5. A Kubernetes configuration with namespace-admin or cluster-admin rights if the target is OpenShift.

## Steps

1. Discover what the source runs with `ansible.aap_snapshot.aap_component_info` and run the `ansible.aap_snapshot.preflight` checks.
2. Build and configure the target platform from scratch with the matching install use case, and do not create objects in it.
3. Export the source with the `ansible.aap_snapshot.artifact_export` playbook, setting `aap_platform` to `rpm` or `containerized`. Set `artifact_export_hub_content` to false only if hub content is rebuilt elsewhere.
4. Verify the artifact with `ansible.aap_snapshot.artifact_verify` before importing. The `ansible.aap_snapshot.validate_migration_artifact` module offers the same check for custom playbooks.
5. Import into the target with `ansible.aap_snapshot.artifact_import`, setting `aap_platform` to `containerized` or `operator`, and for OpenShift the namespace and instance name.
6. Check each component: sign-in, organizations, job templates, a hub collection download and a rulebook activation.
7. Run representative jobs on the target, then switch DNS or load balancer entries to the new gateway and retire the source.

## Success Criteria

1. The artifact passes verification and its version matches the target.
2. Controller, hub, gateway and Event-Driven Ansible data on the target match the source: counts of organizations, users, templates, collections and activations.
3. Hub collections and execution environment images download from the target.
4. Representative job templates complete on the target.
5. Clients use the new URLs and the source is stopped.

## Notes

- Cross-version imports are not supported. To change version, export from a source running the target version, or upgrade first.
- The target keeps its own configuration. Anything environment-specific (identity provider, certificates, mesh nodes) must be done in advance.
- Use the same workflow as a portable backup between installations of the same type; see [Back up, restore and design HA and DR](back-up-restore-and-ha-dr.md).
- For moves from Tower or 2.4, which change the architecture, use [Migrate from Ansible Tower or AAP 2.4 to AAP 2.5 and later](migrate-to-aap-2-5-or-later.md) instead.
