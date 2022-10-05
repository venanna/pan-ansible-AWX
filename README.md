# pan-ansible-examples

[![N|Solid](./images/paloaltonetworks_logo.png)](https://www.paloaltonetworks.com/)

## `Overview`

The goal of this repository is to provide a simple "Hello World!" example of using Ansible with Palo Alto Networks firewalls.

All files related to Ansible are stored within the [ansible](./ansible/) directory at the root of this repository.

## 🚀 `Executing the playbook`

After [ensuring that your environment is setup properly](./docs/environment.md), change into the desired example within the `ansible` directory and execute the playbook with the following command:

```sh
ansible-playbook playbook.yaml
```

If you are using Ansible Vault to secure your secrets, then rename to `group_vars/all/vault.yaml.example` to `group_vars/all/vault.yaml` and make sure to [follow the guide](./docs/vault.md)!

## 📋 `Ansible version compatibility`

This module has been tested back to Ansible version 2.9

## ⚙️ `How it works`

A quick guide on what is happening with this playbook will be [posted here](./docs/howitworks.md)
