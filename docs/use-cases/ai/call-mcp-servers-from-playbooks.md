---
title: Call MCP server tools from playbooks
summary: Use Model Context Protocol servers as governed building blocks inside Ansible playbooks and job templates.
order: 10
personas: [Automation engineer, Platform engineer, AI platform owner]
collections: [ansible.mcp, ansible.mcp_builder, ansible.controller]
key_content:
  - ansible.mcp.server_info
  - ansible.mcp.tools_info
  - ansible.mcp.run_tool
  - ansible.mcp.mcp
  - ansible.controller.job_template
---

# Call MCP server tools from playbooks

## Description

Model Context Protocol (MCP) servers offer tools for cloud services, code hosting and other systems in one standard way. Playbooks can call those tools as tasks, so MCP-based capabilities run under Automation Platform's credentials, approvals, logging and schedules, and not from an uncontrolled client.

## Prerequisites

1. An MCP server for the target system, either installed in the execution environment (see [Build execution environments with MCP servers](build-execution-environments-with-mcp-servers.md)) or reachable over the network.
2. The credentials that the MCP server needs, such as cloud or GitHub tokens, stored as Automation Platform credentials and injected as environment variables.
3. An automation controller or a local `ansible-navigator` set-up to test with. The `ansible.mcp` collection is a Technology Preview, so plan to test before relying on it for production work.
4. A reviewed list of the tools that automation is allowed to call.

## Steps

1. Configure the connection to the server with the `ansible.mcp.mcp` connection plugin, as described in the collection documentation.
2. Inspect the server with `ansible.mcp.server_info`, and list its tools with `ansible.mcp.tools_info`. Record the tool names and their input schema.
3. Call a tool with `ansible.mcp.run_tool`, passing arguments as variables. Register the result and check it with `assert` tasks.
4. Start from the demo playbooks in the collection, such as the ones for AWS Cloud Control API, Azure and GitHub, and adapt them.
5. Wrap the playbook in a job template, add a survey for inputs, and restrict who can launch it.
6. Add approvals in a workflow for tools that change or delete resources, and log the tool name and arguments in the job output.

## Success Criteria

1. A playbook lists the tools of the MCP server and calls one successfully.
2. Calls run with controller credentials, and secrets do not appear in job output.
3. Only approved tools are used, and changes are traceable to a job run.

## Notes

- The playbook pattern also lets an Event-Driven Ansible rulebook trigger MCP-based steps, see [Build self-healing infrastructure from monitoring alerts](../event-driven/build-self-healing-infrastructure-from-monitoring-alerts.md).
- Treat tool arguments from an AI agent as untrusted input: validate them in the playbook.
- Check the Technology Preview support status before committing to production use.
