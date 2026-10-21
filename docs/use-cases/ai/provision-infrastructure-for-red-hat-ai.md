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

## Notes

- Self-signed certificates in the proxy role suit tests. Use certificates from your own CA for shared environments.
- Pair with the cloud use cases on tagging and cost hygiene.
