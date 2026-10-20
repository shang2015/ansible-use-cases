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

## Prerequisites

1. A working IdM domain, as described in [Install Red Hat IdM servers, replicas and clients](install-red-hat-idm.md).
2. An IdM account for automation with the privileges needed to manage users, groups and rules, stored as a credential.
3. An authoritative source for users and roles, such as an HR system export or a Git-based access file.
4. An agreed model for groups, host groups and who may use sudo on which hosts.

## Steps

1. Describe users and groups in YAML and apply them with `redhat.rhel_idm.ipauser` and `redhat.rhel_idm.ipagroup`.
2. Group hosts with `redhat.rhel_idm.ipahostgroup` and enrolled hosts with `redhat.rhel_idm.ipahost`.
3. Define who may log in where with `redhat.rhel_idm.ipahbacrule`, and elevated rights with `redhat.rhel_idm.ipasudorule` together with `redhat.rhel_idm.ipasudocmd` and `redhat.rhel_idm.ipasudocmdgroup`.
4. Set password and lockout rules with `redhat.rhel_idm.ipapwpolicy`.
5. Run the job template from a pull-request merge or on a schedule, and use the state `absent` for leavers.
6. Run a report job that lists users without group membership, disabled accounts and rules that match no hosts.

## Success Criteria

1. Users, groups and rules in IdM match the files in Git after each run.
2. Access for a leaver is removed in the next run, and the removal is recorded.
3. HBAC and sudo rules exist for every host group, and no broad "allow all" rule remains.
4. Changes are traceable to a reviewed pull request.

## Notes

- Test HBAC changes on a limited host group first, because a wrong rule can lock out administrators.
- Use `redhat.rhel_system_roles.sudo` for hosts that are not in IdM.
- For organizations that source users from Active Directory, see [Integrate Active Directory and single sign-on](integrate-active-directory-and-sso.md).
