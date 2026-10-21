---
title: Deploy and operate a web application on AWS
summary: Stand up a web tier, load balancer and managed database on AWS and keep the stack consistent over time.
order: 20
personas: [Cloud engineer, Application owner, DevOps engineer]
collections: [cloud.aws_ops, amazon.aws]
key_content:
  - cloud.aws_ops.webapp.webapp
  - cloud.aws_ops.webapp.webapp_ha_aurora
  - cloud.aws_ops.webapp.migrate_webapp
  - cloud.aws_ops.deploy_flask_app
  - amazon.aws.elb_application_lb
  - amazon.aws.rds_instance
examples:
  - title: cloud.aws_ops validated collection
    url: https://github.com/ansible-collections/cloud.aws_ops
    note: includes the webapp playbooks
---

# Deploy and operate a web application on AWS

## Description

Deliver a complete web application, compute, load balancing and a database, on AWS as one automated workflow. Application teams get a repeatable way to create, update and move the stack, and operations teams get a known layout to support.

## Notes

- `cloud.aws_ops.create_rds_global_cluster` creates an Aurora global cluster across two regions for cross-region database resilience.
- Pair with [Back up and restore AWS resources](back-up-and-restore-aws-resources.md) so the database and volumes are protected from day one.
- Treat the sample Flask role as a pattern; replace it with the organization's own deployment role.
