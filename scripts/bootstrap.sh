#!/bin/bash
# Alpine
if [ -f /etc/alpine-release ]; then
    sudo apk update && \
    sudo apk add python
fi

# Arch
if [ -f /etc/arch-release ]; then
    sudo pacman -Sy --noconfirm ca-certificates glibc libffi python \
    python-boto python-pyopenssl python-pip python-setuptools
fi

# Debian/Ubuntu
if [ -f /etc/debian_version ]; then
    test -e /usr/bin/python || (sudo apt-get update && sudo apt-get -y install python-minimal)
fi

# RHEL
if [ -f /etc/redhat-release ]; then
    if [ -f /etc/os-release ]; then
        os_name="$(awk -F= '/^NAME/{ print $2 }' /etc/os-release | sed 's/"//g')"
        os_version_id="$(awk -F= '/^VERSION_ID/{ print $2}' /etc/os-release | sed 's/"//g')"
        if [[ $os_name = "Fedora" ]]; then
            if [[ $os_version_id -le 21 ]]; then
                sudo yum -y update
                sudo yum -y install dnf
            fi
            sudo dnf -y install python-devel python-dnf
            sudo dnf -y groupinstall "Development Tools"
        else
            if [[ $os_version_id -lt 8 ]]; then
                sudo yum -y install python-devel
                sudo yum -y groupinstall "Development Tools"
            else
                sudo yum -y install platform-python-devel
                sudo yum -y groupinstall "Development Tools"
                test -e /usr/bin/python || (sudo yum -y install python3 && sudo alternatives --set python /usr/bin/python3)
           fi
        fi
    fi
fi
