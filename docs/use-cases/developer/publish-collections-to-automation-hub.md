---
title: Publish collections to automation hub
summary: Build, publish, approve and distribute internal collections through private automation hub.
order: 40
personas: [Automation developer, Platform engineer, Content curator]
collections: [ansible.hub, infra.aap_configuration]
key_content:
  - ansible.hub.ah_namespace
  - ansible.hub.ah_build
  - ansible.hub.ah_collection_upload
  - ansible.hub.ah_approval
  - ansible.hub.collection_repository
  - ansible.hub.collection_remote
  - infra.aap_configuration.ansible_config
---

# Publish collections to automation hub

## Description

Give teams one trusted place to get automation content. Internal roles and modules are packaged as collections, published to private automation hub, reviewed, approved and then installed by pipelines, execution environment builds and developers from one source. Certified and validated content can be synced alongside it.

## Notes

- See [Build CI/CD for automation content](build-cicd-for-automation-content.md) for the pipeline, and [Build and manage execution environments](../platform/build-execution-environments.md) for the images that consume the collections.
- Hub objects (namespaces, repositories, remotes, groups) can be managed with the `hub_*` roles in `infra.aap_configuration`; see [Manage Automation Platform as code](../platform/manage-aap-as-code.md).
- Disconnected sites need an offline sync of the collections they use.
- Do not publish secrets or environment-specific variables in collections. Keep them in inventories and credentials.
