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

## Notes

- Use [Build execution environments with MCP servers](build-execution-environments-with-mcp-servers.md) and [Call MCP server tools from playbooks](call-mcp-servers-from-playbooks.md) for AI agent integrations.
- Limit access to the endpoint through the proxy created during provisioning.
