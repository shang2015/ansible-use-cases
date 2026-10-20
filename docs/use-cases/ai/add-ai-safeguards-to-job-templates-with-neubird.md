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

## Prerequisites

1. A NeuBird AI account and the connection details for the gateway.
2. Automation Platform with job templates for the actions an AI-driven investigation may propose, each described and tested.
3. An execution environment that includes the `neubird.aap` collection.
4. A safety classification for the job templates, such as read-only, low-risk change and high-risk change.

## Steps

1. Review the job templates and classify them by safety level, then name and describe them clearly so the AI service can choose correctly.
2. Add the `neubird.aap` collection to the execution environment and store the NeuBird connection details as a credential.
3. Configure the collection following its documentation, to apply the safety tags, supply the context and run pre-flight checks before execution.
4. Put high-risk templates behind a workflow with approval, and let low-risk or read-only templates run directly.
5. Turn on reporting and audit logging, and send job results back to NeuBird AI. Add notification templates so that people see what was run.
6. Where Event-Driven Ansible starts jobs, use the same templates so that both paths produce the same audit trail.
7. Review the audit records regularly and adjust the classification.

## Success Criteria

1. Every job template that AI can use has a safety level and a clear description.
2. Pre-flight checks block a run that does not meet its conditions.
3. Each AI-initiated job leaves an audit record with who or what asked, what ran and the result.
4. High-risk actions never run without a human approval.

## Notes

- The collection is certified and published by NeuBird AI. Details on its modules and roles are in its README.
- Use this together with [Call MCP server tools from playbooks](call-mcp-servers-from-playbooks.md) when agents reach automation through MCP.
- Start with read-only templates, then add change actions step by step.
