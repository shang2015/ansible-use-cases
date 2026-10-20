---
title: Integrate Active Directory and single sign-on
summary: Connect Linux, IdM, Keycloak and Automation Platform to Active Directory and external identity providers for central login.
order: 120
personas: [Identity engineer, Windows administrator, Security architect]
collections: [redhat.rhel_idm, redhat.rhel_system_roles, microsoft.ad, redhat.rhbk, ansible.platform, infra.automation_development_office]
key_content:
  - redhat.rhel_idm.ipatrust
  - infra.automation_development_office.idm_ad_trust
  - redhat.rhel_system_roles.ad_integration
  - microsoft.ad.user
  - microsoft.ad.group
  - redhat.rhbk.keycloak_identity_provider
  - ansible.platform.authenticator
  - ansible.platform.authenticator_map
---

# Integrate Active Directory and single sign-on

## Description

Let people use their existing corporate identity everywhere. Linux hosts either trust Active Directory through IdM or join it directly, and applications, including Automation Platform, authenticate through Red Hat build of Keycloak or another external identity provider.

## Prerequisites

1. An Active Directory forest with an administrative account for the trust or domain join.
2. Working DNS between AD and the Linux side, with forwarders or conditional forwarding.
3. For single sign-on: an identity provider that speaks SAML or OIDC, such as Red Hat build of Keycloak, Active Directory Federation Services or a third-party provider, and its connection details.
4. An agreed group mapping between directory groups and platform roles.

## Steps

1. Choose the model: a two-way trust between IdM and AD with `redhat.rhel_idm.ipatrust` and the `infra.automation_development_office.idm_ad_trust` role, or direct domain join with `redhat.rhel_system_roles.ad_integration`.
2. Manage AD-side objects that the integration needs, such as service accounts and groups, with `microsoft.ad.user` and `microsoft.ad.group`.
3. Configure Red Hat build of Keycloak as a broker: realms, clients and external providers with `redhat.rhbk.keycloak_identity_provider` and related `redhat.rhbk` modules.
4. Add the authentication source to Automation Platform with `ansible.platform.authenticator` and define which directory groups map to which teams and roles with `ansible.platform.authenticator_map`.
5. Test login for a pilot group, including role assignment in Automation Platform and `sudo` rights on Linux.
6. Roll out to all users and disable the local accounts that the integration replaces.

## Success Criteria

1. AD users can log in to Linux hosts with their AD credentials, through the trust or the direct join.
2. Users log in to Automation Platform with the external provider and receive roles from their group membership.
3. Removing a user from a directory group removes their access at the next login or sync.
4. Local fallback accounts are limited to documented break-glass users.

## Notes

- Okta and other SAML or OIDC providers can be configured as the upstream source of an authenticator; no Okta-specific collection is among the certified security content.
- Test the trust on a lab realm first, since DNS and time errors are the common causes of failure.
- Combine with [Install Red Hat IdM servers, replicas and clients](install-red-hat-idm.md) and [Manage users and access policy in IdM](manage-users-and-access-policy-in-idm.md).
