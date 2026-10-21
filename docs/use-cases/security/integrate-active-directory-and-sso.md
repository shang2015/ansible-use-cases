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

## Notes

- Okta and other SAML or OIDC providers can be configured as the upstream source of an authenticator; no Okta-specific collection is among the certified security content.
- Test the trust on a lab realm first, since DNS and time errors are the common causes of failure.
- Combine with [Install Red Hat IdM servers, replicas and clients](install-red-hat-idm.md) and [Manage users and access policy in IdM](manage-users-and-access-policy-in-idm.md).
