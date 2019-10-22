#!/usr/bin/env bash

set -e
# set -x

red="\033[0;31m"
reset="\033[0m"

timestamp=$(date +"%Y-%m-%d_%H-%M-%S")

UNIT_TEST_LOGFILE="logs/unit-test.log.$timestamp"

if [ ! -d logs ]; then
  mkdir logs 2>&1 | tee "$UNIT_TEST_LOGFILE"
fi

# Check provisioning settings and fail if not set to provision
for i in $(cat environment.yml|grep 'provision:'| awk -F'provision: ' '{ print $2 }'); do
  if [ "$i" != "true" ]; then
    printf "You must set ${red}'provision: true' ${reset}in environment.yml\n"
    printf "in order to do execute a proper unit test."
    exit
  fi
done

# Check ansible version
ansible --version 2>&1 | tee -a "$UNIT_TEST_LOGFILE"

printf "Running ansible-lint against playbooks/playbook.yml"
ansible-lint playbooks/playbook.yml 2>&1 | tee -a "$UNIT_TEST_LOGFILE"

# Spin up environment
vagrant up 2>&1 | tee -a "$UNIT_TEST_LOGFILE"

# Basic Ansible syntax check
ansible-playbook -i hosts playbooks/playbook.yml --syntax-check 2>&1 | tee -a "$UNIT_TEST_LOGFILE"

# Execute Ansible playbook again and check for idempotence
ansible-playbook -i hosts playbooks/playbook.yml \
| (grep -q 'changed=0.*failed=0' && (echo 'Idempotence test: pass' && exit 0) \
|| (echo 'Idempotence test: fail' && exit 1)) 2>&1 | tee -a "$UNIT_TEST_LOGFILE"

# Clean up Vagrant environment
./scripts/cleanup.sh 2>&1 | tee -a "$UNIT_TEST_LOGFILE"
