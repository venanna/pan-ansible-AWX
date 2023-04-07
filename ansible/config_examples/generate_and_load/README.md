# Configuration Generator and Loader Ansible Playbook

![Palo Alto Networks](../../../images/paloaltonetworks_logo.png)

This Ansible playbook automates the generation of a full XML configuration using Jinja2 templates for Palo Alto Networks firewalls. It then uploads the configuration to the firewall through the REST API and loads it into the candidate configuration.

## Installation

1. [Install Ansible](https://docs.ansible.com/ansible/latest/installation_guide/index.html) on your local machine.
2. Clone or download this repository to your local drive.
3. Update the `inventory.yaml` file with the appropriate information for your Palo Alto Networks firewall.
4. Update the variable files inside the `host_vars` directory with your specific configuration details.
5. Run `ansible-playbook configuration.yaml` inside this directory to execute the playbook.

## Customizing the Configuration

To customize the configuration, modify the variable files inside the `host_vars` directory. These files contain variables that will be used by the Jinja2 templates to generate the final XML configuration.

Here is a brief overview of some of the variable files:

- `vault.yaml`: Contains the API token for accessing the firewall's REST API.
- `deviceconfig.yaml`: Contains device configuration settings like timezone, hostname, IP address, netmask, gateway, DNS, and Panorama information.
- `network.yaml`: Contains network interface configuration.
- `paths.yaml`: Contains local paths for directories and files.
- `users.yaml`: Contains user accounts and their permissions.
- `vr.yaml`: Contains virtual router configuration settings.
- `vsys.yaml`: Contains virtual system configuration settings like zones, addresses, and interfaces.

Modify these files according to your requirements and then run the playbook to generate and load the configuration.

## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Author

This project was created by Calvin Remsburg.
