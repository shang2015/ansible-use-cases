---
title: Onboard teams with RBAC and single sign-on
summary: Connect Automation Platform to LDAP, SAML or OIDC and give each team its own organization, roles and resources.
order: 50
personas: [Platform engineer, Security architect, Automation lead]
collections: [ansible.platform, infra.aap_configuration, infra.aap_configuration_extended, redhat.rhbk]
key_content:
  - ansible.platform.authenticator
  - ansible.platform.authenticator_map
  - ansible.platform.organization
  - ansible.platform.team
  - ansible.platform.role_definition
  - ansible.platform.role_team_assignment
  - infra.aap_configuration.gateway_authenticators
---

# Onboard teams with RBAC and single sign-on

## Description

Let users sign in with the corporate identity provider and receive access automatically, based on group membership. Each business team gets an organization, a team, and role assignments on the resources it owns, so new teams are onboarded by adding a few lines of configuration rather than by clicking through the UI.

## Prerequisites

1. An identity provider (LDAP or Active Directory, SAML or OpenID Connect) with a service account or application registration for the platform.
2. A list of teams, the identity provider groups that map to them, and the access each needs (for example execute-only, project admin, auditor).
3. A running Automation Platform 2.5+ with the platform gateway reachable by the identity provider, and TLS trusted by both sides.
4. The configuration repository from [Manage Automation Platform as code](manage-aap-as-code.md), or an administrator token.

## Steps

1. Define the access model: one organization per business unit or tenant, one team per function, and the role definitions (built-in or custom) each team needs.
2. Create the authenticator for the identity provider with `ansible.platform.authenticator`; keep a local break-glass administrator.
3. Map identity provider attributes or groups to platform organizations, teams and administrator status with `ansible.platform.authenticator_map`.
4. Create organizations and teams with `ansible.platform.organization` and `ansible.platform.team`.
5. Define custom roles where the built-in ones are too broad with `ansible.platform.role_definition`, and grant them to teams with `ansible.platform.role_team_assignment` at organization or object level.
6. Express the same objects as variables for `infra.aap_configuration.gateway_authenticators` and the related gateway roles, so onboarding a team is a pull request.
7. Test with a user from each group, confirm what that user sees, and record the results.

## Success Criteria

1. A user signs in with corporate credentials and lands in the correct organization and team without manual steps.
2. Removing a user from the identity provider group removes the access at the next login.
3. Each team sees only its own projects, inventories, credentials and job templates.
4. A new team can be onboarded by one merge request in under an agreed time.
5. The local administrator account exists, is vaulted and is tested.

## Notes

- Configuration written for Automation Platform 2.4 or earlier keeps LDAP and SAML settings in the controller. `infra.aap_configuration_extended.upgrade_config` converts them into gateway authenticators and authenticator maps; see [Migrate from Ansible Tower or AAP 2.4 to AAP 2.5 and later](migrate-to-aap-2-5-or-later.md).
- Role assignment roles in `infra.aap_configuration` differ between 2.5 and 2.6 (controller and gateway variants); use the variant that matches the release.
- Credentials for the managed systems should come from a secret manager through credential input sources rather than being stored per team.
- Put the identity provider itself under automation if it is Red Hat build of Keycloak; the `redhat.rhbk` collection manages realms, clients and users.
