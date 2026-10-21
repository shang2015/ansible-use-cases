---
title: Add AI safeguards to job templates with NeuBird
summary: Connect job templates to NeuBird AI for context, pre-flight checks, safety tagging, reporting and audit logging.
order: 50
personas: [SRE, Operations lead, Automation architect]
collections: [neubird.aap, ansible.controller, ansible.eda]
key_content:
  - ansible.controller.job_template
  - ansible.controller.workflow_job_template
  - ansible.controller.notification_template
  - ansible.eda.rulebook_activation
---

# Add AI safeguards to job templates with NeuBird

## Description

AI-assisted operations only work if automation stays under control. The NeuBird AI gateway for Automation Platform makes job templates aware of the AI service: templates are tagged by safety level, given context before they run, checked before execution and reported on afterwards, with an audit trail.

## Notes

- The collection is certified and published by NeuBird AI. Details on its modules and roles are in its README.
- Use this together with [Call MCP server tools from playbooks](call-mcp-servers-from-playbooks.md) when agents reach automation through MCP.
- Start with read-only templates, then add change actions step by step.
