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

## Prerequisites

1. A build host with `ansible-builder` and a container engine, and access to the container registry or private automation hub.
2. Network access to PyPI, npm or GitHub during the build, or internal mirrors.
3. A list of the MCP servers approved for use and their versions.
4. The `ansible.mcp_builder` collection is a Technology Preview collection, so test the image before use.

## Steps

1. Select the MCP servers that automation needs, for example AWS Core, AWS Cloud Control API, AWS IAM, AWS CDK, Azure or GitHub.
2. Add `ansible.mcp_builder` and `ansible.mcp` to the execution environment definition, together with the cloud collections the playbooks use.
3. Run the `ansible.mcp_builder.install_mcp` playbook, or the server roles, such as `ansible.mcp_builder.aws_ccapi_mcp`, `ansible.mcp_builder.azure_mcp` and `ansible.mcp_builder.github_mcp`, during the build. The `ansible.mcp_builder.common` role prepares the build environment.
4. Build the image, tag it with a version and test it with a playbook that lists the tools with `ansible.mcp.tools_info`.
5. Push the image to the registry and register it as an execution environment in Automation Platform.
6. Update the image on a schedule or when a server version changes, and re-run the tests.

## Success Criteria

1. The image builds from source control with no manual steps.
2. Each installed MCP server starts inside the image, and its tools can be listed.
3. Job templates use the image from the registry, with no extra installation at run time.

## Notes

- Call the servers from playbooks with [Call MCP server tools from playbooks](call-mcp-servers-from-playbooks.md).
- General guidance on image building is in the platform use case on execution environments.
- Pin versions, because MCP servers change quickly.
