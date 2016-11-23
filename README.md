Purpose
=======

Spin up different OS types using Vagrant and learn Ansible at the same time if desired. Some distros also
include Desktop versions.

Requirements
------------

Ansible (http://www.ansible.com/home)  
VirtualBox (https://www.virtualbox.org/)  
Vagrant (https://www.vagrantup.com/)

Usage
-----

````
git clone https://github.com/mrlesmithjr/vagrant-box-templates
cd vagrant-box-templates
````
Find the OS of your choice and spin up a node or more.  
Each Vagrantfile contains a var called N...which is set to N = 1
in most cases. You may change this to any number you wish to spin up
N number of nodes.
````
Vagrant.configure(2) do |config|
  #Define the number of nodes to spin up
  N = 1
````
When you are ready to spin up:
````
vagrant up
````
For example if I want to spin up a Ubuntu Trusty server node:  
````
cd vagrant-box-templates/Ubuntu/trusty64/server
vagrant up
vagrant ssh
````
If you are interested in learning Ansible ensure that Ansible is installed on your host machine. There is an included playbook.yml file to use as a skeleton playbook. Within in folder there is also an included requirements.yml file which includes some basics Ansible roles that can be installed to get an understanding of using this method.  
You will need to install the roles on your host machine which can be done by:
````
sudo ansible-galaxy install -r requirements.yml -f
````
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
