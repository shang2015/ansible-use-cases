---
title: Remediate vulnerabilities from scanner findings
summary: Turn vulnerability scanner findings into patch and configuration jobs, with approval, verification and ticket updates in one closed loop.
order: 30
personas: [Security engineer, Vulnerability management lead, Linux administrator]
collections: [redhat.satellite, ansible.controller, ansible.eda, servicenow.itsm]
key_content:
  - redhat.satellite.host_errata_info
  - redhat.satellite.content_view_version
  - redhat.satellite.job_invocation
  - ansible.controller.workflow_job_template
  - ansible.eda.webhook
  - servicenow.itsm.change_request
---

# Remediate vulnerabilities from scanner findings

## Description

Close the gap between "the scanner found it" and "it is fixed and verified". Findings from a vulnerability scanner start a workflow in Automation Platform that maps each finding to a fix, applies it with the right approvals, and asks the scanner to confirm that the finding has gone.

## Prerequisites

1. A vulnerability scanner that can export findings or send a webhook or API call (for example Tenable Nessus), with a service account for Automation Platform.
2. A patch source for the fixes, for example Red Hat Satellite content views with errata, or a configuration playbook for findings that are not patch-related.
3. A mapping between finding types and remediation playbooks, agreed with the owners of the affected systems.
4. A change process: approval rules and a ticketing system such as ServiceNow.

## Steps

1. Ingest the findings: poll the scanner API from a job template, or receive a webhook in an Event-Driven Ansible rulebook with the `ansible.eda.webhook` source.
2. Map each finding to the affected host and to a fix, using `redhat.satellite.host_errata_info` for applicable errata or a lookup table for configuration findings.
3. Open a change record with `servicenow.itsm.change_request` and group the hosts by maintenance window.
4. Promote the fix to the target environment with `redhat.satellite.content_view_version`, then apply it with `redhat.satellite.job_invocation` or the remediation playbook.
5. Chain the steps in a workflow with `ansible.controller.workflow_job_template`, including an approval node before production hosts.
6. Trigger a re-scan of the remediated hosts and compare the findings before and after.
7. Close the change record when the re-scan no longer reports the finding, and keep the result for reporting.

## Success Criteria

1. Each finding in scope is linked to a workflow run, a change record and a target host.
2. Fixes reach production only after the approval node, and the approver is recorded.
3. The re-scan confirms the finding is gone, and the workflow fails visibly if it is not.
4. Mean time from finding to verified fix is measured from workflow timestamps.

## Notes

- There is no Red Hat Certified collection for Tenable, Qualys or Rapid7 today; integrations call the scanner's REST API (for example with `ansible.builtin.uri`) or use community content from Ansible Galaxy. See the [security vendor pages](../../vendors/index.md) for what exists and how it is supported.
- Not every finding can be patched. Route configuration findings to [Harden RHEL to CIS and DISA STIG baselines](harden-rhel-to-cis-and-stig.md) and send the rest to a ticket with an exception owner.
- Kernel or library updates may need a reboot. Add a reboot and wait step to the workflow and respect maintenance windows.
- Pair with [Scan and remediate compliance](scan-and-remediate-compliance.md) for policy-level findings.
- Pair with Event-Driven Ansible for the trigger, as described in [Respond to security events with Event-Driven Ansible](respond-to-security-events-with-eda.md).
