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

## Notes

- Configuration written for Automation Platform 2.4 or earlier keeps LDAP and SAML settings in the controller. `infra.aap_configuration_extended.upgrade_config` converts them into gateway authenticators and authenticator maps; see [Migrate from Ansible Tower or AAP 2.4 to AAP 2.5 and later](migrate-to-aap-2-5-or-later.md).
- Role assignment roles in `infra.aap_configuration` differ between 2.5 and 2.6 (controller and gateway variants); use the variant that matches the release.
- Credentials for the managed systems should come from a secret manager through credential input sources rather than being stored per team.
- Put the identity provider itself under automation if it is Red Hat build of Keycloak; the `redhat.rhbk` collection manages realms, clients and users.
