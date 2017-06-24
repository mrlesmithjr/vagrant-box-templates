<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
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
  - [Useful information](#useful-information)
    - [Vagrantfile](#vagrantfile)
    - [File structure](#file-structure)
    - [Working on different projects](#working-on-different-projects)
      - [Create development environment](#create-development-environment)
      - [Create project development environment](#create-project-development-environment)
      - [Keeping development environment up to date with this repo](#keeping-development-environment-up-to-date-with-this-repo)
  - [Usage](#usage)
    - [Getting started](#getting-started)
      - [Clone repo](#clone-repo)
      - [Choose distro](#choose-distro)
      - [Customizing environment](#customizing-environment)
        - [Disks, interfaces, and port_forwards](#disks-interfaces-and-port_forwards)
        - [Provisioning](#provisioning)
      - [Spinning up environment](#spinning-up-environment)
        - [Example `Ubuntu Trusty` environment](#example-ubuntu-trusty-environment)
      - [Tearing down environment](#tearing-down-environment)
    - [Learning Ansible](#learning-ansible)
      - [Ansible Groups](#ansible-groups)
      - [Ansible playbook](#ansible-playbook)
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

-   [Ansible](https://www.ansible.com)
-   [Vagrant](https://www.vagrantup.com)
-   [Virtualbox](https://www.virtualbox.org)

### [Alpine](https://alpinelinux.org/) box requirements

#### `vagrant-alpine` plugin

> NOTE:  **require** the `vagrant-alpine` plugin to be installed

```bash
vagrant plugin install vagrant-alpine
```

#### `/vagrant` synced_folder

> NOTE: `NFS` is used for the `/vagrant` synced_folder.
> This means you will be prompted for `sudo` password when spinning up a box.
> This can be changed to not prompt by references
> [here](https://www.vagrantup.com/docs/synced-folders/nfs.html)

##### Setting up `sudoers`

###### `OS X`

To setup `sudoers` for `OSX` add the following using `visudo`

```bash
Cmnd_Alias VAGRANT_EXPORTS_ADD = /usr/bin/tee -a /etc/exports
Cmnd_Alias VAGRANT_NFSD = /sbin/nfsd restart
Cmnd_Alias VAGRANT_EXPORTS_REMOVE = /usr/bin/sed -E -e /*/ d -ibak /etc/exports
%admin ALL=(root) NOPASSWD: VAGRANT_EXPORTS_ADD, VAGRANT_NFSD, VAGRANT_EXPORTS_REMOVE
```

###### `Ubuntu`

To setup `sudoers` for `Ubuntu` add the following using `visudo`

```bash
Cmnd_Alias VAGRANT_EXPORTS_CHOWN = /bin/chown 0\:0 /tmp/*
Cmnd_Alias VAGRANT_EXPORTS_MV = /bin/mv -f /tmp/* /etc/exports
Cmnd_Alias VAGRANT_NFSD_CHECK = /etc/init.d/nfs-kernel-server status
Cmnd_Alias VAGRANT_NFSD_START = /etc/init.d/nfs-kernel-server start
Cmnd_Alias VAGRANT_NFSD_APPLY = /usr/sbin/exportfs -ar
%sudo ALL=(root) NOPASSWD: VAGRANT_EXPORTS_CHOWN, VAGRANT_EXPORTS_MV, VAGRANT_NFSD_CHECK, VAGRANT_NFSD_START, VAGRANT_NFSD_APPLY
```

###### `Fedora`

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

## Useful information

### Vagrantfile

A single [Vagrantfile](./Vagrantfile) is used for all distros to use. This helps
keeping changes to a minimum (Very seldom needed). The reason behind this is
that I have spent close to two years trying to come up with a single `Vagrantfile`
that would fit most any scenario that I have a use case for during development.
Many of these scenarios involve multinode clustering, routing, loadbalancing,
ZFS, GlusterFS, Docker Swarm, Kubernetes, ELK Stack, and so on. Not to say that
a specific use case may not present itself that would require a change to
the `Vagrantfile` but those are far in between.

```ruby
# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.

# Ensure yaml module is loaded
require 'yaml'

# Read yaml node definitions to create
# **Update nodes.yml to reflect any changes
nodes = YAML.load_file(File.join(File.dirname(__FILE__), 'nodes.yml'))

# Define global variables
#

Vagrant.configure(2) do |config|
  # Iterate over nodes to get a count
  # Define as 0 for counting the number of nodes to create from nodes.yml
  groups = [] # Define array to hold ansible groups
  num_nodes = 0
  populated_ansible_groups = Hash.new # Create hash to contain iterated groups

  # Create array of Ansible Groups from iterated nodes
  nodes.each do |node|
    num_nodes = node
    node['ansible_groups'].each do |group|
      groups.push(group)
    end
  end

  # Remove duplicate Ansible Groups
  groups = groups.uniq

  # Iterate through array of Ansible Groups
  groups.each do |group|
    group_nodes = []
    # Iterate list of nodes
    nodes.each do |node|
      node['ansible_groups'].each do |nodegroup|
        # Check if node is a member of iterated group
        if nodegroup == group
          group_nodes.push(node['name'])
        end
      end
      populated_ansible_groups[group] = group_nodes
    end
  end

  # Dynamic Ansible Groups iterated from nodes.yml
  ansible_groups = populated_ansible_groups

  # Define Ansible groups statically for more control
  # ansible_groups = {
  #   "spines" => ["node0", "node7"],
  #   "leafs" => ["node[1:2]", "node[8:9]"],
  #   "quagga-routers:children" => ["spines", "leafs", "compute-nodes"],
  #   "compute-nodes" => ["node[3:6]"],
  #   "docker-swarm:children" => ["docker-swarm-managers", "docker-swarm-workers"],
  #   "docker-swarm-managers" => ["node[3:4]"],
  #   "docker-swarm-workers" => ["node[5:6]"]
  # }

  #Iterate over nodes
  nodes.each do |node_id|
    # Below is needed if not using Guest Additions
    # config.vm.synced_folder ".", "/vagrant", type: "rsync",
    #   rsync__exclude: "hosts"
    config.vm.define node_id['name'] do |node|
      if not node_id['synced_folder'].nil?
        if not node_id['synced_folder']['type'].nil?
          config.vm.synced_folder ".", "/vagrant", type: node_id['synced_folder']['type']
        end
      end
      node.vm.box = node_id['box']
      node.vm.hostname = node_id['name']
      node.vm.provider "virtualbox" do |vb|
        vb.memory = node_id['mem']
        vb.cpus = node_id['vcpu']

        # Setup desktop environment
        if not node_id['desktop'].nil?
          if node_id['desktop']
            vb.gui = true
            vb.customize ["modifyvm", :id, "--graphicscontroller", "vboxvga"]
            vb.customize ["modifyvm", :id, "--accelerate3d", "on"]
            vb.customize ["modifyvm", :id, "--ioapic", "on"]
            vb.customize ["modifyvm", :id, "--vram", "128"]
            vb.customize ["modifyvm", :id, "--hwvirtex", "on"]
          end
        end

        # Add additional disk(s)
        if not node_id['disks'].nil?
          dnum = 0
          node_id['disks'].each do |disk_num|
            dnum = (dnum.to_i + 1)
            ddev = ("#{node_id['name']}_Disk#{dnum}.vdi")
            dsize = disk_num['size'].to_i * 1024
            unless File.exist?("#{ddev}")
              vb.customize ['createhd', '--filename', ("#{ddev}"), \
                '--variant', 'Fixed', '--size', dsize]
            end
            vb.customize ['storageattach', :id,  '--storagectl', \
              "#{disk_num['controller']}", '--port', dnum, '--device', 0, \
              '--type', 'hdd', '--medium', "#{ddev}"]
          end
        end
      end

      # Provision network interfaces
      if not node_id['interfaces'].nil?
        node_id['interfaces'].each do |int|
          if int['method'] == 'dhcp'
            if int['network_name'] == "None"
              node.vm.network :private_network, \
              type: "dhcp"
            end
            if int['network_name'] != "None"
              node.vm.network :private_network, \
              virtualbox__intnet: int['network_name'], \
              type: "dhcp"
            end
          end
          if int['method'] == "static"
            if int['network_name'] == "None"
              node.vm.network :private_network, \
              ip: int['ip'], \
              auto_config: int['auto_config']
            end
            if int['network_name'] != "None"
              node.vm.network :private_network, \
              virtualbox__intnet: int['network_name'], \
              ip: int['ip'], \
              auto_config: int['auto_config']
            end
          end
        end
      end

      # Port Forwards
      if not node_id['port_forwards'].nil?
        node_id['port_forwards'].each do |pf|
          node.vm.network :forwarded_port, \
          guest: pf['guest'], \
          host: pf['host']
        end
      end

      # Provisioners
      if not node_id['provision'].nil?
        if node_id['provision']
          #runs initial shell script
          config.vm.provision :shell, path: "bootstrap.sh", keep_color: "true"
          if node_id == num_nodes
            node.vm.provision "ansible" do |ansible|
              ansible.limit = "all"
              #runs bootstrap Ansible playbook
              ansible.playbook = "bootstrap.yml"
            end
            node.vm.provision "ansible" do |ansible|
              ansible.limit = "all"
              #runs Ansible playbook for installing roles/executing tasks
              ansible.playbook = "playbook.yml"
              ansible.groups = ansible_groups
            end
          end
        end
      end
    end

  end
end
```

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

1.  Clone this repo

```bash
cd ~
mkdir -p projects/vagrant
cd projects/vagrant
git clone https://github.com/mrlesmithjr/vagrant-box-templates
```

2.  Remove the `origin` remote

```bash
cd vagrant-box-templates
git remote remove origin
```

3.  Add this repo as the `upstream` remote

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

Each distro folder contains a `nodes.yml` file which you can change the number
of nodes to spin up if desired.

##### Disks, interfaces, and port_forwards

If you would like to change `disks|interfaces|port_forwards` feel free to
uncomment those sections and adjust them as needed.

`Ubuntu/xenial64/server/nodes.yml`:

```yaml
---
- name: 'node0'
  ansible_groups:
    - 'test-nodes'
  box: 'mrlesmithjr/xenial64'
  desktop: false
  # disks:
  #   - size: 10
  #     controller: "SATA Controller"
  #   - size: 10
  #     controller: "SATA Controller"
  # interfaces:
  #   - ip: 192.168.250.10
  #     auto_config: true
  #     method: 'static'
  #   - ip: 192.168.1.10
  #     auto_config: false
  #     method: 'static'
  #     network_name: 'network-1'
  mem: 512
  provision: false
  vcpu: 1
  # port_forwards:
  #   - guest: 80
  #     host: 8080
  #   - guest: 443
  #     host: 4433
```

##### Provisioning

If you would like to provision the nodes when they startup you will need to
set `provision: true` in the `nodes.yml`.

```yaml
- name: 'node0'
  ansible_groups:
    - 'test-nodes'
  box: 'mrlesmithjr/xenial64'
  desktop: false
  # disks:
  #   - size: 10
  #     controller: "SATA Controller"
  #   - size: 10
  #     controller: "SATA Controller"
  # interfaces:
  #   - ip: 192.168.250.10
  #     auto_config: true
  #     method: 'static'
  #   - ip: 192.168.1.10
  #     auto_config: false
  #     method: 'static'
  #     network_name: 'network-1'
  mem: 512
  provision: true
  vcpu: 1
  # port_forwards:
  #   - guest: 80
  #     host: 8080
  #   - guest: 443
  #     host: 4433
```

By default the following provisioning will occur:

-   [bootstrap.sh](./bootstrap.sh)
-   [bootstrap.yml](./bootstrap.yml)
-   [playbook.yml](./playbook.yml)

```ruby
# Provisioners
if not node_id['provision'].nil?
  if node_id['provision']
    #runs initial shell script
    config.vm.provision :shell, path: "bootstrap.sh", keep_color: "true"
    if node_id == num_nodes
      node.vm.provision "ansible" do |ansible|
        ansible.limit = "all"
        #runs bootstrap Ansible playbook
        ansible.playbook = "bootstrap.yml"
      end
      node.vm.provision "ansible" do |ansible|
        ansible.limit = "all"
        #runs Ansible playbook for installing roles/executing tasks
        ansible.playbook = "playbook.yml"
        ansible.groups = ansible_groups
      end
    end
  end
end
```

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
    ./cleanup.sh
```

`Windows`:

```bat
    cleanup.bat
```

### Learning Ansible

If you are interested in learning Ansible ensure that
[Ansible](https://www.ansible.com) is installed on your host machine.

#### Ansible Groups

If you need to create different Ansible groups for your project all you
need to do is edit the `nodes.yml`. For example if I am working on a project
for Docker Swarm I might want to separate out my nodes by Swarm Managers and
Swarm Workers. So I would something similar to below:

`nodes.yml`:

```yaml
---
- name: 'node0'
  ansible_groups:
    - 'swarm_managers'
  box: 'mrlesmithjr/xenial64'
  desktop: false
  # disks:
  #   - size: 10
  #     controller: "SATA Controller"
  #   - size: 10
  #     controller: "SATA Controller"
  interfaces:
    - ip: 192.168.250.10
      auto_config: true
      method: 'static'
  #   - ip: 192.168.1.10
  #     auto_config: false
  #     method: 'static'
  #     network_name: 'network-1'
  mem: 512
  provision: true
  vcpu: 1
  # port_forwards:
  #   - guest: 80
  #     host: 8080
  #   - guest: 443
  #     host: 4433
- name: 'node1'
  ansible_groups:
    - 'docker_swarm_workers'
  box: 'mrlesmithjr/xenial64'
  desktop: false
  # disks:
  #   - size: 10
  #     controller: "SATA Controller"
  #   - size: 10
  #     controller: "SATA Controller"
  interfaces:
    - ip: 192.168.250.11
      auto_config: true
      method: 'static'
  #   - ip: 192.168.1.10
  #     auto_config: false
  #     method: 'static'
  #     network_name: 'network-1'
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

#### Ansible playbook

There is an included `playbook.yml` file in the root folder to use as a
skeleton playbook.

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

-   [@mrlesmithjr]
-   <http://everythingshouldbevirtual.com>
-   mrlesmithjr [at] gmail.com

[@mrlesmithjr]: https://www.twitter.com/mrlesmithjr
