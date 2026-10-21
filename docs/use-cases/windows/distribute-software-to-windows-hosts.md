---
title: Distribute software to Windows hosts
summary: Install, upgrade and remove Windows software with Chocolatey, native installers or MECM deployments.
order: 50
personas: [Windows administrator, Endpoint management engineer]
collections: [chocolatey.chocolatey, ansible.windows, infra.windows_ops, microsoft.mecm]
key_content:
  - chocolatey.chocolatey.win_chocolatey
  - chocolatey.chocolatey.win_chocolatey_source
  - chocolatey.chocolatey.win_chocolatey_facts
  - ansible.windows.win_package
  - infra.windows_ops.windows_manage_packages
  - microsoft.mecm.application
  - microsoft.mecm.application_deployments
  - microsoft.mecm.device_collection
---

# Distribute software to Windows hosts

## Description

Deliver applications and agents to Windows servers and desktops with a defined version and a record of what is installed. Choose the method that fits the estate: Chocolatey for package-managed software, native MSI/EXE/MSIX installers for vendor packages, or MECM for devices that already use it as their software distribution system.

## Notes

- `windows_manage_packages` is described in its collection as a native replacement for Chocolatey-based package management without third-party dependencies, so choose it if Chocolatey is not already in use.
- For patches to Windows itself, use [Patch Windows servers](patch-windows-servers.md) or [Patch Windows with MECM](patch-windows-with-mecm.md).
- Download large installers from an internal source with `ansible.windows.win_get_url` or stage them on a distribution point, rather than fetching from the internet on every host.
- Web server software and application content are covered in [Deploy IIS web applications](deploy-iis-web-applications.md).
