#! /usr/bin/env python
"""Just a small little script to help manage Vagrant box templates in this repo."""

import argparse
# from datetime import datetime
import jinja2
import json
import logging
import os
# import shutil
import subprocess
# import time
# import requests
import yaml
import git

__author__ = "Larry Smith Jr."
__email__ = "mrlesmithjr@gmail.com"
__maintainer__ = "Larry Smith Jr."
__status__ = "Development"
# http://everythingshouldbevirtual.com
# @mrlesmithjr

logging.basicConfig(level=logging.INFO)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def main():
    """Main program execution."""
    args = parse_args()
    decide_action(args)
    # prep_script_mgmt()


def parse_args():
    """Parse CLI arguments."""
    parser = argparse.ArgumentParser(description="Vagrant box template utils.")
    parser.add_argument(
        "action", help="Define action to take.", choices=[
            'cleanup_builds', 'prep_environment', 'repo_info'])
    args = parser.parse_args()
    return args


def decide_action(args):
    """Make decision on what to do from arguments being passed."""
    if args.action == 'repo_info':
        repo_facts = dict()
        repo_info(repo_facts)
        print json.dumps(repo_facts, indent=4)
    elif args.action == 'prep_environment':
        parse_folders()


def parse_folders():
    for root, dirs, files in os.walk(SCRIPT_DIR):
        if root != os.path.join(SCRIPT_DIR, 'Test', 'dummy', 'server'):
            if 'environment.yml' in files:
                environment_yml = os.path.join(root, 'environment.yml')
                prep_environment(environment_yml)


def prep_environment(environment_yml):
    environment_dir = os.path.dirname(environment_yml)
    with open(environment_yml, 'r') as stream:
        data = yaml.load(stream)
        environment = dict()
        environment_nodes = []
        environment['provisioners'] = data.get('provisioners')
        environment['synced_folders'] = data.get('synced_folders')
        nodes = data.get('nodes')
        if nodes is not None:
            for node in nodes:
                node_info = dict()
                node_info['ansible_groups'] = node.get('ansible_groups')
                node_info['box'] = node.get('box')
                node_info['desktop'] = node.get('desktop')
                node_info['disks'] = node.get('disks')
                node_info['interfaces'] = node.get('interfaces')
                node_info['linked_clone'] = node.get('linked_clone')
                node_info['mem'] = node.get('mem')
                node_info['name'] = node.get('name')
                node_info['port_forwards'] = node.get('port_forwards')
                node_info['provision'] = node.get('provision')
                node_info['provisioners'] = node.get('provisioners')
                node_info['synced_folder'] = node.get('synced_folder')
                node_info['vcpu'] = node.get('vcpu')
                node_info['windows'] = node.get('windows')
                environment_nodes.append(node_info)

        environment['nodes'] = environment_nodes
        j2_env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(SCRIPT_DIR))
        j2_template = j2_env.get_template('environment.yml.j2')
        environment_config = j2_template.render(environment=environment)
        with open(os.path.join(environment_dir, 'environment.yml'), 'w') as f:
            f.write(environment_config)
            f.close()


def prep_script_mgmt():
    environment_yml = 'environment.yml'
    prep_script = 'prep.sh'
    prep_script_dir = os.path.join(SCRIPT_DIR, 'scripts')
    for root, dirs, files in os.walk(SCRIPT_DIR):
        if root != os.path.join(SCRIPT_DIR, 'scripts'):
            if environment_yml in files:
                if prep_script in files:
                    script = os.path.join(root, prep_script)
                    if not os.path.islink(script):
                        subprocess.Popen(['git', 'rm', script])
                else:
                    os.chdir(root)
                    subprocess.Popen(['./scripts/prep.sh'])
                    subprocess.Popen(['git', 'add', 'group_vars'])


def repo_info(repo_facts):
    """Collect important repo info and store as facts."""
    changed_files = []
    repo_remotes = []
    repo_path = os.getcwd()
    repo = git.Repo(repo_path)
    for item in repo.index.diff(None):
        changed_files.append(item.a_path)
    for item in repo.remotes:
        remote_info = dict()
        remote_info[item.name] = {"url": item.url}
        repo_remotes.append(remote_info)
    repo_facts['changed_files'] = changed_files
    repo_facts['remotes'] = repo_remotes
    repo_facts['untracked_files'] = repo.untracked_files


if __name__ == '__main__':
    main()
