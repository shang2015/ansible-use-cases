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

## Prerequisites

1. A private automation hub (part of Automation Platform) with a user or token that may create namespaces and upload collections.
2. Collections with a `galaxy.yml` that follows the team's namespace and versioning rules (semantic versioning).
3. A reviewer group that approves content before it becomes visible to consumers, and a policy for which external content is allowed.
4. A CI pipeline that builds from a tagged commit.
5. A token from the Red Hat hosted automation hub if certified and validated content is to be synced.

## Steps

1. Create the namespace for the team's collections with `ansible.hub.ah_namespace`, and give the owning group permissions.
2. Build the collection archive from the tagged commit with `ansible.hub.ah_build`.
3. Upload it to hub with `ansible.hub.ah_collection_upload`, which places it in the staging repository.
4. After review and automated checks, move it to the published repository with `ansible.hub.ah_approval`.
5. Create the repositories consumers use with `ansible.hub.collection_repository` (for example a curated set per environment), and for external content add a remote with `ansible.hub.collection_remote` and sync only the collections on the allow-list.
6. Generate the client configuration with the `infra.aap_configuration.ansible_config` role, so that pipelines and developer workspaces point to the hub, in the right order, with a token.
7. Pin collection versions in each project and execution environment `requirements.yml`, and rebuild the environments when a version changes.
8. Deprecate old versions on a schedule and record who consumes what.

## Success Criteria

1. A tagged release results in a collection on hub with no manual upload.
2. Consumers install a collection with `ansible-galaxy` from hub only.
3. Only approved collections appear in the consumer repositories.
4. Every execution environment records the exact collection versions it contains.
5. External content is limited to the approved list.

## Notes

- See [Build CI/CD for automation content](build-cicd-for-automation-content.md) for the pipeline, and [Build and manage execution environments](../platform/build-execution-environments.md) for the images that consume the collections.
- Hub objects (namespaces, repositories, remotes, groups) can be managed with the `hub_*` roles in `infra.aap_configuration`; see [Manage Automation Platform as code](../platform/manage-aap-as-code.md).
- Disconnected sites need an offline sync of the collections they use.
- Do not publish secrets or environment-specific variables in collections. Keep them in inventories and credentials.
