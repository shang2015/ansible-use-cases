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

## Notes

- The playbook pattern also lets an Event-Driven Ansible rulebook trigger MCP-based steps, see [Build self-healing infrastructure from monitoring alerts](../event-driven/build-self-healing-infrastructure-from-monitoring-alerts.md).
- Treat tool arguments from an AI agent as untrusted input: validate them in the playbook.
- Check the Technology Preview support status before committing to production use.
