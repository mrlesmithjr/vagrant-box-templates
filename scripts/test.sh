#!/usr/bin/env bash
set -e

if [ -f /etc/os-release ]; then
    os_name="$(awk -F= '/^NAME/{ print $2 }' /etc/os-release | sed 's/"//g')"
    os_version_id="$(awk -F= '/^VERSION_ID/{ print $2}' /etc/os-release | sed 's/"//g')"
    echo "$os_name"
    echo "$os_version_id"
fi