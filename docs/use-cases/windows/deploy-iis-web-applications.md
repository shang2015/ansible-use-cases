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

## Notes

- Read back current settings with the `*_info` modules, such as `microsoft.iis.website_info`, to audit existing servers before bringing them under management.
- Import certificates with `ansible.windows.win_certificate_store`. Site bindings, including host names and SNI, are set with the `bindings` option of `microsoft.iis.website`.
- Use [Distribute software to Windows hosts](distribute-software-to-windows-hosts.md) for application packages that are installers rather than file copies.
- Apply [Harden Windows](harden-windows.md) to the web servers after the application is configured.
