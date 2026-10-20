---
title: Configure Satellite as code
summary: Export Satellite configuration to Git, apply it to other servers and detect drift between Git and the live system.
order: 30
personas: [Linux administrator, Platform engineer]
collections: [infra.satellite_configuration, redhat.satellite]
key_content:
  - infra.satellite_configuration.filetree_create
  - infra.satellite_configuration.filetree_read
  - infra.satellite_configuration.dispatch
  - infra.satellite_configuration.filetree_reconcile
  - redhat.satellite.organizations
  - redhat.satellite.lifecycle_environments
  - redhat.satellite.content_views
  - redhat.satellite.activation_keys
examples:
  - title: infra.satellite_configuration validated collection
    url: https://github.com/redhat-cop/infra.satellite_configuration
    note: export, import and reconcile Satellite configuration as code
---

# Configure Satellite as code

## Description

Keep the configuration of Red Hat Satellite (organizations, locations, products, repositories, content views, lifecycle environments, activation keys, host groups) as YAML in Git. The same definitions can then build a new Satellite, rebuild a lost one or promote settings from a test server to production.

## Prerequisites

1. A running Satellite with API access for an administrator account, stored as an automation controller credential.
2. A Git repository for the configuration tree and an automation controller project that points to it.
3. A subscription manifest for each organization that owns Red Hat content.
4. An execution environment with `redhat.satellite` and `infra.satellite_configuration`. The collection documents Ansible Core 2.16 or later and a supported Satellite release (6.17 is named in its README).

## Steps

1. Export the current configuration of an existing Satellite with the `infra.satellite_configuration.filetree_create` role into one `satellite_<resource>.d/` directory per object type, and commit it to Git. For a new site, start from a hand-written tree in the same layout.
2. Replace the placeholders in the generated `vault_template.yaml` with secrets and encrypt the file with Ansible Vault or an external secrets credential.
3. Describe differences between environments as override files (for example the URL and administrator contact settings) and keep them outside the base tree.
4. Import into the target Satellite by running the `infra.satellite_configuration.filetree_read` role to load the tree and the `infra.satellite_configuration.dispatch` role to apply it.
5. Check the result against Git with `infra.satellite_configuration.filetree_reconcile`, which compares live configuration with the tree and writes reconcile diff files.
6. Put export, import and reconcile into job templates. Run import from a pull request merge and reconcile on a schedule.
7. For small changes, call the single-object roles such as `redhat.satellite.organizations`, `redhat.satellite.lifecycle_environments`, `redhat.satellite.content_views` and `redhat.satellite.activation_keys` directly.

## Success Criteria

1. A new Satellite built from the Git tree has the same organizations, content views, lifecycle environments and activation keys as the source.
2. The reconcile job reports no difference, or lists exactly the objects changed by hand.
3. All configuration changes are pull requests with a reviewer and a history.

## Notes

- Compute resources, compute profiles, global parameters, SCAP content and policies, job templates, webhooks and HTTP proxies are listed as not yet covered end to end by `infra.satellite_configuration`. Manage them with the `redhat.satellite` modules.
- The collection includes filters that drop locked (built-in) Satellite objects, so the export is meant to hold your own objects only. Review the first export before committing it.
- This tree defines the content that [Patch RHEL at scale](patch-rhel-at-scale.md) and [Provision RHEL with Satellite](provision-rhel-with-satellite.md) rely on.
