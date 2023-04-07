# Nautobot Integration Configuration Example

![Palo Alto Networks](../../../images/paloaltonetworks_logo.png)

This configuration example demonstrates how to use the [Nautobot](https://nautobot.readthedocs.io/en/latest/) API to dynamically generate configuration for a Palo Alto Networks firewall. The playbook uses the Nautobot API to retrieve information about the firewall, such as the IP address, hostname, and interfaces. It then uses this information to generate the configuration for the firewall.

## Installation

Please follow the instructions in the [project's root README.md file](../../../README.md) to set up your environment using either Docker containers or a virtual environment.

## Customizing the Configuration

The configuration is generated based on the contents of the `group_vars` directories for variables. Each YAML file within this directory contains settings that are used to connect to Nautobot to retrieve information about the configuration. Modify the files in this directory to customize the configuration for your Nautobot instance.

Example:

```yaml
# groups_vars/all/nautobot.yaml
---
nautobot:
    # the GitHub repo UUID from Nautobot
    git_repo: "9607d365-4867-4552-a057-a28754aa1f24"
    # the GraphQL UUID from Nautobot
    graphql_uuid: "61fb0080-a3a5-439d-8a06-ec8c63266f26"
    # API token
    token: "mynautobottoken"
    # Nautobot URL
    url: "nautobot.redtail.com:8080"
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
        aus-vfw-01:
        dal-vfw-01:
        dal-vfw-02:
        hou-vfw-01:
        hou-vfw-02:
        hdq-vfw-01:
        san-vfw-01:
```

## Running the Playbook

To run the playbook, execute the following command:

```bash
ansible-playbook playbook.yaml
```

## How the Playbook Works

The playbook imports tasks from the roles directory and applies them sequentially:

1. **nautobot** - Retrieves information about the firewall from Nautobot and stores it in the `nautobot` variable.
2. **firewall** - Generates the configuration for the firewall based on the information retrieved from Nautobot.

## Contributing

Please read [CONTRIBUTING.md](../../../CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

- **Calvin Remsburg (@cdot65)** - _Initial work_
