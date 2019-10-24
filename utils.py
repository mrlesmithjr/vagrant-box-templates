#! /usr/bin/env python
"""Just a small little script to help manage Vagrant box templates in this repo."""

import argparse
# from datetime import datetime
import json
import logging
import os
import subprocess
import jinja2
# import shutil
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
        repo_facts = repo_info()
        print(json.dumps(repo_facts, indent=4))
    elif args.action == 'prep_environment':
        environments = parse_folders()
        prep_environments(environments)


def parse_folders():
    """Parse folders to find environment.yml"""
    environments = list()
    for root, _dirs, files in os.walk(SCRIPT_DIR):
        if root != os.path.join(SCRIPT_DIR, 'Test', 'dummy', 'server'):
            if 'environment.yml' in files:
                environment_yml = os.path.join(root, 'environment.yml')
                environments.append(environment_yml)
    return environments


def prep_environments(environments):
    """Load existing data from environment.yml then write new data."""
    for env_yaml in environments:
        logging.info('Processing: %s', env_yaml)
        with open(env_yaml, 'r') as stream:
            data = yaml.load(stream, Loader=yaml.FullLoader)
        environment_nodes = list()
        nodes = data.get('nodes')
        if nodes is not None:
            for node in nodes:
                node_info = dict(
                    ansible_groups=node.get('ansible_groups'),
                    box=node.get('box'),
                    desktop=node.get('desktop'),
                    disable_synced_folders=node.get('disable_synced_folders'),
                    disks=node.get('disks'),
                    interfaces=node.get('interfaces'),
                    linked_clone=node.get('linked_clone'),
                    manage_hostname=node.get('manage_hostname'),
                    mem=node.get('mem'),
                    name=node.get('name'),
                    port_forwards=node.get('port_forwards'),
                    provision=node.get('provision'),
                    provisioners=node.get('provisioners'),
                    synced_folder=node.get('synced_folder'),
                    vcpu=node.get('vcpu'),
                    windows=node.get('windows')
                )
                environment_nodes.append(node_info)

        environment = dict(
            nodes=environment_nodes,
            provisioners=data.get('provisioners'),
            synced_folders=data.get('synced_folders')
        )
        j2_env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(SCRIPT_DIR))
        j2_template = j2_env.get_template('environment.yml.j2')
        environment_config = j2_template.render(environment=environment)
        with open(env_yaml, 'w') as stream:
            stream.write(environment_config)
            stream.close()


# def prep_script_mgmt():
#     environment_yml = 'environment.yml'
#     prep_script = 'prep.sh'
#     for root, _dirs, files in os.walk(SCRIPT_DIR):
#         if root != os.path.join(SCRIPT_DIR, 'scripts'):
#             if environment_yml in files:
#                 if prep_script in files:
#                     script = os.path.join(root, prep_script)
#                     if not os.path.islink(script):
#                         subprocess.Popen(['git', 'rm', script])
#                 else:
#                     os.chdir(root)
#                     subprocess.Popen(['./scripts/prep.sh'])
#                     subprocess.Popen(['git', 'add', 'group_vars'])


def repo_info():
    """Collect important repo info and store as facts."""
    changed_files = list()
    repo_remotes = list()
    repo_path = os.getcwd()
    repo = git.Repo(repo_path)
    for item in repo.index.diff(None):
        changed_files.append(item.a_path)
    for item in repo.remotes:
        remote_info = dict()
        remote_info[item.name] = dict(url=item.url)
        repo_remotes.append(remote_info)
    repo_facts = dict(
        changed_files=changed_files,
        remotes=repo_remotes,
        untracked_files=repo.untracked_files
    )
    return repo_facts


if __name__ == '__main__':
    main()
