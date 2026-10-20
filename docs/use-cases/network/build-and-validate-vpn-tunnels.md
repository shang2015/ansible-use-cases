---
title: Build and validate VPN tunnels
summary: Create site-to-site VPN tunnels between on-premises devices and cloud gateways and verify that they are up.
order: 150
personas: [Network engineer, Cloud network engineer]
collections: [network.vpn, ansible.netcommon]
key_content:
  - network.vpn.deploy
  - network.vpn.validate
  - network.vpn.azure_rm_localnetworkgateway
  - network.vpn.azure_rm_virtualnetworkgatewayconnection
  - ansible.netcommon.net_ping
examples:
  - title: network.vpn validated collection
    url: https://github.com/redhat-cop/network.vpn
    note: build, maintain and validate VPN tunnels across cloud providers and network appliances
---

# Build and validate VPN tunnels

## Description

Connect a data center or branch to a cloud network with an IPsec VPN, and prove that it works. Both ends of the tunnel are configured from the same data, so peer addresses, pre-shared keys and routes cannot drift apart.

## Prerequisites

1. A cloud account with permission to create gateways and connections, and access to the on-premises VPN device.
2. Tunnel design: peer IP addresses, address ranges, IKE/IPsec parameters.
3. Pre-shared keys or certificates stored in Automation Platform credentials or an external vault.
4. A test host or address behind each end for end-to-end checks.

## Steps

1. Write the tunnel definition as data: local and remote gateways, address spaces and parameters.
2. Run the `network.vpn.deploy` role to read the VPN configuration and apply it to the network appliances.
3. Create the cloud side. For Azure, `network.vpn.azure_rm_localnetworkgateway` and `network.vpn.azure_rm_virtualnetworkgatewayconnection` define the on-premises gateway and the connection.
4. Run the `network.vpn.validate` role for the provider in use to check tunnel status.
5. Run a reachability test across the tunnel, for example with `ansible.netcommon.net_ping` from the on-premises device.
6. Schedule the validation, and attach the result to the change record.

## Success Criteria

1. The tunnel shows as connected on both the appliance and the cloud side.
2. Test traffic passes in both directions between the two address ranges.
3. Running the job again makes no changes.
4. The validation job can be run at any time and reports the current tunnel state.

## Notes

- Check the collection documentation for the providers and appliances supported by each role.
- Related: [Validate operational state and health checks](validate-operational-state-and-health-checks.md).
- Pair with Event-Driven Ansible to re-run validation, or open a ticket, when a tunnel-down alert arrives from monitoring.
