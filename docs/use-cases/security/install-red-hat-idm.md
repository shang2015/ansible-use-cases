---
title: Install Red Hat IdM servers, replicas and clients
summary: Deploy a Red Hat Identity Management domain with replicas and enrolled clients in a repeatable way.
order: 100
personas: [Identity engineer, Linux administrator, Security architect]
collections: [redhat.rhel_idm, infra.automation_development_office]
key_content:
  - redhat.rhel_idm.ipaserver
  - redhat.rhel_idm.ipareplica
  - redhat.rhel_idm.ipaclient
  - redhat.rhel_idm.ipadnszone
  - infra.automation_development_office.idm_server
  - infra.automation_development_office.idm_client
---

# Install Red Hat IdM servers, replicas and clients

## Description

Stand up Red Hat Identity Management as the central directory, Kerberos and certificate service for Linux. The first server, its replicas and every client are installed from the same inventory, so a new site or a rebuild takes a job run instead of a runbook.

## Prerequisites

1. RHEL hosts for the IdM servers, with fixed host names, forward and reverse DNS records, and synchronized time.
2. Planned realm and domain names, and a replica topology across sites.
3. Passwords for the directory manager and the IdM admin, stored as Automation Platform credentials or in a vault.
4. Network access between servers, replicas and clients for the IdM ports.
5. An inventory with groups for the first server, replicas and clients, as expected by the `redhat.rhel_idm` roles.

## Steps

1. Build the inventory groups `ipaserver`, `ipareplicas` and `ipaclients`, with the domain, realm and password variables.
2. Install the first server with the `redhat.rhel_idm.ipaserver` role, including integrated DNS when IdM manages DNS.
3. Add replicas with `redhat.rhel_idm.ipareplica` according to the planned topology.
4. Create the DNS zones and records needed with `redhat.rhel_idm.ipadnszone` and `redhat.rhel_idm.ipadnsrecord`.
5. Enroll Linux hosts with `redhat.rhel_idm.ipaclient`, through a job template that runs after provisioning.
6. As an alternative, use the validated roles `infra.automation_development_office.idm_server`, `idm_configure_replica` and `idm_client` that wrap the same process for the Automation Development Office reference environments.
7. Verify that Kerberos and LDAP lookups work from a client and that replication between servers is healthy.

## Success Criteria

1. The IdM servers and replicas are installed and replicate with each other.
2. Clients resolve users and groups from IdM and can obtain Kerberos tickets.
3. DNS records for IdM services resolve correctly from client networks.
4. A repeat run of the playbooks makes no changes on a healthy deployment.

## Notes

- Back up the IdM servers before upgrades or topology changes.
- Day-two administration is covered in [Manage users and access policy in IdM](manage-users-and-access-policy-in-idm.md); trusts to Active Directory in [Integrate Active Directory and single sign-on](integrate-active-directory-and-sso.md).
- Certificates issued by the IdM CA can be managed as described in [Manage the certificate lifecycle](manage-certificate-lifecycle.md).
