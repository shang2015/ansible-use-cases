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

## Notes

- Compute resources, compute profiles, global parameters, SCAP content and policies, job templates, webhooks and HTTP proxies are listed as not yet covered end to end by `infra.satellite_configuration`. Manage them with the `redhat.satellite` modules.
- The collection includes filters that drop locked (built-in) Satellite objects, so the export is meant to hold your own objects only. Review the first export before committing it.
- This tree defines the content that [Patch RHEL at scale](patch-rhel-at-scale.md) and [Provision RHEL with Satellite](provision-rhel-with-satellite.md) rely on.
