Purpose
=======

Spins up a Fedora 22 x64 Server node.

Requirements
============

Ansible (http://www.ansible.com/home)

VirtualBox (https://www.virtualbox.org/)

Vagrant (https://www.vagrantup.com/)


Variable Definitions
====================
````
nodes.yml
````
Define the nodes to spin up
````
- name: node-1
  box: mrlesmithjr/mrlesmithjr/fedora22_x86_64
  mem: 2048
  cpus: 1
  ansible_ssh_host_ip: 192.168.202.33 #always create for Ansible provisioning within nodes
  config_interfaces: "False"  #defines if interfaces below should be created or not...Set to "False" if you do not wish to create the interfaces.
  interfaces:  #Define additional interface settings
    - ip: 192.168.12.11
      auto_config: "True"
      network_name: 01-to-02
      method: static
      type: private_network
````

Usage
=====

````
git clone https://github.com/mrlesmithjr/vagrant-box-templates
cd vagrant-box-templates/Fedora/server/fedora22_x86_64
````
Update nodes.yml to reflect your desired node(s) configurations to spin up.

Spin up your environment
````
vagrant up
````

License
-------

BSD

Author Information
------------------

Larry Smith Jr.
- @mrlesmithjr
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com
