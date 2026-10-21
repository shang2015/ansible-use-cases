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

## Notes

- Back up the IdM servers before upgrades or topology changes.
- Day-two administration is covered in [Manage users and access policy in IdM](manage-users-and-access-policy-in-idm.md); trusts to Active Directory in [Integrate Active Directory and single sign-on](integrate-active-directory-and-sso.md).
- Certificates issued by the IdM CA can be managed as described in [Manage the certificate lifecycle](manage-certificate-lifecycle.md).
