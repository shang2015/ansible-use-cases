---
title: Rotate vaulted secrets and platform credentials
summary: Re-key Ansible Vault variables across inventory repositories and rotate the platform's own database passwords and encryption keys.
order: 140
personas: [Platform engineer, Security engineer, Operations lead]
collections: [infra.ansible_rekey_variables, ansible.scm, ansible.controller, infra.aap_utilities]
key_content:
  - infra.ansible_rekey_variables.rekey_variable
  - ansible.scm.git_retrieve
  - ansible.scm.git_publish
  - ansible.controller.credential
  - infra.aap_utilities.aap_password_rotate
  - infra.aap_utilities.aap_secret_rotate
examples:
  - title: infra.ansible_rekey_variables validated collection
    url: https://github.com/redhat-cop/ansible_rekey_variables
    note: re-encrypts every vaulted variable under a new vault password
---

# Rotate vaulted secrets and platform credentials

## Description

Change the secrets that automation depends on on a schedule or after an incident, without hand-editing hundreds of files. Ansible re-encrypts every vaulted variable in the inventory repositories under a new vault password and updates the matching vault credential in the controller. The same approach rotates the platform's own database passwords and encryption keys.

## Notes

- Rekeying rewrites many files. Do it from a clean branch, review only that the diff consists of vault blocks, and merge quickly to avoid conflicts.
- Password and key rotation are separate operations: passwords change authentication, keys change how stored fields are encrypted. Do them in separate windows.
- The platform rotation roles target recent releases and the containerized and operator deployments; check the role documentation for the supported versions before use.
- Prefer secret managers through credential input sources for the long term, so that fewer secrets need to be vaulted in files at all. See [Manage Automation Platform as code](manage-aap-as-code.md).
