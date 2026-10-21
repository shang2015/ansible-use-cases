---
title: Patch RHEL at scale
summary: Control patch content with Satellite content views and lifecycle environments, then roll it out ring by ring.
order: 50
personas: [Linux administrator, Operations lead]
collections: [redhat.satellite]
key_content:
  - redhat.satellite.lifecycle_environment
  - redhat.satellite.content_view
  - redhat.satellite.content_view_publish
  - redhat.satellite.content_view_version
  - redhat.satellite.host_errata_info
  - redhat.satellite.job_invocation
  - redhat.satellite.sync_plan
  - redhat.satellite.content_view_version_cleanup
---

# Patch RHEL at scale

## Description

Patch every RHEL host from content that has been tested, not from whatever is newest. Satellite freezes the package set in content view versions and promotes it through lifecycle environments (for example Dev, Test, Production); Ansible publishes, promotes and applies the patches in a controlled order.

## Notes

- Build the whole cycle as a workflow: sync, publish, promote to Dev, patch Dev, approval, promote to Test, and so on.
- Take LVM snapshots before patching critical hosts with the roles described in [Upgrade RHEL in place with snapshot rollback](upgrade-rhel-in-place.md).
- Use [Remediate with Red Hat Insights](remediate-rhel-with-insights.md) to find and fix vulnerabilities, and this use case for planned, bulk patching.
- Start the lifecycle design in [Configure Satellite as code](configure-satellite-as-code.md) so content views and environments are versioned.
