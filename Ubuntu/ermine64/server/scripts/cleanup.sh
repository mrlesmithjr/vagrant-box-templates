#!/bin/bash
vagrant destroy -f
# find . -type d -name "host_vars"
# find . -type d -name "host_vars" -exec rm -rf {} +
# find . -type d -name ".vagrant"
# find . -type d -name ".vagrant" -exec rm -rf {} +
find . -type f -name "*.retry"
find . -type f -name "*.retry" -exec rm {} +
find . -type f -name "*.vmdk"
find . -type f -name "*.vmdk" -exec rm {} +
