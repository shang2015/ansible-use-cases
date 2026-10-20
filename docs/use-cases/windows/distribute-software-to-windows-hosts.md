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

## Prerequisites

1. WinRM access to the target hosts with an administrator account stored as an automation controller credential.
2. A software source: an internal Chocolatey feed or file share, an artifact repository holding installers, or an MECM site with distribution points.
3. A list of approved applications with versions, silent install arguments and product IDs.
4. Licences or entitlements for commercial software.

## Steps

1. Pick the method per application. Use one method per application to avoid conflicting installs.
2. For Chocolatey, install it on the hosts, point it at the internal feed with `chocolatey.chocolatey.win_chocolatey_source`, and set options with `chocolatey.chocolatey.win_chocolatey_config` and `chocolatey.chocolatey.win_chocolatey_feature`.
3. Install, pin, upgrade or remove packages with `chocolatey.chocolatey.win_chocolatey`, giving a version for controlled rollouts.
4. For installers, use `ansible.windows.win_package` or the `infra.windows_ops.windows_manage_packages` role with the installer path or URL, `product_id`, arguments and expected return codes. Allow a reboot when the installer reports one is needed.
5. For MECM, create the application with `microsoft.mecm.application` and its deployment types, group target devices with `microsoft.mecm.device_collection`, distribute content with `microsoft.mecm.distribution_point_group` and deploy with `microsoft.mecm.application_deployments`.
6. Collect what is installed with `chocolatey.chocolatey.win_chocolatey_facts` and compare it with the approved list. Run `ansible.windows.win_package` in check mode to test installer-based applications.
7. Run the install job against a pilot group first, then widen it, and schedule a recurring compliance run that re-applies the approved versions.

## Success Criteria

1. Each in-scope host has the approved version of each application.
2. Installs are repeatable: a second run reports no change.
3. Hosts missing an application or running an old version are listed in the job output.
4. Removals of retired software are done by job, not by hand.

## Notes

- `windows_manage_packages` is described in its collection as a native replacement for Chocolatey-based package management without third-party dependencies, so choose it if Chocolatey is not already in use.
- For patches to Windows itself, use [Patch Windows servers](patch-windows-servers.md) or [Patch Windows with MECM](patch-windows-with-mecm.md).
- Download large installers from an internal source with `ansible.windows.win_get_url` or stage them on a distribution point, rather than fetching from the internet on every host.
- Web server software and application content are covered in [Deploy IIS web applications](deploy-iis-web-applications.md).
