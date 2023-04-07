# DHCP Reservation Ansible Playbook

![Palo Alto Networks](../../../images/paloaltonetworks_logo.png)

This playbook automates the configuration of DHCP reservations for devices on your network using a Palo Alto Networks firewall. It simplifies the process of adding, removing, or updating DHCP reservations, making network management more efficient and less error-prone.

## Installation

Please follow the instructions in the [project's root README.md file](../../../README.md) to set up your environment using either Docker containers or a virtual environment.

## Customizing DHCP Reservations

You can customize the DHCP reservations by modifying the `group_vars/dhcp.yaml` file. This file contains a list of DHCP reservations with the following properties:

- `ip_address`: The reserved IP address for the device.
- `mac`: The MAC address of the device.
- `description`: A brief description of the device.
- `interface`: The interface on which the device is connected.
- `template`: The firewall template to be used.

Example:

    ```yaml
    dhcp_reservations:
    - ip_address: "192.168.101.20"
        mac: "00:50:56:11:20:44"
        description: "server20"
        interface: "ethernet1/2"
        template: "BranchFirewalls"
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

## How the Playbook Works

The playbook leverages the paloaltonetworks.panos Ansible collection to interact with the Palo Alto Networks firewall. The playbook.yaml file imports tasks from the tasks directory and applies them sequentially.

The main task, tasks/dhcp_reservations.yaml, iterates through the list of DHCP reservations specified in the group_vars/dhcp.yaml file. For each reservation, it uses the paloaltonetworks.panos.panos_config_element module to create an address object and configure the DHCP reservation on the firewall.

```yaml
- name: DHCP reservations
  paloaltonetworks.panos.panos_config_element:
    provider:
      ip_address: "{{ ansible_host }}"
      username: "{{ panorama_username }}"
      api_key: "{{ panorama_api_token }}"
    xpath: "/config/devices/entry[@name='localhost.localdomain']/template/entry[@name='{{ item.template }}']/config/devices/entry[@name='localhost.localdomain']/network/dhcp/interface/entry[@name='{{ item.interface }}']/server/reserved"
    element: |
      "<entry name='{{ item.ip_address }}'>
        <mac>{{ item.mac }}</mac>
        <description>{{ item.description }}</description>
      </entry>"
  loop: "{{ dhcp_reservations }}"
```

## Contributing

Please read [CONTRIBUTING.md](../../../CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

- **Calvin Remsburg (@cdot65)** - _Initial work_
