---
title: Configure MySQL and MariaDB databases and replication
summary: Create databases, users and roles, tune settings and set up replication on MySQL and MariaDB servers.
order: 60
personas: [Database administrator, Application owner]
collections: [ansible.mysql, ansible.mariadb]
key_content:
  - ansible.mysql.mysql_db
  - ansible.mysql.mysql_user
  - ansible.mysql.mysql_role
  - ansible.mysql.mysql_variables
  - ansible.mysql.mysql_replication
  - ansible.mysql.mysql_info
  - ansible.mariadb.mariadb_db
  - ansible.mariadb.mariadb_replication
---

# Configure MySQL and MariaDB databases and replication

## Description

Database servers are configured with the same standard every time. The automation creates the schema, users and roles that an application needs, sets server variables and password policy, and builds replication between primary and replica servers.

## Notes

- For a rolling restart or upgrade of replicas see [Patch application nodes one at a time behind a load balancer](patch-application-nodes-behind-a-load-balancer.md).
- PostgreSQL and SQL Server are covered in [Install PostgreSQL and SQL Server](install-postgresql-and-sql-server.md).
