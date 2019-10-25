#! /usr/bin/env python
"""Just a small little script to help manage Vagrant box templates in this repo."""

import argparse
import json
import logging
import os
import re
import shutil
import jinja2
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
        repo_facts = repo_info()
        environments = parse_folders()
        prep_environments(repo_facts, environments)


def repo_info():
    """Collect important repo info and store as facts."""
    changed_files = list()
    entries = list()
    repo_remotes = list()
    repo_path = os.getcwd()
    repo = git.Repo(repo_path)
    for (path, _stage), _entry in repo.index.entries.items():
        entries.append(path)
    for item in repo.index.diff(None):
        changed_files.append(item.a_path)
    for item in repo.remotes:
        remote_info = dict()
        remote_info[item.name] = dict(url=item.url)
        repo_remotes.append(remote_info)
    repo_facts = dict(
        changed_files=changed_files,
        entries=entries,
        repo=repo,
        remotes=repo_remotes,
        untracked_files=repo.untracked_files,
        working_tree_dir=repo.working_tree_dir
    )
    return repo_facts


def parse_folders():
    """Parse folders to find environment.yml"""
    environments = list()
    for root, _dirs, files in os.walk(SCRIPT_DIR):
        if root != os.path.join(SCRIPT_DIR, 'Test', 'dummy', 'server'):
            if 'environment.yml' in files:
                environment_yml = os.path.join(root, 'environment.yml')
                environments.append(environment_yml)
    return environments


def prep_environments(repo_facts, environments):
    """Load existing data from environment.yml then write new data."""
    for env_yaml in environments:
        # logging.info('Processing: %s', env_yaml)

        cleanup_links(env_yaml, repo_facts)

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
                    disable_synced_folders=node.get(
                        'disable_synced_folders'),
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


def cleanup_links(env_yaml, repo_facts):
    """Cleans up environment symlinks to ensure consistency."""
    env_dir = os.path.dirname(env_yaml)

    repo = repo_facts['repo']

    cleanup_ansible_links(env_dir, repo, repo_facts)
    cleanup_linked_dirs(env_dir, repo, repo_facts)
    cleanup_linked_files(env_dir, repo, repo_facts)


def cleanup_ansible_links(env_dir, repo, repo_facts):
    """Cleanup Ansible related links."""

    # Defines Ansible links that should exist in environment directory
    ansible_links = dict(
        hosts='vagrant_ansible_inventory',
        host_vars='host_vars',
        group_vars='group_vars'
    )

    # Defines the Vagrant inventory directory which Ansible links should
    # reference
    vagrant_inventory_dir = os.path.join(
        '.vagrant', 'provisioners',
        'ansible', 'inventory')

    for key, value in ansible_links.items():
        dest = f'{env_dir}/{key}'.replace(
            f'{SCRIPT_DIR}/', '')
        src = os.path.join(vagrant_inventory_dir, value)
        if not os.path.islink(dest):
            if dest in repo_facts['entries']:
                repo.index.remove(dest, r=True)
            if os.path.isfile(dest):
                os.remove(dest)
            os.symlink(src, dest)
            repo.index.add(dest)


def cleanup_linked_dirs(env_dir, repo, repo_facts):
    """Cleanup linked directories."""

    # Defines directories that should be linked in environment directory
    linked_dirs = ['playbooks', 'scripts']

    for linked_dir in linked_dirs:
        dir_path = os.path.join(env_dir, linked_dir)
        if os.path.exists(dir_path):
            if not os.path.islink(dir_path):
                entry = f'{env_dir}/{linked_dir}'.replace(
                    f'{SCRIPT_DIR}/', '')
                entry_regex = re.compile(f'.*{entry}.*')
                if any(entry_regex.match(line) for line
                       in repo_facts['entries']):
                    repo.index.remove(entry, r=True)
                    if os.path.isdir(entry):
                        shutil.rmtree(entry)
                    os.symlink(os.path.join('..', '..', '..', linked_dir),
                               dir_path)
                    repo.index.add(entry)
        else:
            os.symlink(os.path.join('..', '..', '..', linked_dir),
                       dir_path)
            repo.index.add(entry)


def cleanup_linked_files(env_dir, repo, repo_facts):
    """Cleanup linked files."""

    # Defines files that should be linked in environment directory
    linked_files = ['.gitignore', 'ansible.cfg',
                    'cleanup.bat', 'requirements.yml', 'unit-test.sh',
                    'Vagrantfile']

    for linked_file in linked_files:
        file_path = os.path.join(env_dir, linked_file)
        if os.path.exists(file_path):
            if not os.path.islink(file_path):
                entry = f'{env_dir}/{linked_file}'.replace(
                    f'{SCRIPT_DIR}/', '')
                if entry in repo_facts['entries']:
                    repo.index.remove(entry)
                    os.remove(entry)
                os.symlink(os.path.join(
                    '..', '..', '..', linked_file), file_path)
                repo.index.add(entry)
        else:
            os.symlink(os.path.join(
                '..', '..', '..', linked_file), file_path)
            repo.index.add(entry)


if __name__ == '__main__':
    main()
