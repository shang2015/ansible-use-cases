---
title: Use Google Cloud as a dynamic inventory source
summary: Build inventories from live Compute Engine instances, grouped by label, zone and project.
order: 30
personas: [Cloud engineer, Automation architect]
collections: [google.cloud]
key_content:
  - google.cloud.gcp_compute
  - google.cloud.gcp_compute_instance
  - google.cloud.gcp_compute_instance_info
---

# Use Google Cloud as a dynamic inventory source

## Description

Use Google Cloud as the source of truth for which Compute Engine instances exist. Automation Platform syncs instances from one or more projects, and groups them by label, zone or machine type so jobs always target current machines.

## Prerequisites

1. A service account with read access to Compute Engine in each project, stored as a Google Compute Engine credential in Automation Platform.
2. A labeling standard for environment, application and owner.
3. Network access from the execution environment to the instances.
4. An execution environment containing `google.cloud` and the Google authentication libraries.

## Steps

1. Create a project with an inventory source file for the `google.cloud.gcp_compute` plugin, naming the Google Cloud projects, zones and filters.
2. Add `keyed_groups` for labels and zones, and set `hostnames` and `compose` so `ansible_host` uses an address the execution environment can reach.
3. Create an inventory in Automation Platform, add the project as a source with the Google credential, and schedule updates.
4. Use one inventory source per project or organization boundary.
5. Run configuration jobs against label-based groups, and use the instance creation job in [Provision Google Cloud networking and compute](provision-google-cloud-networking-and-compute.md) to add machines.

## Success Criteria

1. New instances appear in the inventory after the next sync, in the correct groups.
2. Deleted or stopped instances are excluded according to the filter.
3. Jobs can target a group such as `env_prod` without a manual host list.
4. Each project in scope has a working inventory source.

## Notes

- Pair with Event-Driven Ansible to run a job when a new instance appears, if an event source for the organization's messaging service is available.
- Restrict the service account to read-only roles for inventory.
- Instance details beyond inventory can be gathered with the `google.cloud.gcp_compute_instance_info` module.
