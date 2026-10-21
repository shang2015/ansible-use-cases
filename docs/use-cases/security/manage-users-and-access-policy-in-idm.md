---
title: Manage users and access policy in IdM
summary: Maintain users, groups, host access rules, sudo rules and password policy in Red Hat IdM as code.
order: 110
personas: [Identity engineer, Security engineer, Linux administrator]
collections: [redhat.rhel_idm, redhat.rhel_system_roles]
key_content:
  - redhat.rhel_idm.ipauser
  - redhat.rhel_idm.ipagroup
  - redhat.rhel_idm.ipahostgroup
  - redhat.rhel_idm.ipahbacrule
  - redhat.rhel_idm.ipasudorule
  - redhat.rhel_idm.ipapwpolicy
---

# Manage users and access policy in IdM

## Description

Define who can log in where, and who can run what with elevated rights, in files under version control. Joiner, mover and leaver changes and access policy changes are made through reviewed pull requests and applied by Automation Platform.

## Notes

- Test HBAC changes on a limited host group first, because a wrong rule can lock out administrators.
- Use `redhat.rhel_system_roles.sudo` for hosts that are not in IdM.
- For organizations that source users from Active Directory, see [Integrate Active Directory and single sign-on](integrate-active-directory-and-sso.md).
