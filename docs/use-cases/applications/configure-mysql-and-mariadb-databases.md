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

## Prerequisites

1. MySQL or MariaDB packages installed on the hosts, either from the operating system repositories or from an internal repository.
2. An administrative database account, stored as a credential, and network access from the execution environment.
3. The database standards: names, character sets, roles, password policy and replication layout.
4. Backups available before any change to a production server.

## Steps

1. Gather the current state with `ansible.mysql.mysql_info` or `ansible.mariadb.mariadb_info` and record it.
2. Create the databases with `ansible.mysql.mysql_db` or `ansible.mariadb.mariadb_db`, and import an initial dump if needed.
3. Create roles and users with `ansible.mysql.mysql_role` and `ansible.mysql.mysql_user` (or the `ansible.mariadb` modules), with privileges limited to what the application requires.
4. Set server variables, the password policy and TLS options with `ansible.mysql.mysql_variables`, `ansible.mysql.mysql_password_policy` and `ansible.mysql.mysql_tls`.
5. Configure replication on the replica with `ansible.mysql.mysql_replication` or `ansible.mariadb.mariadb_replication`, and check the replica status.
6. Enable slow query logging with `ansible.mysql.mysql_slow_log` where tuning is planned.
7. Run the job from a template with a survey for database and application names, and schedule drift checks.

## Success Criteria

1. Requested databases, roles and users exist with the agreed privileges.
2. Server variables match the standard on every server.
3. Replication reports healthy and lag is within the target.
4. Re-running the job makes no change.

## Notes

- For a rolling restart or upgrade of replicas see [Patch application nodes one at a time behind a load balancer](patch-application-nodes-behind-a-load-balancer.md).
- PostgreSQL and SQL Server are covered in [Install PostgreSQL and SQL Server](install-postgresql-and-sql-server.md).
