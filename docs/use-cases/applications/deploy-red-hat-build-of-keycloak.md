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

## Prerequisites

1. RHEL hosts with SSH access and privilege escalation.
2. A supported database and its credentials, and DNS names and TLS certificates for the Keycloak hostname.
3. Entitlement and download location for the Red Hat build of Keycloak archive.
4. Decisions on clustering, the admin account and the identity providers to connect.

## Steps

1. Download the product with `redhat.runtimes_common.product_download`.
2. Create the database with the database use case, for example [Install PostgreSQL and SQL Server](install-postgresql-and-sql-server.md).
3. Install and configure Keycloak with the `redhat.rhbk.keycloak` role: hostname, HTTPS, database settings and clustering.
4. Put a load balancer or reverse proxy in front of the nodes, and add them one by one.
5. Test sign-in with a sample client and check the health endpoints.
6. Add nodes or update versions by re-running the role. Upgrade nodes one at a time.

## Success Criteria

1. Keycloak runs as a service on each node and is reachable over HTTPS on the agreed hostname.
2. Nodes form a cluster and share sessions.
3. A sample application can sign in and sign out.

## Notes

- Use `redhat.rhbk.rhsso` or the `redhat.sso` collection for environments that still run Red Hat Single Sign-On, and plan the move to the newer product.
- Configuring realms, clients and users after installation is a separate task for Keycloak administration.
