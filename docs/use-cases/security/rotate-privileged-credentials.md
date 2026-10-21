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

## Notes

- Rotate a test account first and confirm every consumer picks up the new value before widening the scope.
- Use the vault's own audit log as the record of who retrieved which credential.
- Pair with Event-Driven Ansible to rotate immediately after a suspected compromise; the `cyberark.pas.syslog` event source can feed such a rulebook, see [Respond to security events with Event-Driven Ansible](respond-to-security-events-with-eda.md).
