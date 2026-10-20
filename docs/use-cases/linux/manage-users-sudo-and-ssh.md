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

## Prerequisites

1. A list of required access by team and host group, owned by a security or operations lead.
2. Privileged access to the hosts and a break-glass account that the automation never changes.
3. For directory logins, an Active Directory or IdM domain and an account allowed to join hosts.
4. Public SSH keys collected from a source of record, not typed into the playbook by hand.

## Steps

1. Join hosts to Active Directory with `redhat.rhel_system_roles.ad_integration` so that most users authenticate against the directory. For IdM, use the `redhat.rhel_idm` collection.
2. Create the local accounts that must exist (service and break-glass accounts) and groups with `ansible.builtin.user` and `ansible.builtin.group`.
3. Distribute public keys with `ansible.posix.authorized_key`. Use `exclusive: true` where the managed list should be the only list of keys.
4. Define sudo rules as data and apply them with `redhat.rhel_system_roles.sudo`, one drop-in file per team, validated before they take effect.
5. Set client-side SSH defaults, such as ciphers and host key checking, with `redhat.rhel_system_roles.ssh`.
6. Set file access rules for shared directories with `ansible.posix.acl` where group permissions are not enough.
7. Run the job template on a schedule and after each team change, and send the changed-task output to the audit log.

## Success Criteria

1. Each user and key on a host maps to an approved entry in Git.
2. Keys of departed users are removed from all hosts at the next run.
3. Sudo rights match the approved rules, and no unmanaged rules remain in the sudoers drop-in directory.
4. Access changes appear as reviewed commits with matching job runs.

## Notes

- The `ssh` role configures the SSH client. Server-side `sshd` hardening is a separate task and belongs to the security hardening use cases.
- The sudo role can replace the distribution `/etc/sudoers` and has an option to remove unlisted drop-in files. Test on one host first, and keep the break-glass account out of the change.
- Store secrets such as the AD join password in an automation controller credential, not in variables.
- Combine with [Standardise RHEL configuration](standardise-rhel-configuration.md) so access settings are part of the same baseline.
- Windows equivalents are in [Manage Active Directory](../windows/manage-active-directory.md).
