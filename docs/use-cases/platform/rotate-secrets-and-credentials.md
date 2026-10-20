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

## Prerequisites

1. The list of inventory and content repositories that hold vaulted variables, with write access for a service account, and a convention that vaulted files are named `vault_*.yml` (the default pattern of the role).
2. The current and the new vault passwords, held in a secret manager and passed to the job as credentials, never in the repository.
3. A branch protection and review process, so that the re-keyed files arrive as a pull request.
4. A current backup of the platform before rotating its own passwords or keys (see [Back up, restore and design HA and DR](back-up-restore-and-ha-dr.md)).
5. For platform rotation, SSH access to the platform hosts or cluster access to the namespace, and a maintenance window.

## Steps

1. Retrieve each inventory repository onto the execution node with `ansible.scm.git_retrieve`.
2. Run `infra.ansible_rekey_variables.rekey_variable` with `rekey_variable_inventory_repo_name` and `rekey_variable_new_vault_password` set, so every encrypted variable in the matching files is decrypted and re-encrypted with the new password. Keep `rekey_variable_secure_logging` enabled.
3. Push the result to a branch with `ansible.scm.git_publish` and open a pull request for review.
4. Update the vault credential used by the job templates with `ansible.controller.credential` at the moment the pull request is merged, so that jobs do not run with a mismatched password.
5. Run a canary job template against each repository and confirm that variables decrypt.
6. Rotate the platform's database and administrator passwords with `infra.aap_utilities.aap_password_rotate`, and the database encryption keys with `infra.aap_utilities.aap_secret_rotate`, first in a test environment.
7. Record the rotation date, the scope and the next due date, and retire the old vault passwords.

## Success Criteria

1. No vaulted file in the in-scope repositories can be decrypted with the old password.
2. All job templates that depend on the repositories complete with the new vault credential.
3. Platform database and administrator passwords have changed and all components are healthy.
4. The platform's encryption keys were rotated after a backup was taken, and encrypted fields such as credentials still work.
5. The rotation is a scheduled, repeatable job with an audit trail.

## Notes

- Rekeying rewrites many files. Do it from a clean branch, review only that the diff consists of vault blocks, and merge quickly to avoid conflicts.
- Password and key rotation are separate operations: passwords change authentication, keys change how stored fields are encrypted. Do them in separate windows.
- The platform rotation roles target recent releases and the containerized and operator deployments; check the role documentation for the supported versions before use.
- Prefer secret managers through credential input sources for the long term, so that fewer secrets need to be vaulted in files at all. See [Manage Automation Platform as code](manage-aap-as-code.md).
