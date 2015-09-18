#!/bin/bash
apt-get install -y python-pip python-dev
pip install ansible==1.9.1

ansible-galaxy install mrlesmithjr.bootstrap
ansible-galaxy install mrlesmithjr.base
