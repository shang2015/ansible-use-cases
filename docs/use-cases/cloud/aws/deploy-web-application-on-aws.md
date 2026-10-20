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

## Prerequisites

1. An AWS credential in Automation Platform with rights for EC2, load balancing and RDS.
2. A VPC and subnets, or the [networking build](provision-aws-networking-and-compute.md) to create them.
3. The application code or package, and an agreed instance size, database engine and region.
4. An execution environment with `amazon.aws` and `cloud.aws_ops`.

## Steps

1. Review the `cloud.aws_ops.webapp.webapp` playbook as the reference deployment and copy it into a project, adjusting variables for the application.
2. Provision the web tier and load balancer, with `amazon.aws.elb_application_lb` where the layout needs changing.
3. Provision the database with `amazon.aws.rds_instance`, or use `cloud.aws_ops.webapp.webapp_ha_aurora` for a high availability Aurora cluster.
4. Deploy the application to the instances, for example with the `cloud.aws_ops.deploy_flask_app` role as a sample.
5. Publish the playbook as a job template and a workflow that runs build, deploy and smoke test.
6. Use `cloud.aws_ops.webapp.migrate_webapp` when the application has to move to another region.

## Success Criteria

1. The application answers requests through the load balancer address.
2. The database is reachable only from the application tier.
3. Re-running the workflow updates the stack without recreating healthy resources.
4. A documented, tested job exists for moving the application to another region.

## Notes

- `cloud.aws_ops.create_rds_global_cluster` creates an Aurora global cluster across two regions for cross-region database resilience.
- Pair with [Back up and restore AWS resources](back-up-and-restore-aws-resources.md) so the database and volumes are protected from day one.
- Treat the sample Flask role as a pattern; replace it with the organization's own deployment role.
