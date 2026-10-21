---
title: Manage the certificate lifecycle
summary: Request, deploy, renew and revoke TLS and SSH certificates from internal and commercial CAs.
order: 130
personas: [PKI administrator, Security engineer, Platform operations]
collections: [venafi.machine_identity, entrust.crypto, hashicorp.vault, redhat.rhel_idm, redhat.rhel_system_roles, microsoft.ad]
key_content:
  - venafi.machine_identity.venafi_certificate
  - venafi.machine_identity.venafi_certificate_revoke
  - entrust.crypto.cagw_certificate
  - hashicorp.vault.pki_certificate
  - redhat.rhel_idm.ipacert
  - redhat.rhel_system_roles.certificate
---

# Manage the certificate lifecycle

## Description

Stop certificate expiry from causing outages. Automation requests certificates from the approved authority, installs them where services use them, reloads the services, and renews or revokes certificates on a schedule or on demand.

## Notes

- Keep private keys on the host that uses them, and do not copy them through job output or artifacts.
- `venafi.machine_identity` also covers SSH certificates, through `venafi.machine_identity.venafi_ssh_certificate`.
- Pair with Event-Driven Ansible to renew on an expiry alert from monitoring; see [Respond to security events with Event-Driven Ansible](respond-to-security-events-with-eda.md).
- Related: [Install Red Hat IdM servers, replicas and clients](install-red-hat-idm.md) for the IdM CA.
