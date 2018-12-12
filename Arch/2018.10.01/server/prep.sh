#!/usr/bin/env bash

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