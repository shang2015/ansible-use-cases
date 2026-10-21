---
title: Build execution environments with MCP servers
summary: Install MCP servers for AWS, Azure and GitHub into execution environments so playbooks can use them in Automation Platform.
order: 20
personas: [Platform engineer, Automation engineer]
collections: [ansible.mcp_builder, ansible.mcp]
key_content:
  - ansible.mcp_builder.install_mcp
  - ansible.mcp_builder.common
  - ansible.mcp_builder.aws_core_mcp
  - ansible.mcp_builder.aws_ccapi_mcp
  - ansible.mcp_builder.azure_mcp
  - ansible.mcp_builder.github_mcp
---

# Build execution environments with MCP servers

## Description

MCP servers need a defined runtime: Python or Node packages, binaries and configuration. Building them into an execution environment gives automation a tested, versioned image that runs the same on a laptop and on the automation controller.

## Notes

- Call the servers from playbooks with [Call MCP server tools from playbooks](call-mcp-servers-from-playbooks.md).
- General guidance on image building is in the platform use case on execution environments.
- Pin versions, because MCP servers change quickly.
