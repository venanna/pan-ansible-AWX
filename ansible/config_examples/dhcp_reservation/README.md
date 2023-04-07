# DHCP Reservation Ansible Playbook

![Palo Alto Networks](../../../images/paloaltonetworks_logo.png)

This playbook automates the configuration of DHCP reservations for devices on your network using a Palo Alto Networks firewall. It simplifies the process of adding, removing, or updating DHCP reservations, making the network management more efficient and less error-prone.

## Installation

  1. [Install Ansible](https://docs.ansible.com/ansible/latest/installation_guide/index.html) on your local machine.
  2. Clone or download this repository to your local drive.
  3. Run `ansible-galaxy install -r requirements.yml` inside this directory to install the required Ansible roles.
  4. Update the `inventory.yaml` file with the appropriate information for your Palo Alto Networks firewall.
  5. Update the variable files inside the `group_vars` directory with your specific configuration details.
  6. Run `ansible-playbook playbook.yaml` inside this directory to execute the playbook.

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

Add or modify the entries in the dhcp_reservations list to suit your requirements, and then run the playbook to apply the changes.

## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Author

This project was created by Calvin Remsburg.
