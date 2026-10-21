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

## Notes

- There is no Red Hat Certified collection for Tenable, Qualys or Rapid7 today; integrations call the scanner's REST API (for example with `ansible.builtin.uri`) or use community content from Ansible Galaxy. See the [security vendor pages](../../vendors/index.md) for what exists and how it is supported.
- Not every finding can be patched. Route configuration findings to [Harden RHEL to CIS and DISA STIG baselines](harden-rhel-to-cis-and-stig.md) and send the rest to a ticket with an exception owner.
- Kernel or library updates may need a reboot. Add a reboot and wait step to the workflow and respect maintenance windows.
- Pair with [Scan and remediate compliance](scan-and-remediate-compliance.md) for policy-level findings.
- Pair with Event-Driven Ansible for the trigger, as described in [Respond to security events with Event-Driven Ansible](respond-to-security-events-with-eda.md).
