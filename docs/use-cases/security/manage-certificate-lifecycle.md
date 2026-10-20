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

## Prerequisites

1. One or more certificate authorities with API access: CyberArk Certificate Manager (Venafi), Entrust, HashiCorp Vault PKI, the IdM CA or Active Directory Certificate Services.
2. Certificate policy: allowed key types, validity periods, naming rules, and which team owns each certificate.
3. An inventory of the services and hosts that use certificates, with the paths of the key and certificate files.
4. Credentials for the CA stored in Automation Platform or an external vault.

## Steps

1. Build the certificate inventory and record the expiry date, owner and CA for each entry.
2. Request certificates from the approved CA with `venafi.machine_identity.venafi_certificate`, `entrust.crypto.cagw_certificate`, `hashicorp.vault.pki_certificate` or `redhat.rhel_idm.ipacert`.
3. For hosts that renew from a CA by themselves, configure that with the `redhat.rhel_system_roles.certificate` role.
4. Deploy the certificate and key to the service, then reload it with a handler and test the endpoint.
5. Schedule a renewal job that selects certificates that expire within the threshold.
6. Revoke certificates for decommissioned or compromised systems with `venafi.machine_identity.venafi_certificate_revoke` or the CA's equivalent.
7. Manage Active Directory certificate templates with `microsoft.ad.cs_template` where AD CS issues the certificates.

## Success Criteria

1. Every certificate in scope has a known owner, CA and expiry date.
2. Renewal happens before the expiry threshold with no manual steps, and services are reloaded cleanly.
3. A report lists certificates that expire within the next 30 days.
4. Revoked certificates are no longer served by any host.

## Notes

- Keep private keys on the host that uses them, and do not copy them through job output or artifacts.
- `venafi.machine_identity` also covers SSH certificates, through `venafi.machine_identity.venafi_ssh_certificate`.
- Pair with Event-Driven Ansible to renew on an expiry alert from monitoring; see [Respond to security events with Event-Driven Ansible](respond-to-security-events-with-eda.md).
- Related: [Install Red Hat IdM servers, replicas and clients](install-red-hat-idm.md) for the IdM CA.
