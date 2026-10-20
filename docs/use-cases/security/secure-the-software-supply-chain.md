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

## Prerequisites

1. A RHEL host for each single-node service, sized according to the product documentation: Red Hat Trusted Artifact Signer (RHTAS) and Red Hat Trusted Profile Analyzer (RHTPA).
2. An OIDC identity provider for signer identities, and certificates for the service endpoints.
3. A CI/CD pipeline that builds images and can call the signing tools.
4. Red Hat Advanced Cluster Security for Kubernetes (RHACS) on the clusters that enforce policy.

## Steps

1. Deploy the signing service on a managed node with the `redhat.artifact_signer.tas_single_node` role, supplying the identity provider and certificate settings.
2. Deploy the SBOM and vulnerability analysis service with the `redhat.trusted_profile_analyzer.tpa_single_node` role.
3. Connect the registries and scanners to RHACS with `infra.rhacs_configuration.rhacs_image_integration`.
4. Register the signature verification setup in RHACS with `infra.rhacs_configuration.rhacs_signature`.
5. Define the admission and build-time policies, such as "image must be signed", with `infra.rhacs_configuration.rhacs_policy`.
6. Update the pipeline to sign images and publish SBOMs, and test with one signed and one unsigned image.
7. Move the policy from inform to enforce after the pilot teams have fixed their pipelines.

## Success Criteria

1. The signing and analysis services are running and reachable from the pipeline.
2. Images built by the pipeline are signed, and their SBOMs are available for query.
3. An unsigned image is flagged or blocked by the RHACS policy, according to the chosen mode.
4. The configuration of the services and policies can be rebuilt from Git.

## Notes

- The single-node roles suit evaluation and small environments; plan separately for production availability.
- Continue with [Configure RHACS as code](configure-rhacs-as-code.md) for the full policy and integration set.
- Use [Retrieve secrets from external vaults](retrieve-secrets-from-external-vaults.md) for registry and signing credentials.
