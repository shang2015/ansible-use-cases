---
title: Configure and serve models on RHEL AI
summary: Set up InstructLab, download models, serve them and test the endpoint with Red Hat AI collection content.
order: 40
personas: [AI platform engineer, Data scientist, Automation engineer]
collections: [redhat.ai, infra.ai]
key_content:
  - redhat.ai.ilab_init
  - redhat.ai.ilab_config
  - redhat.ai.ilab_model_download
  - redhat.ai.ilab_serve
  - redhat.ai.completion
  - redhat.ai.ilab
---

# Configure and serve models on RHEL AI

## Description

After the host exists, the AI software has to be configured and the model must be served. The automation initialises InstructLab, sets the configuration, downloads the model, starts the serving process and sends a test request, so every host is set up the same way and a failed host can be rebuilt without notes.

## Prerequisites

1. A RHEL AI host with GPUs, for example from [Provision infrastructure for Red Hat AI](provision-infrastructure-for-red-hat-ai.md).
2. Access to the model source, with the registry or token stored as a credential.
3. Agreed model names, serving parameters and the users or applications that will call the endpoint.

## Steps

1. Create the initial InstructLab configuration with `redhat.ai.ilab_init`.
2. Adjust settings such as serving parameters and paths with `redhat.ai.ilab_config`, using variables from inventory.
3. Download the required models with `redhat.ai.ilab_model_download`.
4. Serve the model with the `redhat.ai.ilab_serve` role, which runs it as a managed service. The `redhat.ai.ilab` playbook shows the full sequence.
5. Test the endpoint with `redhat.ai.completion` and a fixed prompt, and check the answer and the latency.
6. Put the playbook in a job template, and run it again after each model or configuration change.

## Success Criteria

1. The model is served from the host as a service and survives a restart.
2. `redhat.ai.completion` returns a valid response for the test prompt.
3. Two hosts built from the same inventory have identical configuration.

## Notes

- Use [Build execution environments with MCP servers](build-execution-environments-with-mcp-servers.md) and [Call MCP server tools from playbooks](call-mcp-servers-from-playbooks.md) for AI agent integrations.
- Limit access to the endpoint through the proxy created during provisioning.
