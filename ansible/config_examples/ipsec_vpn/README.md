# IPsec VPN Configuration Example

![Palo Alto Networks](../../../images/paloaltonetworks_logo.png)

This playbook automates the configuration of an IPsec VPN tunnel between two Palo Alto Networks firewalls. The configuration is pushed to the firewalls and loaded into the candidate configuration.

## Installation

Please follow the instructions in the [project's root README.md file](../../../README.md) to set up your environment using either Docker containers or a virtual environment.

## Customizing the Configuration

The configuration is generated based on the contents of the `host_vars` and `group_vars` directories for host-specific and group-specific variables, respectively. Each YAML file within this directory contains settings that are used to build the configuration. Modify the files in this directory to customize the configuration for your firewall.

Example:

```yaml
# host_vars/dal-vfw-01/address_objects.yaml
---
local_address_objects:
  - name: "WAN-IP-Prefix"
    address_type: "ip-netmask"
    value: "51.95.83.2/24"
    description: "Dallas WAN IP address and prefix"
    tag: ["WAN"]

  - name: "LAN-IP-Prefix"
    address_type: "ip-netmask"
    value: "10.255.2.1/24"
    description: "Dallas LAN IP address and prefix"
    tag: ["LAN"]

  - name: "DMZ-IP-Prefix"
    address_type: "ip-netmask"
    value: "192.168.2.1/24"
    description: "Dallas DMZ IP address and prefix"
    tag: ["DMZ"]

  - name: "SAN-DAL-Tunnel-IP-Prefix"
    address_type: "ip-netmask"
    value: "100.0.0.1/32"
    description: "San Antonio - Dallas VPN IP address and prefix"
    tag: ["VPN"]

  - name: "Default-Gateway"
    address_type: "ip-netmask"
    value: "51.95.83.1"
    description: "Default gateway for Dallas"
    tag: ["WAN"]
```

## Working with Ansible Vault

It's important to secure sensitive information such as API keys and usernames. This project uses Ansible Vault to encrypt the group_vars/vault.yaml file, which contains the Panorama username and API token.

This file does not ship with the project, but there is an example file that you can should edit and rename to create your own. To copy the example and encrypt the file, use the following command:

```bash
cp group_vars/vault.yaml.example group_vars/vault.yaml
ansible-vault encrypt group_vars/vault.yaml
```

You'll be prompted to enter a password. Make sure to remember this password, as you'll need it to decrypt the file or edit its contents. To edit the encrypted file, use:

```bash
ansible-vault edit group_vars/vault.yaml
```

To decrypt the file, use:

```bash
ansible-vault decrypt group_vars/vault.yaml
```

When running the playbook, you'll need to provide the vault password using the --ask-vault-pass flag:

```bash
ansible-playbook playbook.yaml --ask-vault-pass
```

## Inventory

The inventory.yaml file specifies the firewalls that the playbook will be applied to. You can add or remove firewalls from this file as needed.

Example:

```yaml
# inventory.yaml
all:
  children:
    firewalls:
      hosts:
        dallas-vfw-01:
        san-vfw-01:
    panorama:
      hosts:
        redtail:
          ansible_host: panorama.redtail.com
```

## Running the Playbook

To run the playbook, execute the following command:

```bash
ansible-playbook playbook.yaml
```

## How the Playbook Works

The playbook imports tasks from the roles directory and applies them sequentially:

1. **create_tags** - Creates tags on the firewall.
2. **create_address_objects** - Creates address objects on the firewall.
3. **create_interfaces** - Creates interfaces on the firewall.
4. **configure_vpn** - Configures the IPsec VPN tunnel on the firewall.
5. **configure_static_routes** - Configures static routes on the firewall.

## Contributing

Please read [CONTRIBUTING.md](../../../CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

- **Calvin Remsburg (@cdot65)** - _Initial work_
