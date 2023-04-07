# Generate and Load Ansible Playbook

![Palo Alto Networks](../../../images/paloaltonetworks_logo.png)

This playbook automates the generation and loading of a full XML configuration for a Palo Alto Networks firewall using Jinja2 templates. The configuration is pushed to the firewall and loaded into the candidate configuration.

## Installation

Please follow the instructions in the [project's root README.md file](../../../README.md) to set up your environment using either Docker containers or a virtual environment.

## Customizing the Configuration

The configuration is generated based on the contents of the `host_vars` directory. Each YAML file within this directory contains settings that are used to build the configuration. Modify the files in this directory to customize the configuration for your firewall.

Example:

```yaml
# host_vars/dal-vfw-01/deviceconfig.yaml
---
deviceconfig:
  timezone: "US/Central"
  hostname: "{{ ansible_host }}"
  ip_address: "10.60.0.44"
  netmask: "255.255.0.0"
  gateway: "10.60.0.1"
  dns:
    primary: "10.30.0.50"
    secondary: "10.30.0.51"
  panorama:
    - type: "local-panorama"
      host: "hdq-pan-01.redtail.com"
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
        dal-vfw-01:
```

## Running the Playbook

To run the playbook, execute the following command:

```bash
ansible-playbook main.yaml
```

## How the Playbook Works

The playbook imports tasks from the roles directory and applies them sequentially:

1. The directories role creates local directories to hold configuration files.
2. The build_config role uses Jinja2 templates to generate the firewall configuration, piece by piece.
3. The assemble role assembles a full configuration from the parts created in the previous step.
4. The playbook uploads the full configuration to the firewall through the REST API.
5. The playbook loads the generated configuration into the candidate configuration on the firewall.

## Contributing

Please read [CONTRIBUTING.md](../../../CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

- **Calvin Remsburg (@cdot65)** - _Initial work_
