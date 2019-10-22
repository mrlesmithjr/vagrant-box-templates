#!/usr/bin/env bash

# Just a little script to prep a folder for a new environment
# This will eventually migrate to utils.py

LINKS=(".gitignore" "ansible.cfg" "scripts" "cleanup.bat"  \
"requirements.yml" "unit-test.sh" "Vagrantfile" "playbooks")

TOP_FOLDER_PATH="../../.."

for i in "${LINKS[@]}"
do
  if [ -d "$TOP_FOLDER_PATH/$i" ]; then
    if [ -d "./$i" ] && [ ! -L "./$i" ]; then
      rm -rf "./$i"
      ln -s "$TOP_FOLDER_PATH/$i" .
    elif [ ! -L "./$i" ]; then
      ln -s "$TOP_FOLDER_PATH/$i" .
    fi
  elif [ -f "$TOP_FOLDER_PATH/$i" ]; then
    if [ -f "./$i" ] && [ ! -L "./$i" ]; then
      rm "./$i"
      ln -s "$TOP_FOLDER_PATH/$i" .
    elif [ ! -L "./$i" ]; then
      ln -s "$TOP_FOLDER_PATH/$i" .
    fi
  fi
done

if [ -f ./hosts ] && [ ! -L ./hosts ]; then
  rm ./hosts
  ln -sf .vagrant/provisioners/ansible/inventory/vagrant_ansible_inventory ./hosts
elif [ ! -L ./hosts ]; then
  ln -sf .vagrant/provisioners/ansible/inventory/vagrant_ansible_inventory ./hosts
fi

if [ -d ./host_vars ] && [ ! -L ./host_vars ]; then
  rm -rf ./host_vars
  ln -sf .vagrant/provisioners/ansible/inventory/host_vars .
elif [ ! -L ./host_vars ]; then
  ln -sf .vagrant/provisioners/ansible/inventory/host_vars .
fi

if [ -d ./group_vars ] && [ ! -L ./group_vars ]; then
  rm -rf ./group_vars
  ln -sf .vagrant/provisioners/ansible/inventory/group_vars .
elif [ ! -L ./group_vars ]; then
  ln -sf .vagrant/provisioners/ansible/inventory/group_vars .
fi
