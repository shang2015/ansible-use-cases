---
title: Manage users, sudo and SSH
summary: Control who can log in to Linux hosts and what they can run, from directory integration to sudo rules and SSH keys.
order: 70
personas: [Linux administrator, Security engineer]
collections: [redhat.rhel_system_roles, ansible.posix, redhat.rhel_idm]
key_content:
  - redhat.rhel_system_roles.sudo
  - redhat.rhel_system_roles.ssh
  - redhat.rhel_system_roles.ad_integration
  - ansible.posix.authorized_key
  - ansible.posix.acl
---

# Manage users, sudo and SSH

## Description

Make access to Linux hosts consistent and auditable. Identities come from a directory where possible; local accounts, SSH keys and sudo rules that remain are defined in Git and applied by Ansible, including the removal of access when people leave a team.

## Notes

- The `ssh` role configures the SSH client. Server-side `sshd` hardening is a separate task and belongs to the security hardening use cases.
- The sudo role can replace the distribution `/etc/sudoers` and has an option to remove unlisted drop-in files. Test on one host first, and keep the break-glass account out of the change.
- Store secrets such as the AD join password in an automation controller credential, not in variables.
- Combine with [Standardise RHEL configuration](standardise-rhel-configuration.md) so access settings are part of the same baseline.
- Windows equivalents are in [Manage Active Directory](../windows/manage-active-directory.md).
