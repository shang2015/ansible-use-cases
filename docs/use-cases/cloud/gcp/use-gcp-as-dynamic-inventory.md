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

## Notes

- Pair with Event-Driven Ansible to run a job when a new instance appears, if an event source for the organization's messaging service is available.
- Restrict the service account to read-only roles for inventory.
- Instance details beyond inventory can be gathered with the `google.cloud.gcp_compute_instance_info` module.
