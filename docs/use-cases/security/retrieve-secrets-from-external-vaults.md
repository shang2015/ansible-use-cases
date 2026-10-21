---
title: Retrieve secrets from external vaults
summary: Fetch passwords, tokens and keys from HashiCorp Vault, CyberArk, 1Password and other vaults at job runtime, so none are stored in playbooks.
order: 80
personas: [Security engineer, Automation architect, Platform administrator]
collections: [hashicorp.vault, cyberark.conjur, cyberark.isp, onepassword.connect, delinea.ss, akeyless.secrets_management, ansible.controller]
key_content:
  - hashicorp.vault.kv2_secret_get
  - hashicorp.vault.kv2_secret_info
  - cyberark.conjur.conjur_variable
  - cyberark.isp.cyberark_credential
  - onepassword.connect.field_info
  - ansible.controller.credential_input_source
---

# Retrieve secrets from external vaults

## Description

Keep secrets in the corporate vault and let automation read them only when a job runs. Automation Platform authenticates to the vault, passes the value to the job, and never writes it to the project, the inventory or the job output.

## Notes

- Prefer credential input sources for platform credentials, and direct lookups only when a playbook needs a value for its own use.
- `delinea.ss` and `akeyless.secrets_management` are certified collections; check their documentation for the plugins available in your version.
- Rotate the values themselves with [Rotate privileged credentials](rotate-privileged-credentials.md).
- Pair with Event-Driven Ansible by storing rulebook credentials in the same way; `ansible.eda.credential_input_source` exists for that purpose.
