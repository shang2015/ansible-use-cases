---
title: Rotate privileged credentials
summary: Onboard accounts into a privileged access vault and rotate database and service passwords on a schedule or after an event.
order: 90
personas: [Security engineer, PAM administrator, Database administrator]
collections: [cyberark.isp, cyberark.pas, hashicorp.vault, delinea.pas, ansible.controller]
key_content:
  - cyberark.isp.cyberark_safe
  - cyberark.isp.cyberark_account
  - cyberark.isp.cyberark_safe_member
  - hashicorp.vault.database_connection
  - hashicorp.vault.database_static_role
  - hashicorp.vault.database_credential_rotation
  - delinea.pas.delinea_vault
---

# Rotate privileged credentials

## Description

Replace long-lived shared passwords with credentials that the vault owns and changes regularly. Automation onboards accounts into the privileged access system, sets up rotation, and updates the systems that depend on the credentials.

## Prerequisites

1. A privileged access platform: CyberArk Privilege Cloud or PAS, HashiCorp Vault with the database secrets engine, or Delinea.
2. An inventory of privileged and service accounts with owners, target systems and consumers.
3. An automation identity in the vault with rights to create safes, accounts and members.
4. A maintenance window for services that cannot yet read the new credential dynamically.

## Steps

1. Create the safes and grant access with `cyberark.isp.cyberark_safe` and `cyberark.isp.cyberark_safe_member`.
2. Onboard accounts from the inventory with `cyberark.isp.cyberark_account`, or `cyberark.pas.cyberark_account` for self-hosted PAS.
3. For databases in HashiCorp Vault, register the connection with `hashicorp.vault.database_connection` and define rotation per account with `hashicorp.vault.database_static_role`.
4. Rotate database credentials on demand with `hashicorp.vault.database_credential_rotation`.
5. Enroll Linux hosts into Delinea privileged access with the `delinea.pas.delinea_vault`, `delinea.pas.delinea_auth` and `delinea.pas.delinea_audit` roles where that platform is used.
6. Update the consumers: applications and jobs read the current value from the vault as described in [Retrieve secrets from external vaults](retrieve-secrets-from-external-vaults.md).
7. Schedule a job template that reports accounts that are not onboarded or not rotated within the policy interval.

## Success Criteria

1. Every account in scope is registered in the vault with an owner and a rotation policy.
2. Rotation completes on schedule, and dependent applications continue to work with the new value.
3. Shared static passwords for the migrated accounts are removed or disabled.
4. The compliance report lists exceptions with an owner.

## Notes

- Rotate a test account first and confirm every consumer picks up the new value before widening the scope.
- Use the vault's own audit log as the record of who retrieved which credential.
- Pair with Event-Driven Ansible to rotate immediately after a suspected compromise; the `cyberark.pas.syslog` event source can feed such a rulebook, see [Respond to security events with Event-Driven Ansible](respond-to-security-events-with-eda.md).
