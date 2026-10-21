---
title: Secure the software supply chain
summary: Deploy Red Hat Trusted Artifact Signer and Trusted Profile Analyzer, and enforce signed images with RHACS.
order: 140
personas: [Platform engineer, DevSecOps engineer, Security architect]
collections: [redhat.artifact_signer, redhat.trusted_profile_analyzer, infra.rhacs_configuration]
key_content:
  - redhat.artifact_signer.tas_single_node
  - redhat.trusted_profile_analyzer.tpa_single_node
  - infra.rhacs_configuration.rhacs_signature
  - infra.rhacs_configuration.rhacs_policy
  - infra.rhacs_configuration.rhacs_image_integration
---

# Secure the software supply chain

## Description

Make it possible to prove where a container image or build artifact came from, what is inside it, and that only trusted artifacts run. Automation installs the signing and analysis services and sets the cluster policy that rejects unsigned or vulnerable content.

## Notes

- The single-node roles suit evaluation and small environments; plan separately for production availability.
- Continue with [Configure RHACS as code](configure-rhacs-as-code.md) for the full policy and integration set.
- Use [Retrieve secrets from external vaults](retrieve-secrets-from-external-vaults.md) for registry and signing credentials.
