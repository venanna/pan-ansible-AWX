"""Pseudo code for creating hundreds of security policies on PAN-OS.

Resulting policy will contain this format:

    rule_name: "rule_name"
    description: "description"
    source_zone: ["source_zone"]
    destination_zone: ["destination_zone"]
    source_ip: ["source_ip"]
    source_user: ["source_user"]
    destination_ip: ["destination_ip"]
    category: ["category"]
    application: ["application"]
    service: ["application-default"]
    tag_name: ["tag_name"]
    action: "action"
"""
import requests
import random
import ipdb

from panos.firewall import Firewall
from panos.policies import Rulebase, SecurityRule


INVENTORY = "dallas-vfw-01"
PAN_USER = "panofficehours"
PAN_PASS = "paloalto1!"


def pull_words():
    """Pull words from word list."""
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

    response = requests.get(word_site)
    WORDS = response.content.splitlines()

    cleanup = []
    for word in WORDS:
        cleanup.append(word.decode("utf-8"))

    return cleanup


def create_random_string(random_words):
    """Create random string."""
    x = random.sample(random_words, 3)
    rule_name = " ".join(x)

    x = random.sample(random_words, 10)
    description = " ".join(x)

    return rule_name, description


def main():
    """Main function."""
    fw = Firewall(INVENTORY, PAN_USER, PAN_PASS)
    rule_base = Rulebase()
    fw.add(rule_base)

    random_words = pull_words()

    i = 1
    while i < 200:
        rule_name, description = create_random_string(random_words)

        zones = ["DMZ", "LAN", "WAN"]

        source_zone = random.sample(zones, 1)
        destination_zone = random.sample(zones, 1)
        action = random.sample(["allow", "deny"], 1)

        new_rule = SecurityRule(
            name=rule_name,
            fromzone=source_zone,
            tozone=destination_zone,
            source=["any"],
            source_user=["any"],
            destination=["any"],
            application=["any"],
            service=["any"],
            category=["any"],
            action=action[0],
            description=description,
            tag=["Automation"],
        )
        rule_base.add(new_rule)
        new_rule.create()
        i += 1


if __name__ == "__main__":
    main()
