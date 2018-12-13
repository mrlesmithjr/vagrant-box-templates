#! /usr/bin/env python
"""Just a small little script to help manage Vagrant box templates in this repo."""

import argparse
# from datetime import datetime
import json
import logging
import os
# import shutil
import subprocess
# import time
# import requests
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


def parse_args():
    """Parse CLI arguments."""
    parser = argparse.ArgumentParser(description="Vagrant box template utils.")
    parser.add_argument(
        "action", help="Define action to take.", choices=[
            'cleanup_builds', 'repo_info'])
    args = parser.parse_args()
    return args


def decide_action(args):
    """Make decision on what to do from arguments being passed."""
    if args.action == 'repo_info':
        repo_facts = dict()
        repo_info(repo_facts)
        print json.dumps(repo_facts, indent=4)


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
