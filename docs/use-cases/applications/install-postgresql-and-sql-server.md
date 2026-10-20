---
title: Install PostgreSQL and SQL Server
summary: Install and configure PostgreSQL, EDB Postgres Advanced Server and Microsoft SQL Server on RHEL with certified content.
order: 70
personas: [Database administrator, Linux administrator]
collections: [redhat.rhel_system_roles, microsoft.sql, edb.epas_postgresql]
key_content:
  - redhat.rhel_system_roles.postgresql
  - microsoft.sql.server
---

# Install PostgreSQL and SQL Server

## Description

Database servers are delivered ready to use: the packages are installed, the service is configured and secured, and the basic settings follow the standard. The same job templates serve development, test and production.

## Prerequisites

1. RHEL hosts, correctly sized and with storage mounted for data, logs and backups.
2. Repository access and subscriptions for PostgreSQL, or the EDB and Microsoft repositories and licences where those products are used.
3. A database standard with port, memory settings, authentication method and TLS.
4. Credentials for the administrator accounts, stored in Automation Platform.

## Steps

1. Prepare the hosts, covering time sync, firewall rules, kernel settings and storage layout.
2. Install and configure PostgreSQL with the `redhat.rhel_system_roles.postgresql` role, which sets up the cluster and service.
3. Install and configure SQL Server with the `microsoft.sql.server` role, passing the edition, licence settings, ports and sa password through variables and credentials.
4. For EDB Postgres Advanced Server use the modules of the `edb.epas_postgresql` collection in the same job.
5. Create the application databases, users and roles, and apply the security baseline.
6. Run a connection test from an application host and capture the version and settings as a report.
7. Package the steps as job templates, with approvals for production.

## Success Criteria

1. The database service is running and enabled at boot on each host.
2. Applications connect with the agreed authentication and encryption.
3. Settings are the same as the standard on all servers of the same type.

## Notes

- MySQL and MariaDB are covered in [Configure MySQL and MariaDB databases and replication](configure-mysql-and-mariadb-databases.md).
- Use the SAP use cases for SAP HANA, see [Install SAP HANA and S/4HANA](install-sap-hana-and-s4hana.md).
- Take a backup before any change to a production database, and keep it outside the job host.
