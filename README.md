Purpose
=======

Spin up different OS types using Vagrant and learn Ansible at the same time if
desired. Some distros also include Desktop versions.

Requirements
------------

- [Ansible]
- [Vagrant]
- [Virtualbox]

Usage
-----

```
git clone https://github.com/mrlesmithjr/vagrant-box-templates
cd vagrant-box-templates
```
Find the OS of your choice and spin up a node or more.  
Each distro folder has a `nodes.yml` file which you can change the number of
nodes to spin up if desired.

If you would like to change `disks|interfaces|port_forwards` feel free to
uncomment those sections and adjust them as needed.

`Ubuntu/xenial64/server/nodes.yml`:
```
---
- name: 'node0'
  ansible_groups:
    - 'test-nodes'
  box: 'mrlesmithjr/xenial64'
  desktop: false
  # disks:
  #   - size: '10'
  #     controller: "SATA Controller"
  #   - size: '10'
  #     controller: "SATA Controller"
  # interfaces:
  #   - ip: '192.168.250.10'
  #     auto_config: true
  #     method: 'static'
  #   - ip: '192.168.1.10'
  #     auto_config: false
  #     method: 'static'
  #     network_name: 'network-1'
  mem: '512'
  provision: false
  vcpu: '1'
  # port_forwards:
  #   - guest: '80'
  #     host: '8080'
  #   - guest: '443'
  #     host: '4433'
```

When you are ready to spin up:
```
vagrant up
```
For example if I want to spin up a Ubuntu Trusty server node:  
```
cd vagrant-box-templates/Ubuntu/trusty64/server
vagrant up
vagrant ssh
```
If you are interested in learning Ansible ensure that Ansible is installed on
your host machine. There is an included `playbook.yml` file in the root folder
to use as a skeleton playbook. Within the root folder there is also an
included `requirements.yml` file which includes some basics Ansible roles that
can be installed to get an understanding of using this method. You will need to
install the roles on your host machine which can be done by:
```
sudo ansible-galaxy install -r requirements.yml -f
```
If you would like to provision the nodes when they startup you will need to
set `provision: true` in the `nodes.yml`.
```
- name: 'node0'
  ansible_groups:
    - 'test-nodes'
  box: 'mrlesmithjr/xenial64'
  desktop: false
  # disks:
  #   - size: '10'
  #     controller: "SATA Controller"
  #   - size: '10'
  #     controller: "SATA Controller"
  # interfaces:
  #   - ip: '192.168.250.10'
  #     auto_config: true
  #     method: 'static'
  #   - ip: '192.168.1.10'
  #     auto_config: false
  #     method: 'static'
  #     network_name: 'network-1'
  mem: '512'
  provision: true
  vcpu: '1'
  # port_forwards:
  #   - guest: '80'
  #     host: '8080'
  #   - guest: '443'
  #     host: '4433'
```
Most files are symlinked into each distro folder to keep a consistent and easy
method of changing things around. Feel free to change as needed.

And when you are all done with your Vagrant node(s) you can tear everything down
and cleanup easily by running the following:

`Non-Windows`
```
./cleanup.sh
```
`Windows`
```
cleanup.bat
```

License
-------

BSD

Author Information
------------------

Larry Smith Jr.
- @mrlesmithjr
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com

[Ansible]: <https://www.ansible.com>
[Vagrant]: <https://www.vagrantup.com/>
[Virtualbox]: <https://www.virtualbox.org/>
