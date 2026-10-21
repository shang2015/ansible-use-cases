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

## Notes

- Applying a STIG or CIS profile can change SSH, authentication and audit settings. Test on non-production hosts first and keep out-of-band console access.
- Hardening is the fix side of compliance. Use [Scan and remediate compliance](scan-and-remediate-compliance.md) to measure it.
- Controls for the identity layer are covered in [Install Red Hat IdM](install-red-hat-idm.md).
- Pair with Event-Driven Ansible to re-apply the baseline when a configuration change on a host is detected, for example from `ansible.eda.file_watch`.
