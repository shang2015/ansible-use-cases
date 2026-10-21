---
title: Deploy Red Hat build of Keycloak
summary: Install and configure Red Hat build of Keycloak servers for single sign-on.
order: 110
personas: [Identity engineer, Middleware administrator, Security engineer]
collections: [redhat.rhbk, redhat.sso, redhat.runtimes_common]
key_content:
  - redhat.rhbk.keycloak
  - redhat.rhbk.rhsso
  - redhat.sso.keycloak
  - redhat.runtimes_common.product_download
---

# Deploy Red Hat build of Keycloak

## Description

Single sign-on is delivered as a service for applications. Ansible installs Red Hat build of Keycloak with a database, TLS and clustering, so the identity service is the same in every environment and can be rebuilt on demand.

## Notes

- Use `redhat.rhbk.rhsso` or the `redhat.sso` collection for environments that still run Red Hat Single Sign-On, and plan the move to the newer product.
- Configuring realms, clients and users after installation is a separate task for Keycloak administration.
