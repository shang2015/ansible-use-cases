---
title: Provision consistently across clouds
summary: Use one workflow, one set of variables and one configuration baseline to deliver the same service on AWS, Azure and Google Cloud.
order: 20
personas: [Cloud architect, Platform engineer]
collections: [cloud.terraform, amazon.aws, azure.azcollection, google.cloud]
key_content:
  - cloud.terraform.terraform
  - cloud.terraform.terraform_provider
  - cloud.terraform.tf_output
  - amazon.aws.aws_ec2
  - azure.azcollection.azure_rm
  - google.cloud.gcp_compute
---

# Provision consistently across clouds

## Description

Offer the same service, for example a hardened application server, on more than one public cloud without each cloud team writing its own process. A single request and workflow provisions on the chosen cloud, then applies the same configuration, so the result is identical regardless of provider.

## Notes

- Keep the cloud-specific layer thin; differences in networking and identity are best handled in each provisioning job.
- Related: [Provision AWS networking and compute](../aws/provision-aws-networking-and-compute.md), [Provision Azure networking and virtual machines](../azure/provision-azure-networking-and-virtual-machines.md) and [Provision Google Cloud networking and compute](../gcp/provision-google-cloud-networking-and-compute.md).
- Enforce the tagging standard with [Enforce tagging and cost hygiene across clouds](enforce-tagging-and-cost-hygiene-across-clouds.md).
