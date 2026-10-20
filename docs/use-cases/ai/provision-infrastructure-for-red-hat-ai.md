---
title: Provision infrastructure for Red Hat AI
summary: Create the cloud or bare-metal hosts that run Red Hat AI, and tear them down again, from playbooks.
order: 30
personas: [AI platform engineer, Infrastructure architect, Cloud engineer]
collections: [infra.ai, redhat.ai]
key_content:
  - infra.ai.aws_provision
  - infra.ai.azure_provision
  - infra.ai.gcp_provision
  - infra.ai.baremetal_provision
  - infra.ai.baremetal_iso
  - infra.ai.nginx_proxy
  - infra.ai.aws_teardown
---

# Provision infrastructure for Red Hat AI

## Description

GPU-enabled hosts for Red Hat AI are expensive and are often needed for short periods. The playbooks create the instances or bare-metal hosts, install the access proxy and remove everything when the work is done, so teams get an environment on request and do not pay for idle machines.

## Prerequisites

1. An account with GPU quota in the target cloud, or bare-metal servers with out-of-band access.
2. Red Hat AI subscriptions and access to the installation media or images.
3. Cloud credentials stored in Automation Platform, and network and security design for the new hosts.
4. The `infra.ai` collection is a validated collection, so check its README for the variables of each target.

## Steps

1. Choose the target and set the variables: instance type with GPUs, region, disk size, SSH keys and tags.
2. Provision on the cloud with `infra.ai.aws_provision`, `infra.ai.azure_provision` or `infra.ai.gcp_provision`.
3. For bare metal, build the automated installation ISO with the `infra.ai.baremetal_iso` role and provision the host with `infra.ai.baremetal_provision`.
4. Install the reverse proxy with TLS in front of the model endpoint using `infra.ai.nginx_proxy` or the `infra.ai.proxy` playbook.
5. Continue with the software set-up in [Configure and serve models on RHEL AI](configure-and-serve-models-on-rhel-ai.md).
6. Add tags with owner and expiry date, and schedule the teardown job.
7. Remove the resources with `infra.ai.aws_teardown`, `infra.ai.azure_teardown` or `infra.ai.gcp_teardown` when the work is finished.

## Success Criteria

1. A GPU host is created from a job template within the agreed time.
2. The access proxy answers over HTTPS with the expected certificate.
3. A teardown leaves no instances, disks or addresses behind.
4. Resource owners and expiry dates are visible in tags.

## Notes

- Self-signed certificates in the proxy role suit tests. Use certificates from your own CA for shared environments.
- Pair with the cloud use cases on tagging and cost hygiene.
