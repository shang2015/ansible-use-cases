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

## Prerequisites

1. A Satellite with RHEL repositories synced and hosts registered with activation keys that point to a content view and lifecycle environment.
2. An inventory in automation controller built from Satellite, with host groups or host collections that match the patch rings.
3. Maintenance windows agreed for each ring, and a rollback method (snapshots or VM backups) for critical hosts.
4. Satellite and host credentials stored as automation controller credentials.

## Steps

1. Create the lifecycle path with `redhat.satellite.lifecycle_environment` and keep repository content current with `redhat.satellite.sync_plan`, or run `redhat.satellite.repository_sync` on demand.
2. Define content views with `redhat.satellite.content_view`. Add filters (`redhat.satellite.content_view_filter`) to hold back errata types or dates when policy requires it.
3. Publish a new version on a cadence, for example monthly, with the `redhat.satellite.content_view_publish` role or `redhat.satellite.content_view_version`.
4. Promote the version to the first environment by setting `lifecycle_environments` on `redhat.satellite.content_view_version`. Promote to later environments only after tests pass.
5. Report applicable errata per host with `redhat.satellite.host_errata_info` and attach the result to the change record.
6. Apply the updates to hosts in the promoted environment with a job template that runs a package update (for example `ansible.builtin.dnf`) or with Satellite remote execution through `redhat.satellite.job_invocation`. Use `serial` or ring-based inventory groups to limit the blast radius.
7. Reboot hosts when required (for example after kernel or core library updates) and verify service state and listening ports afterwards.
8. Remove unused versions with the `redhat.satellite.content_view_version_cleanup` role, keeping a set number of previous versions for rollback.

## Success Criteria

1. Every host reports the content view version of its lifecycle environment, and hosts in Production never receive content that skipped Test.
2. The number of hosts with applicable security errata falls to zero after each patch window.
3. Each ring has a job record showing what changed and when.
4. Failed hosts are listed with the reason and are excluded from the next ring.

## Notes

- Build the whole cycle as a workflow: sync, publish, promote to Dev, patch Dev, approval, promote to Test, and so on.
- Take LVM snapshots before patching critical hosts with the roles described in [Upgrade RHEL in place with snapshot rollback](upgrade-rhel-in-place.md).
- Use [Remediate with Red Hat Insights](remediate-rhel-with-insights.md) to find and fix vulnerabilities, and this use case for planned, bulk patching.
- Start the lifecycle design in [Configure Satellite as code](configure-satellite-as-code.md) so content views and environments are versioned.
