<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Vagrant Box Templates](#vagrant-box-templates)
  - [Purpose](#purpose)
  - [Requirements](#requirements)
    - [Software](#software)
    - [Alpine box requirements](#alpine-box-requirements)
      - [`vagrant-alpine` plugin](#vagrant-alpine-plugin)
      - [`/vagrant` synced_folder](#vagrant-synced_folder)
      - [Setting up `sudoers`](#setting-up-sudoers)
        - [`OS X`](#os-x)
        - [`Ubuntu`](#ubuntu)
        - [`Fedora`](#fedora)
  - [Included Box Distros](#included-box-distros)
  - [Useful information](#useful-information)
    - [Building Vagrant Boxes](#building-vagrant-boxes)
    - [Vagrantfile](#vagrantfile)
    - [File structure](#file-structure)
    - [Working on different projects](#working-on-different-projects)
      - [Create development environment](#create-development-environment)
      - [Create project development environment](#create-project-development-environment)
      - [Keeping development environment up to date with this repo](#keeping-development-environment-up-to-date-with-this-repo)
    - [Using Docker containers](#using-docker-containers)
  - [Usage](#usage)
    - [Getting started](#getting-started)
      - [Clone repo](#clone-repo)
      - [Choose distro](#choose-distro)
      - [Customizing environment](#customizing-environment)
        - [Nested Virtualization](#nested-virtualization)
        - [Disks, interfaces, and port_forwards](#disks-interfaces-and-port_forwards)
        - [Provisioning](#provisioning)
        - [Linked Clones](#linked-clones)
      - [Spinning up environment](#spinning-up-environment)
        - [Example `Ubuntu Trusty` environment](#example-ubuntu-trusty-environment)
      - [Tearing down environment](#tearing-down-environment)
      - [Unit tests](#unit-tests)
        - [Executing unit tests](#executing-unit-tests)
        - [Example unit test results](#example-unit-test-results)
    - [Learning Ansible](#learning-ansible)
      - [Ansible Groups](#ansible-groups)
      - [Ansible playbooks](#ansible-playbooks)
      - [Ansible `requirements.yml`](#ansible-requirementsyml)
        - [Installing Ansible roles](#installing-ansible-roles)
          - [Global Ansible roles installation](#global-ansible-roles-installation)
          - [Non-Global Ansible roles installation](#non-global-ansible-roles-installation)
          - [Using existing folder of Ansible roles](#using-existing-folder-of-ansible-roles)
  - [License](#license)
  - [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Vagrant Box Templates

## Purpose

Spin up different OS types using [Vagrant](https://www.vagrantup.com) and learn
[Ansible](https://www.ansible.com) at the same time if desired. Some distros
also include `Desktop` versions.

## Requirements

### Software

- [Ansible](https://www.ansible.com)
- [Vagrant](https://www.vagrantup.com)
- [Virtualbox](https://www.virtualbox.org)

### [Alpine](https://alpinelinux.org/) box requirements

#### `vagrant-alpine` plugin

> NOTE: **require** the `vagrant-alpine` plugin to be installed

```bash
vagrant plugin install vagrant-alpine
```

#### `/vagrant` synced_folder

> NOTE: `NFS` is used for the `/vagrant` synced_folder.
> This means you will be prompted for `sudo` password when spinning up a box.
> This can be changed to not prompt by references
> [here](https://www.vagrantup.com/docs/synced-folders/nfs.html)

#### Setting up `sudoers`

##### `OS X`

To setup `sudoers` for `OSX` add the following using `visudo`

```bash
Cmnd_Alias VAGRANT_EXPORTS_ADD = /usr/bin/tee -a /etc/exports
Cmnd_Alias VAGRANT_NFSD = /sbin/nfsd restart
Cmnd_Alias VAGRANT_EXPORTS_REMOVE = /usr/bin/sed -E -e /*/ d -ibak /etc/exports
%admin ALL=(root) NOPASSWD: VAGRANT_EXPORTS_ADD, VAGRANT_NFSD, VAGRANT_EXPORTS_REMOVE
```

##### `Ubuntu`

To setup `sudoers` for `Ubuntu` add the following using `visudo`

```bash
Cmnd_Alias VAGRANT_EXPORTS_CHOWN = /bin/chown 0\:0 /tmp/*
Cmnd_Alias VAGRANT_EXPORTS_MV = /bin/mv -f /tmp/* /etc/exports
Cmnd_Alias VAGRANT_NFSD_CHECK = /etc/init.d/nfs-kernel-server status
Cmnd_Alias VAGRANT_NFSD_START = /etc/init.d/nfs-kernel-server start
Cmnd_Alias VAGRANT_NFSD_APPLY = /usr/sbin/exportfs -ar
%sudo ALL=(root) NOPASSWD: VAGRANT_EXPORTS_CHOWN, VAGRANT_EXPORTS_MV, VAGRANT_NFSD_CHECK, VAGRANT_NFSD_START, VAGRANT_NFSD_APPLY
```

##### `Fedora`

To setup `sudoers` for `Fedora` add the following using `visudo`

> Note: Given your user belongs to the vagrant group

```bash
Cmnd_Alias VAGRANT_EXPORTS_CHOWN = /bin/chown 0\:0 /tmp/*
Cmnd_Alias VAGRANT_EXPORTS_MV = /bin/mv -f /tmp/* /etc/exports
Cmnd_Alias VAGRANT_NFSD_CHECK = /usr/bin/systemctl status --no-pager nfs-server.service
Cmnd_Alias VAGRANT_NFSD_START = /usr/bin/systemctl start nfs-server.service
Cmnd_Alias VAGRANT_NFSD_APPLY = /usr/sbin/exportfs -ar
%vagrant ALL=(root) NOPASSWD: VAGRANT_EXPORTS_CHOWN, VAGRANT_EXPORTS_MV, VAGRANT_NFSD_CHECK, VAGRANT_NFSD_START, VAGRANT_NFSD_APPLY
```

## Included Box Distros

> NOTE: This list may not be completely up to date.

Below are the included distros along with their respective releases that are
available in this repo.

| Distro             | Releases                                                                                          |
| ------------------ | ------------------------------------------------------------------------------------------------- |
| `Alpine`           | `3.7`, `3.8`, `3.9`                                                                               |
| `Arch`             | `N/A`                                                                                             |
| `CentOS`           | `5`, `6`, `7`                                                                                     |
| `Debian`           | `7`, `8`, `9`                                                                                     |
| `Fedora`           | `21`, `22`, `23`, `24`, `25`, `26`, `27`, `28`, `29`, `30`                                        |
| `FreeNAS`          | `11.2`                                                                                            |
| `LinuxMint`        | `18`, `19`                                                                                        |
| `openSUSE`         | `15.0`, `15.1`, `42.2`, `42.3`                                                                    |
| `Oracle Linux`     | `7`                                                                                               |
| `Scientific-Linux` | `7`                                                                                               |
| `Ubuntu`           | `12.04`, `14.04`, `15.04`, `15.10`, `16.04`, `16.10`, `17.04`, `17.10`, `18.04`, `18.10`, `19.04` |
| `VyOS`             | `1.1.8`                                                                                           |
| `Windows`          | `10`, `2008 R2`, `2012 R2`, `2016`, `2019`                                                        |

## Useful information

### Building Vagrant Boxes

My process for building and keeping the majority of these boxes up to date is
by using [Packer](https://www.packer.io). I also maintain a
[Packer Templates](https://github.com/mrlesmithjr/packer-templates) repository
which contains all of the relevant information on how build and test new boxes.

### Vagrantfile

A single [Vagrantfile](./Vagrantfile) is used for all distros to use. This helps
keeping changes to a minimum (Very seldom needed). The reason behind this is
that I have spent close to two years trying to come up with a single `Vagrantfile`
that would fit most any scenario that I have a use case for during development.
Many of these scenarios involve multinode clustering, routing, loadbalancing,
ZFS, GlusterFS, Docker Swarm, Kubernetes, ELK Stack, and so on. Not to say that
a specific use case may not present itself that would require a change to
the `Vagrantfile` but those are far in between.

[Vagrantfile](Vagrantfile)

### File structure

Most files are symlinks from each distro folder into the repo root to keep a
consistent and easy method of changing things around.
Feel free to change as needed.

### Working on different projects

One trick that I use daily with these templates is to working on many different
projects and not ever need to change out of my single folder. What I mean by this
is that I can stay within a single folder and easily switch between projects by
using `GIT` branches for each project.

#### Create development environment

1. Clone this repo

```bash
cd ~
mkdir -p projects/vagrant
cd projects/vagrant
git clone https://github.com/mrlesmithjr/vagrant-box-templates
```

2. Remove the `origin` remote

```bash
cd vagrant-box-templates
git remote remove origin
```

3. Add this repo as the `upstream` remote

```bash
git remote add upstream https://github.com/mrlesmithjr/vagrant-box-templates.git
git fetch upstream master
```

At this point you now are on your local `master` branch with a remote called
`upstream`.

#### Create project development environment

I never do any work in `master` to keep this nice and untouched. So when I need
to work on a project I simply do the following:

```bash
git checkout master
git checkout -b projectname
```

I then define my environment, Ansible groups, Ansible roles, and Ansible
playbooks for the specific project. I then do all of my testing and development,
and when I am finished, I simply add all of the new/changed files and commit them
only locally. Then the next time I need a new environment I follow this same
process by going back to `master` and checking out another branch for developing
in.

> NOTE: You could definitely add another GIT remote and keep your projects
> (branches) synced.

Example of what my current environment looks like after cleaning it up a bit
not long ago.

```bash
  dev/alpine-docker
  dev/apache2
  dev/bird
  dev/bro-ids
  dev/cacti
  dev/ceph
  dev/config-interfaces
  dev/dnsmasq
  dev/docker
  dev/dumb-init
  dev/elasticsearch
  dev/eve-ng
  dev/fluentd
  dev/gerrit
  dev/graylog
  dev/influxdb
  dev/k8s
  dev/kea-dhcp
  dev/kvm
  dev/landscape
  dev/letsencrypt
  dev/lvm
  dev/monit
  dev/motd
  dev/mysql
  dev/netdata
  dev/pdns
  dev/postgres
  dev/prometheus-grafana-docker
  dev/rabbitmq
  dev/sensu
  dev/spinnaker
  dev/squid-haproxy-keepalived
  dev/stackstorm
  dev/syslog-ng
  dev/testing-roles
  dev/tripwire
  dev/unbound
  dev/vault-consul
  dev/vault-consul-docker
  dev/vault-consul-docker-monitoring
  dev/zabbix
  issue-#9
* master
  play/linuxmint
  play/zesty-desktop
  test/uname
  testing/consul
```

#### Keeping development environment up to date with this repo

In order to keep my development environment synced up with any changes from this
repo all I have to do is:

```bash
git checkout master
git fetch upstream master
git pull --rebase upstream master
```

And now if I want to pull any important changes into any existing projects I
simply have to only do:

```bash
git checkout projectname
git rebase master
```

### Using Docker containers

You may also be interested in using [Docker](https://www.docker.com) containers
to perform similar testing scenarios as we are doing here. We can still use
[Vagrant](https://www.vagrantup.com) and [Ansible](https://www.ansible.com) as
we do here but we replace [Virtualbox](https://www.virtualbox.org) with
[Docker](https://www.docker.com) as our provider. This definitely keeps things
slimmed down a bit but does limit some of our testing scenarios. However, if you
are interested in this you can also checkout my [vagrant-container-templates](https://github.com/mrlesmithjr/vagrant-container-templates)
repo for more info on that.

## Usage

### Getting started

#### Clone repo

```bash
git clone https://github.com/mrlesmithjr/vagrant-box-templates
cd vagrant-box-templates
```

#### Choose distro

Find the OS of your choice and spin up a node or more.

#### Customizing environment

Each distro folder contains a `environment.yml` file which you can change the
number of nodes to spin up if desired.

For examples of possible settings checkout the following test environment:
[Test/dummy/server/environment.yml](Test/dummy/server/environment.yml)

##### Nested Virtualization

You can enable nested virtualization by defining/modifying the `nested_virtualization`
parameter in a node definition. This currently **ONLY** works on VMware boxes.

##### Disks, interfaces, and port_forwards

If you would like to change `disks|interfaces|port_forwards` feel free to
uncomment those sections and adjust them as needed.

##### Provisioning

If you would like to provision the nodes when they startup you will need to
set `provision: true` in the `environment.yml`. Also if the box that is to be
spun up is Windows based then set `windows: true` in order for provisioning
specific to Windows to occur.

By default the following provisioning will occur:

- [scripts/bootstrap.sh](scripts/bootstrap.sh)
- [pre_host_vars.yml](playbooks/prep_host_vars.yml)
- [bootstrap.yml](playbooks/bootstrap.yml)
- [playbook.yml](playbooks/playbook.yml)

You may also define custom provisioners either globally or per node to be
executed during provisioning.

To define global provisioners, simply edit the `environment.yml` file and use
the following as an example:

```yaml
# Global provisioners
provisioners:
  - type: shell
    inline: |
      if [ -f /etc/os-release ]; then
          os_name="$(awk -F= '/^NAME/{ print $2 }' /etc/os-release | sed 's/"//g')"
          os_version_id="$(awk -F= '/^VERSION_ID/{ print $2}' /etc/os-release | sed 's/"//g')"
          echo $os_name
          echo $os_version_id
      fi
    privileged: true
  # - type: shell
  #   path:
  #     - scripts/test.sh
  #   privileged: false
  # - type: ansible
  #   playbooks:
  #     - test.yml
```

When it comes to per node provisioning, currently only `scripts` and `ansible_local` are supported.
Ansible playbook provisioners are easy enough to define which nodes should be
executed against already.

To define per node provisioners, use the below as an example to use within the
`environment.yml` file:

```yaml
nodes:
  - name: node0
    ansible_groups:
      - test_nodes
    box: mrlesmithjr/bionic64
    desktop: false
    disks: []
    interfaces: []
    linked_clone: true
    mem: 512
    provision: true
    # Node specific provisioners
    provisioners:
      # - type: shell
      #   inline: |
      #       if [ -f /etc/os-release ]; then
      #           os_name="$(awk -F= '/^NAME/{ print $2 }' /etc/os-release | sed 's/"//g')"
      #           os_version_id="$(awk -F= '/^VERSION_ID/{ print $2}' /etc/os-release | sed 's/"//g')"
      #           echo $os_name
      #           echo $os_version_id
      #       fi
      #   privileged: true
      - type: shell
        path:
          - scripts/test.sh
        privileged: false
    vcpu: 1
    port_forwards: []
    windows: false
```

##### Linked Clones

By default, all VMs are configured to be spun up as linked clones. This is the
default to keep disk space to a minimum. You can easily change a VM to either
be a linked clone or not by changing or adding the `linked_clone: true` or
`linked_clone: false` to the `environment.yml` file in the respective distro folder:

#### Spinning up environment

When you are ready to spin up your environment simply:

```bash
vagrant up
```

##### Example `Ubuntu Trusty` environment

For example if I want to spin up a Ubuntu Trusty server node:

```bash
cd vagrant-box-templates/Ubuntu/trusty64/server
vagrant up
vagrant ssh
```

#### Tearing down environment

When you are all done with your [Vagrant](https://www.vagrantup.com) environment
you can quickly and cleanly tear it all down:

`Non-Windows`:

```bash
    ./scripts/cleanup.sh
```

`Windows`:

```bat
    cleanup.bat
```

#### Unit tests

If you are interested in using these templates for unit testing I have included
a beginning [script](./unit-test.sh) which can be used for spinning up a box or
boxes to conduct unit testing. The current main focus on this is to spin up the
boxes, provision them based on the roles defined in `playbook.yml`, test
idempotency and then tear everything down. This script will create a `logs`
directory which will contain all of the output collected from the unit test. This
is not perfect at this time but it does work fairly well for basic testing. I
will be adding more functionality over time and definitely welcome feedback.

##### Executing unit tests

In order to effectively conduct a unit test all you need to do is adjust the
`environment.yml` file and define your nodes, ensure `provision: true` is defined,
define the roles in `playbook.yml` and then:

```bash
./unit-test.sh
```

And then let the script do all of the work and record the results.

##### Example unit test results

Below is an example output from a unit test:

```raw
ansible 2.3.1.0
  config file = /Users/larry/projects/vagrant/vagrant-box-templates/Ubuntu/xenial64/server/ansible.cfg
  configured module search path = Default w/o overrides
  python version = 2.7.13 (default, Apr  4 2017, 08:47:57) [GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.38)]
ANSIBLE0013 Use shell only when shell functionality is required
/Users/larry/Git_Projects/GitHub/mrlesmithjr/ansible-base/handlers/main.yml:3
Task/Handler: update resolvconf

 [WARNING]: Host file not found: /etc/ansible/hosts
 [WARNING]: provided hosts list is empty, only localhost is available

playbook: playbook.yml
Bringing machine 'node0' up with 'virtualbox' provider...
==> node0: Importing base box 'mrlesmithjr/xenial64'...

[KProgress: 10%
[KProgress: 20%
[KProgress: 30%
[KProgress: 40%
[KProgress: 50%
[KProgress: 60%
[KProgress: 70%
[KProgress: 80%
[KProgress: 90%
[K==> node0: Matching MAC address for NAT networking...
==> node0: Checking if box 'mrlesmithjr/xenial64' is up to date...
==> node0: Setting the name of the VM: server_node0_1498705353100_6863
==> node0: Clearing any previously set network interfaces...
==> node0: Preparing network interfaces based on configuration...
    node0: Adapter 1: nat
    node0: Adapter 2: hostonly
==> node0: Forwarding ports...
    node0: 22 (guest) => 2222 (host) (adapter 1)
==> node0: Running 'pre-boot' VM customizations...
==> node0: Booting VM...
==> node0: Waiting for machine to boot. This may take a few minutes...
    node0: SSH address: 127.0.0.1:2222
    node0: SSH username: vagrant
    node0: SSH auth method: private key
    node0:
    node0: Vagrant insecure key detected. Vagrant will automatically replace
    node0: this with a newly generated keypair for better security.
    node0:
    node0: Inserting generated public key within guest...
    node0: Removing insecure key from the guest if it's present...
    node0: Key inserted! Disconnecting and reconnecting using new SSH key...
==> node0: Machine booted and ready!
==> node0: Checking for guest additions in VM...
==> node0: Setting hostname...
==> node0: Configuring and enabling network interfaces...
==> node0: Mounting shared folders...
    node0: /vagrant => /Users/larry/projects/vagrant/vagrant-box-templates/Ubuntu/xenial64/server
==> node0: Running provisioner: shell...
    node0: Running: /var/folders/x5/wbmc7zqj1nv4cnjxjqls86sh0000gn/T/vagrant-shell20170628-82789-jpoks9.sh
==> node0: Hit:1 http://us.archive.ubuntu.com/ubuntu xenial InRelease
==> node0: Get:2 http://us.archive.ubuntu.com/ubuntu xenial-updates InRelease [102 kB]
==> node0: Get:3 http://security.ubuntu.com/ubuntu xenial-security InRelease [102 kB]
==> node0: Get:4 http://us.archive.ubuntu.com/ubuntu xenial-backports InRelease [102 kB]
==> node0: Get:5 http://us.archive.ubuntu.com/ubuntu xenial-updates/main amd64 Packages [568 kB]
==> node0: Get:6 http://us.archive.ubuntu.com/ubuntu xenial-updates/main i386 Packages [549 kB]
==> node0: Get:7 http://security.ubuntu.com/ubuntu xenial-security/main amd64 Packages [294 kB]
==> node0: Get:8 http://us.archive.ubuntu.com/ubuntu xenial-updates/main Translation-en [230 kB]
==> node0: Get:9 http://us.archive.ubuntu.com/ubuntu xenial-updates/restricted amd64 Packages [7,772 B]
==> node0: Get:10 http://us.archive.ubuntu.com/ubuntu xenial-updates/restricted i386 Packages [7,772 B]
==> node0: Get:11 http://us.archive.ubuntu.com/ubuntu xenial-updates/restricted Translation-en [2,548 B]
==> node0: Get:12 http://us.archive.ubuntu.com/ubuntu xenial-updates/universe amd64 Packages [490 kB]
==> node0: Get:13 http://us.archive.ubuntu.com/ubuntu xenial-updates/universe i386 Packages [471 kB]
==> node0: Get:14 http://security.ubuntu.com/ubuntu xenial-security/main i386 Packages [278 kB]
==> node0: Get:15 http://us.archive.ubuntu.com/ubuntu xenial-updates/universe Translation-en [194 kB]
==> node0: Get:16 http://us.archive.ubuntu.com/ubuntu xenial-updates/multiverse amd64 Packages [8,932 B]
==> node0: Get:17 http://us.archive.ubuntu.com/ubuntu xenial-updates/multiverse i386 Packages [7,992 B]
==> node0: Get:18 http://us.archive.ubuntu.com/ubuntu xenial-updates/multiverse Translation-en [4,460 B]
==> node0: Get:19 http://us.archive.ubuntu.com/ubuntu xenial-backports/main amd64 Packages [4,688 B]
==> node0: Get:20 http://us.archive.ubuntu.com/ubuntu xenial-backports/main i386 Packages [4,692 B]
==> node0: Get:21 http://us.archive.ubuntu.com/ubuntu xenial-backports/main Translation-en [3,216 B]
==> node0: Get:22 http://us.archive.ubuntu.com/ubuntu xenial-backports/universe amd64 Packages [5,804 B]
==> node0: Get:23 http://us.archive.ubuntu.com/ubuntu xenial-backports/universe i386 Packages [5,812 B]
==> node0: Get:24 http://us.archive.ubuntu.com/ubuntu xenial-backports/universe Translation-en [3,004 B]
==> node0: Get:25 http://security.ubuntu.com/ubuntu xenial-security/main Translation-en [125 kB]
==> node0: Get:26 http://security.ubuntu.com/ubuntu xenial-security/restricted amd64 Packages [7,420 B]
==> node0: Get:27 http://security.ubuntu.com/ubuntu xenial-security/restricted i386 Packages [7,420 B]
==> node0: Get:28 http://security.ubuntu.com/ubuntu xenial-security/restricted Translation-en [2,428 B]
==> node0: Get:29 http://security.ubuntu.com/ubuntu xenial-security/universe amd64 Packages [140 kB]
==> node0: Get:30 http://security.ubuntu.com/ubuntu xenial-security/universe i386 Packages [125 kB]
==> node0: Get:31 http://security.ubuntu.com/ubuntu xenial-security/universe Translation-en [72.7 kB]
==> node0: Get:32 http://security.ubuntu.com/ubuntu xenial-security/multiverse amd64 Packages [2,748 B]
==> node0: Get:33 http://security.ubuntu.com/ubuntu xenial-security/multiverse i386 Packages [2,908 B]
==> node0: Fetched 3,934 kB in 1s (2,118 kB/s)
==> node0: Reading package lists...
==> node0: Reading package lists...
==> node0: Building dependency tree...
==> node0: Reading state information...
==> node0: The following additional packages will be installed:
==> node0:   libpython-stdlib libpython2.7-minimal libpython2.7-stdlib python python2.7
==> node0:   python2.7-minimal
==> node0: Suggested packages:
==> node0:   python-doc python-tk python2.7-doc binfmt-support
==> node0: The following NEW packages will be installed:
==> node0:   libpython-stdlib libpython2.7-minimal libpython2.7-stdlib python
==> node0:   python-minimal python2.7 python2.7-minimal
==> node0: 0 upgraded, 7 newly installed, 0 to remove and 93 not upgraded.
==> node0: Need to get 3,915 kB of archives.
==> node0: After this operation, 16.6 MB of additional disk space will be used.
==> node0: Get:1 http://us.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libpython2.7-minimal amd64 2.7.12-1ubuntu0~16.04.1 [339 kB]
==> node0: Get:2 http://us.archive.ubuntu.com/ubuntu xenial-updates/main amd64 python2.7-minimal amd64 2.7.12-1ubuntu0~16.04.1 [1,295 kB]
==> node0: Get:3 http://us.archive.ubuntu.com/ubuntu xenial/main amd64 python-minimal amd64 2.7.11-1 [28.2 kB]
==> node0: Get:4 http://us.archive.ubuntu.com/ubuntu xenial-updates/main amd64 libpython2.7-stdlib amd64 2.7.12-1ubuntu0~16.04.1 [1,884 kB]
==> node0: Get:5 http://us.archive.ubuntu.com/ubuntu xenial-updates/main amd64 python2.7 amd64 2.7.12-1ubuntu0~16.04.1 [224 kB]
==> node0: Get:6 http://us.archive.ubuntu.com/ubuntu xenial/main amd64 libpython-stdlib amd64 2.7.11-1 [7,656 B]
==> node0: Get:7 http://us.archive.ubuntu.com/ubuntu xenial/main amd64 python amd64 2.7.11-1 [137 kB]
==> node0: dpkg-preconfigure: unable to re-open stdin: No such file or directory
==> node0: Fetched 3,915 kB in 1s (2,962 kB/s)
==> node0: Selecting previously unselected package libpython2.7-minimal:amd64.
==> node0: (Reading database ...
==> node0: (Reading database ... 5%
==> node0: (Reading database ... 10%
==> node0: (Reading database ... 15%
==> node0: (Reading database ... 20%
==> node0: (Reading database ... 25%
==> node0: (Reading database ... 30%
==> node0: (Reading database ... 35%
==> node0: (Reading database ... 40%
==> node0: (Reading database ... 45%
==> node0: (Reading database ... 50%
==> node0: (Reading database ... 55%
==> node0: (Reading database ... 60%
==> node0: (Reading database ... 65%
==> node0: (Reading database ... 70%
==> node0: (Reading database ... 75%
==> node0: (Reading database ... 80%
==> node0: (Reading database ... 85%
==> node0: (Reading database ... 90%
==> node0: (Reading database ... 95%
==> node0: (Reading database ... 100%
==> node0: (Reading database ...
==> node0: 70600 files and directories currently installed.)
==> node0: Preparing to unpack .../libpython2.7-minimal_2.7.12-1ubuntu0~16.04.1_amd64.deb ...
==> node0: Unpacking libpython2.7-minimal:amd64 (2.7.12-1ubuntu0~16.04.1) ...
==> node0: Selecting previously unselected package python2.7-minimal.
==> node0: Preparing to unpack .../python2.7-minimal_2.7.12-1ubuntu0~16.04.1_amd64.deb ...
==> node0: Unpacking python2.7-minimal (2.7.12-1ubuntu0~16.04.1) ...
==> node0: Selecting previously unselected package python-minimal.
==> node0: Preparing to unpack .../python-minimal_2.7.11-1_amd64.deb ...
==> node0: Unpacking python-minimal (2.7.11-1) ...
==> node0: Selecting previously unselected package libpython2.7-stdlib:amd64.
==> node0: Preparing to unpack .../libpython2.7-stdlib_2.7.12-1ubuntu0~16.04.1_amd64.deb ...
==> node0: Unpacking libpython2.7-stdlib:amd64 (2.7.12-1ubuntu0~16.04.1) ...
==> node0: Selecting previously unselected package python2.7.
==> node0: Preparing to unpack .../python2.7_2.7.12-1ubuntu0~16.04.1_amd64.deb ...
==> node0: Unpacking python2.7 (2.7.12-1ubuntu0~16.04.1) ...
==> node0: Selecting previously unselected package libpython-stdlib:amd64.
==> node0: Preparing to unpack .../libpython-stdlib_2.7.11-1_amd64.deb ...
==> node0: Unpacking libpython-stdlib:amd64 (2.7.11-1) ...
==> node0: Processing triggers for man-db (2.7.5-1) ...
==> node0: Processing triggers for mime-support (3.59ubuntu1) ...
==> node0: Setting up libpython2.7-minimal:amd64 (2.7.12-1ubuntu0~16.04.1) ...
==> node0: Setting up python2.7-minimal (2.7.12-1ubuntu0~16.04.1) ...
==> node0: Linking and byte-compiling packages for runtime python2.7...
==> node0: Setting up python-minimal (2.7.11-1) ...
==> node0: Selecting previously unselected package python.
==> node0: (Reading database ...
==> node0: (Reading database ... 5%
==> node0: (Reading database ... 10%
==> node0: (Reading database ... 15%
==> node0: (Reading database ... 20%
==> node0: (Reading database ... 25%
==> node0: (Reading database ... 30%
==> node0: (Reading database ... 35%
==> node0: (Reading database ... 40%
==> node0: (Reading database ... 45%
==> node0: (Reading database ... 50%
==> node0: (Reading database ... 55%
==> node0: (Reading database ... 60%
==> node0: (Reading database ... 65%
==> node0: (Reading database ... 70%
==> node0: (Reading database ... 75%
==> node0: (Reading database ... 80%
==> node0: (Reading database ... 85%
==> node0: (Reading database ... 90%
==> node0: (Reading database ... 95%
==> node0: (Reading database ... 100%
==> node0: (Reading database ...
==> node0: 71347 files and directories currently installed.)
==> node0: Preparing to unpack .../python_2.7.11-1_amd64.deb ...
==> node0: Unpacking python (2.7.11-1) ...
==> node0: Processing triggers for man-db (2.7.5-1) ...
==> node0: Setting up libpython2.7-stdlib:amd64 (2.7.12-1ubuntu0~16.04.1) ...
==> node0: Setting up python2.7 (2.7.12-1ubuntu0~16.04.1) ...
==> node0: Setting up libpython-stdlib:amd64 (2.7.11-1) ...
==> node0: Setting up python (2.7.11-1) ...
==> node0: Running provisioner: ansible...
    node0: Running ansible-playbook...

PLAY [all] *********************************************************************

TASK [Gathering Facts] *********************************************************
ok: [node0]

TASK [Updating Apt Cache (Debian)] *********************************************
ok: [node0]

TASK [Installing Ansible Pre-Reqs (Alpine)] ************************************
skipping: [node0] => (item=[])

TASK [Installing Python Packages (Alpine)] *************************************
skipping: [node0] => (item=[])

TASK [Installing Python Packages (Alpine)] *************************************
skipping: [node0] => (item=[])

TASK [Installing Ansible Pre-Reqs (Debian)] ************************************
changed: [node0] => (item=[u'build-essential', u'libffi-dev', u'libssl-dev', u'python-dev', u'python-pip', u'python-setuptools'])

TASK [Installing EPEL Repo (RedHat)] *******************************************
skipping: [node0]

TASK [Installing Ansible Pre-Reqs (RedHat)] ************************************
skipping: [node0] => (item=[])

TASK [Installing Ansible Pre-Reqs (Fedora)] ************************************
skipping: [node0]

TASK [Installing Ansible Pre-Reqs (Fedora)] ************************************
skipping: [node0] => (item=[])

TASK [Installing Ansible Pre-Reqs (openSUSE)] **********************************
skipping: [node0] => (item=[])

TASK [Updating Python Modules] *************************************************
changed: [node0] => (item=pip)
changed: [node0] => (item=cffi)

TASK [Installing Ansible] ******************************************************
changed: [node0]

TASK [Ensuring host_vars Directory Exists] *************************************
changed: [node0 -> localhost]

TASK [Ensuring Host File Exists In host_vars] **********************************
ok: [node0 -> localhost]

TASK [Creating Missing host_vars] **********************************************
changed: [node0 -> localhost]

TASK [Updating ansible_ssh_host] ***********************************************
skipping: [node0]

TASK [Updating ansible_ssh_host] ***********************************************
changed: [node0 -> localhost]

TASK [Capturing eth1 IP Address (Alpine)] **************************************
skipping: [node0]

TASK [Updating ansible_ssh_host (Alpine)] **************************************
skipping: [node0]

TASK [Updating ansible_ssh_port] ***********************************************
changed: [node0 -> localhost]

TASK [Updating ansible_ssh_key] ************************************************
changed: [node0 -> localhost]

TASK [Ensuring host_vars Is YAML Formatted] ************************************
changed: [node0 -> localhost]

PLAY RECAP *********************************************************************
node0                      : ok=12   changed=9    unreachable=0    failed=0

==> node0: Running provisioner: ansible...
    node0: Running ansible-playbook...

PLAY [test_nodes] **************************************************************

TASK [Gathering Facts] *********************************************************
ok: [node0]

TASK [ansible-base : debian | running apt-get update] **************************
ok: [node0]

TASK [ansible-base : debian | running apt-get update (forced)] *****************
skipping: [node0]

TASK [ansible-base : debian | installing base packages] ************************
changed: [node0] => (item=[u'build-essential', u'software-properties-common', u'curl', u'git', u'git-core', u'ntp', u'scsitools'])

TASK [ansible-base : debian | resetting /etc/dhcp/dhclient.conf to default] ****
skipping: [node0]

TASK [ansible-base : debian_update_dns_nameservers | setting dns nameservers] ***
skipping: [node0]

TASK [ansible-base : debian | setting dns search suffix] ***********************
skipping: [node0]

TASK [ansible-base : redhat | installing base packages] ************************
skipping: [node0] => (item=[])

TASK [ansible-base : redhat | installing base packages] ************************
skipping: [node0] => (item=[])

TASK [ansible-dnsmasq : alpine | Installing DNSMasq] ***************************
skipping: [node0]

TASK [ansible-dnsmasq : debian | Installing DNSMasq] ***************************
changed: [node0]

TASK [ansible-dnsmasq : redhat | Installing DNSMasq] ***************************
skipping: [node0]

TASK [ansible-dnsmasq : redhat | Installing DNSMasq] ***************************
skipping: [node0]

TASK [ansible-dnsmasq : redhat | Ensuring DNSMasq Service is Enabled and Started] ***
skipping: [node0]

TASK [ansible-dnsmasq : opensuse | Installing DNSMasq] *************************
skipping: [node0]

TASK [ansible-dnsmasq : opensuse | Ensuring DNSMasq Service Is Enabled and Started] ***
skipping: [node0]

TASK [ansible-dnsmasq : dnsmasq_config | Configuring DNSMasq] ******************
changed: [node0]

TASK [ansible-dnsmasq : dnsmasq_config | Ensuring /var/lib/tftpboot Exists] ****
skipping: [node0]

RUNNING HANDLER [ansible-dnsmasq : restart dnsmasq] ****************************
changed: [node0]

PLAY RECAP *********************************************************************
node0                      : ok=6    changed=4    unreachable=0    failed=0

Idempotence test: pass
==> node0: Forcing shutdown of VM...
==> node0: Destroying VM and associated drives...
```

### Learning Ansible

If you are interested in learning Ansible ensure that
[Ansible](https://www.ansible.com) is installed on your host machine.

#### Ansible Groups

If you need to create different Ansible groups for your project all you
need to do is edit the `environment.yml`. For example if I am working on a project
for Docker Swarm I might want to separate out my nodes by Swarm Managers and
Swarm Workers. So I would something similar to below:

`environment.yml`:

```yaml
- name: "node0"
  ansible_groups:
    - "swarm_managers"
  box: "mrlesmithjr/xenial64"
  desktop: false
  # disks:
  #   - size: 10
  #     controller: "SATA Controller"
  #   - size: 10
  #     controller: "SATA Controller"
  interfaces:
    - ip: 192.168.250.10
      auto_config: true
      method: "static"
  #   - ip: 192.168.1.10
  #     auto_config: false
  #     method: 'static'
  #     network_name: 'network-1'
  linked_clone: true
  mem: 512
  provision: true
  vcpu: 1
  # port_forwards:
  #   - guest: 80
  #     host: 8080
  #   - guest: 443
  #     host: 4433
- name: "node1"
  ansible_groups:
    - "docker_swarm_workers"
  box: "mrlesmithjr/xenial64"
  desktop: false
  # disks:
  #   - size: 10
  #     controller: "SATA Controller"
  #   - size: 10
  #     controller: "SATA Controller"
  interfaces:
    - ip: 192.168.250.11
      auto_config: true
      method: "static"
  #   - ip: 192.168.1.10
  #     auto_config: false
  #     method: 'static'
  #     network_name: 'network-1'
  linked_clone: true
  mem: 512
  provision: true
  vcpu: 1
  # port_forwards:
  #   - guest: 80
  #     host: 8080
  #   - guest: 443
  #     host: 4433
```

And that would be all you need to do and those groups would be created when we
do a `vagrant up`. As you can see there were no changes required in the
`Vagrantfile` to make this all happen. And you will be able to define your
playbook as you normally would.

#### Ansible playbooks

Within in the [playbooks](playbooks/) directory there is an included `playbook.yml` file to use as a skeleton playbook. This playbook is always
executed when provisioning. So, you may want to just modify this playbook to
suit your needs. However, you may create additional playbooks or leverage
existing ones by adapting your `environment.yml` within the distro folders.

#### Ansible `requirements.yml`

Within the root folder there is also an included `requirements.yml` file which
includes some basics [Ansible](https://www.ansible.com) roles that can be
installed to get an understanding of using this method.

##### Installing Ansible roles

###### Global Ansible roles installation

If you would like to install the [Ansible](https://www.ansible.com) roles
globally on your host machine you can do so by:

```bash
sudo ansible-galaxy install -r requirements.yml
```

###### Non-Global Ansible roles installation

If you would like to install the [Ansible](https://www.ansible.com) roles
in the current directory in a specific distro version you can do so by:

For example for `Ubuntu Xenial`:

```bash
cd vagrant-box-templates/Ubuntu/xenial64/server
ansible-galaxy install -r requirements.yml -p ./roles
```

###### Using existing folder of Ansible roles

If you have an existing folder which includes some
[Ansible](https://www.ansible.com) roles you can very easily leverage those as
well.

> TIP: This is something that I do for development of roles.

Simply edit the included `ansible.cfg` file and change the following:

`From`:

```bash
# additional paths to search for roles in, colon separated
#roles_path    = /etc/ansible/roles
```

`To`:

```bash
# additional paths to search for roles in, colon separated
roles_path    = /etc/ansible/roles:~/Git_Projects/GitHub/mrlesmithjr:roles
```

## License

MIT

## Author Information

Larry Smith Jr.

- [EverythingShouldBeVirtual](http://everythingshouldbevirtual.com)
- [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
- [mrlesmithjr@gmail.com](mailto:mrlesmithjr@gmail.com)
