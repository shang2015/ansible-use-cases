---
title: Harden RHEL to CIS and DISA STIG baselines
summary: Apply a security baseline to every RHEL host with certified hardening roles and system roles, and keep it enforced.
order: 10
personas: [Security engineer, Linux administrator, Compliance officer]
collections: [redhat.rhel_hardening_roles, infra.automation_development_office, redhat.rhel_system_roles]
key_content:
  - infra.automation_development_office.rhel_stig_cac
  - redhat.rhel_system_roles.selinux
  - redhat.rhel_system_roles.crypto_policies
  - redhat.rhel_system_roles.auditd
  - redhat.rhel_system_roles.aide
  - redhat.rhel_system_roles.fapolicyd
  - redhat.rhel_system_roles.ssh
---

# Harden RHEL to CIS and DISA STIG baselines

## Description

Bring new and existing RHEL servers to a documented security baseline such as CIS or DISA STIG, and re-apply it on a schedule so that hosts do not drift. The same automation is used at build time and for hosts already in production.

## Prerequisites

1. Agreement on the target baseline and profile (for example CIS Level 1 or a DISA STIG), including the list of approved exceptions.
2. An inventory of RHEL hosts grouped by major version and by function, with privileged SSH access through an Automation Platform machine credential.
3. A test group of hosts that mirrors production workloads, and a change window for the first production run.
4. An execution environment that includes `redhat.rhel_hardening_roles`, `infra.automation_development_office` and `redhat.rhel_system_roles`.

## Steps

1. Choose the baseline content: the roles in `redhat.rhel_hardening_roles`, or the `infra.automation_development_office.rhel_stig_cac` role for DISA STIG Compliance-as-Code on RHEL 8, 9 and 10.
2. Record every approved exception as a variable in the inventory or in a group variable file, with the reason and an owner, instead of editing the role.
3. Complement the baseline with the system roles that implement individual controls: `redhat.rhel_system_roles.selinux`, `redhat.rhel_system_roles.crypto_policies`, `redhat.rhel_system_roles.auditd`, `redhat.rhel_system_roles.aide`, `redhat.rhel_system_roles.fapolicyd` and `redhat.rhel_system_roles.ssh`.
4. Create a job template that runs the hardening playbook, and run it first against the test group with check mode enabled to preview changes.
5. Run it against production in batches by using the job template's slice or limit settings, and review the job output for failed tasks.
6. Schedule the job template to re-apply the baseline, and add it to the image or kickstart build pipeline so new hosts start hardened.
7. Verify the result with a scan as described in [Scan and remediate compliance](scan-and-remediate-compliance.md).

## Success Criteria

1. Every host in scope has had the baseline applied, and the job history shows the date, the content version and the result per host.
2. Exceptions exist only as reviewed variables, each with an owner and a reason.
3. A follow-up compliance scan shows no failed rules other than the documented exceptions.
4. A re-run of the job template reports no unexpected changes on hosts that have not drifted.

## Notes

- Applying a STIG or CIS profile can change SSH, authentication and audit settings. Test on non-production hosts first and keep out-of-band console access.
- Hardening is the fix side of compliance. Use [Scan and remediate compliance](scan-and-remediate-compliance.md) to measure it.
- Controls for the identity layer are covered in [Install Red Hat IdM](install-red-hat-idm.md).
- Pair with Event-Driven Ansible to re-apply the baseline when a configuration change on a host is detected, for example from `ansible.eda.file_watch`.
