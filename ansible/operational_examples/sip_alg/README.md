# Disable SIP ALG

![Palo Alto Networks](../../../images/paloaltonetworks_logo.png)

This playbook automates the disabling of SIP ALG on a firewall. The configuration is pushed to the firewall and loaded into the candidate configuration.

## Installation

Please follow the instructions in the [project's root README.md file](../../../README.md) to set up your environment using either Docker containers or a virtual environment.

## Customizing the Configuration

The configuration is generated based on the contents of the `group_vars` directories for variables. The only YAML file here is used to store the Panorama username and API token. Modify the files in this directory to customize the configuration for your Panorama instance.

Example:

```yaml
---
panorama_username: "example_username"
panorama_api_token: "example_apitoken"
```

## Working with Ansible Vault

It's important to secure sensitive information such as API keys and usernames. This project uses Ansible Vault to encrypt the group_vars/vault.yaml file, which contains the Panorama username and API token.

This file does not ship with the project, but there is an example file that you can should edit and rename to create your own. To copy the example and encrypt the file, use the following command:

```bash
cp group_vars/vault.yaml.example group_vars/vault.yaml
ansible-vault encrypt group_vars/vault.yaml
```

You'll be prompted to enter a password. Make sure to remember this password, as you'll need it to decrypt the file or edit its contents. To edit the encrypted file, use:

```yaml
ansible-vault edit group_vars/vault.yaml
```

To decrypt the file, use:

```yaml
ansible-vault decrypt group_vars/vault.yaml
```

When running the playbook, you'll need to provide the vault password using the --ask-vault-pass flag:

```yaml
ansible-playbook playbook.yaml --ask-vault-pass
```

## Inventory

The inventory.yaml file specifies the Panorama instance that the playbook will be applied to. You can add or remove Panorama instances from this file as needed.

Example:

```yaml
# inventory.yaml
all:
  children:
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

The playbook runs the following tasks:

1. **Disable SIP ALG** - Disables SIP ALG on the firewall.

## Contributing

Please read [CONTRIBUTING.md](../../../CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

- **Calvin Remsburg (@cdot65)** - _Initial work_
