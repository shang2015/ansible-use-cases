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

## Prerequisites

1. Credentials for each cloud in scope, stored in Automation Platform.
2. A defined service catalog: which sizes, regions, images and network patterns are allowed per cloud.
3. A decision on the provisioning layer per cloud, either Terraform or native Ansible modules.
4. An execution environment with the collections for each cloud and `cloud.terraform` if Terraform is used.

## Steps

1. Write a cloud-neutral request: service name, size class, environment and region group, mapped to cloud-specific values in a variables file.
2. Create one provisioning job per cloud, using `cloud.terraform.terraform` or the native modules (see the AWS, Azure and Google Cloud provisioning use cases).
3. Create a workflow with a survey for cloud choice, and branch on that choice to the right provisioning job.
4. Collect outputs with `cloud.terraform.tf_output` or the cloud inventory plugins `amazon.aws.aws_ec2`, `azure.azcollection.azure_rm` and `google.cloud.gcp_compute`.
5. Run one shared configuration job against all new hosts, covering hardening, agents, monitoring and patching.
6. Record the cloud, owner and request in the tags, labels and the ticket.

## Success Criteria

1. A service request produces a working, configured host on any supported cloud with no per-cloud manual work.
2. The configuration baseline is the same on every cloud, as shown by a post-provisioning check.
3. Hosts from all clouds appear in Automation Platform inventories with consistent group names.
4. Adding a region or size to the catalog is a variable change, not a workflow rewrite.

## Notes

- Keep the cloud-specific layer thin; differences in networking and identity are best handled in each provisioning job.
- Related: [Provision AWS networking and compute](../aws/provision-aws-networking-and-compute.md), [Provision Azure networking and virtual machines](../azure/provision-azure-networking-and-virtual-machines.md) and [Provision Google Cloud networking and compute](../gcp/provision-google-cloud-networking-and-compute.md).
- Enforce the tagging standard with [Enforce tagging and cost hygiene across clouds](enforce-tagging-and-cost-hygiene-across-clouds.md).
