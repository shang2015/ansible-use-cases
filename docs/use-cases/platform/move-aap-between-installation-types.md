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

## Notes

- Cross-version imports are not supported. To change version, export from a source running the target version, or upgrade first.
- The target keeps its own configuration. Anything environment-specific (identity provider, certificates, mesh nodes) must be done in advance.
- Use the same workflow as a portable backup between installations of the same type; see [Back up, restore and design HA and DR](back-up-restore-and-ha-dr.md).
- For moves from Tower or 2.4, which change the architecture, use [Migrate from Ansible Tower or AAP 2.4 to AAP 2.5 and later](migrate-to-aap-2-5-or-later.md) instead.
