---
title: Deploy IIS web applications
summary: Install IIS and configure sites, application pools, applications and authentication consistently across web servers.
order: 40
personas: [Windows administrator, Application owner]
collections: [microsoft.iis, ansible.windows, infra.windows_ops]
key_content:
  - microsoft.iis.website
  - microsoft.iis.web_app_pool
  - microsoft.iis.web_application
  - microsoft.iis.virtual_directory
  - microsoft.iis.authentication
  - ansible.windows.win_feature
  - ansible.windows.win_uri
  - infra.windows_ops.windows_manage_iis
---

# Deploy IIS web applications

## Description

Build web servers that are identical in every environment. Ansible installs IIS, creates the application pools, sites and applications, sets authentication and publishes the application files, so a rebuilt or scaled-out server is ready without manual console work.

## Prerequisites

1. Windows Server hosts with WinRM access and an account with local administrator rights.
2. The application package or build output in an artifact repository reachable from the hosts or the execution environment.
3. TLS certificates and the service account for application pools, stored as automation controller credentials.
4. A definition of each site: name, bindings, physical path, pool identity and authentication method.

## Steps

1. Install the web server role and required features with `ansible.windows.win_feature`.
2. Create application pools with `microsoft.iis.web_app_pool`, setting pool attributes such as the managed pipeline mode, start mode and process identity.
3. Create sites with `microsoft.iis.website`, including bindings and the physical path. For a simple site, the `infra.windows_ops.windows_manage_iis` role creates a basic IIS server with a name, port and web root.
4. Add applications and virtual directories with `microsoft.iis.web_application` and `microsoft.iis.virtual_directory`.
5. Set authentication options for the site or application with `microsoft.iis.authentication`.
6. Copy or download the application content with `ansible.windows.win_copy` or `ansible.windows.win_get_url`, and open the firewall port with `ansible.windows.win_firewall_rule`.
7. Test the result with `ansible.windows.win_uri` against the site URL and fail the job on an unexpected response.
8. Run in a workflow behind the load balancer: take the server out, deploy, test, and put it back.

## Success Criteria

1. Every web server in the group has the same sites, pools, applications and authentication settings.
2. The test request to each site returns the expected status.
3. A new server built from the same job is serving traffic without manual steps.
4. Configuration changes are visible in Git and job history.

## Notes

- Read back current settings with the `*_info` modules, such as `microsoft.iis.website_info`, to audit existing servers before bringing them under management.
- Import certificates with `ansible.windows.win_certificate_store`. Site bindings, including host names and SNI, are set with the `bindings` option of `microsoft.iis.website`.
- Use [Distribute software to Windows hosts](distribute-software-to-windows-hosts.md) for application packages that are installers rather than file copies.
- Apply [Harden Windows](harden-windows.md) to the web servers after the application is configured.
