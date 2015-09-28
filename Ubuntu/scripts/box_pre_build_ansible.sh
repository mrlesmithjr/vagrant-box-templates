#!/bin/bash

# Install Ansible to provision host
sudo apt-get install -y python-pip python-dev
sudo pip install ansible==1.9.1

# Run Ansible provisioning
ansible-playbook -i hosts box_pre_build.yml --connection=local --ask-sudo-pass

# Zero out the free space to save space in the final image:
sudo dd if=/dev/zero of=/EMPTY bs=1M
sudo rm -f /EMPTY

sleep 15s

cat /dev/null > ~/.bash_history && history -c && exit

sudo reboot
