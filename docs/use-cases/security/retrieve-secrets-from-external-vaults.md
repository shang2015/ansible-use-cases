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

## Prerequisites

1. A supported vault with an identity for Automation Platform that has read-only access to the required paths: HashiCorp Vault, CyberArk Secrets Manager (Conjur) or Credential Provider, 1Password Connect, Delinea Secret Server or Akeyless.
2. A network path from the execution nodes or execution environments to the vault.
3. A naming scheme for secret paths, by application and environment.
4. An execution environment with the vault collection installed, where playbooks call the vault directly.

## Steps

1. Create the vault role or policy for automation with least privilege, scoped to the secret paths each team needs.
2. Store the vault connection details as a credential in Automation Platform and keep its own token short-lived.
3. Link target credentials, such as machine, cloud or network credentials, to the vault with `ansible.controller.credential_input_source`, so values are resolved at launch.
4. For secrets needed inside a playbook, use the vault plugin directly: `hashicorp.vault.kv2_secret_get`, `cyberark.conjur.conjur_variable`, `cyberark.isp.cyberark_credential` or `onepassword.connect.field_info`.
5. Set `no_log: true` on tasks that handle secret values, and check the job output for leakage.
6. Run a job against a non-production vault path, then switch the production credentials over and remove static copies of the secrets.

## Success Criteria

1. No plain-text secrets remain in Git, inventories, variables or survey defaults for the migrated jobs.
2. Jobs fetch secrets at launch and the vault audit log shows access by the automation identity.
3. Revoking the automation identity in the vault stops the jobs from retrieving secrets.
4. Job output and logs contain no secret values.

## Notes

- Prefer credential input sources for platform credentials, and direct lookups only when a playbook needs a value for its own use.
- `delinea.ss` and `akeyless.secrets_management` are certified collections; check their documentation for the plugins available in your version.
- Rotate the values themselves with [Rotate privileged credentials](rotate-privileged-credentials.md).
- Pair with Event-Driven Ansible by storing rulebook credentials in the same way; `ansible.eda.credential_input_source` exists for that purpose.
