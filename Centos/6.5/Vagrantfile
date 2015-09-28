# -*- mode: ruby -*-
# vi: set ft=ruby :

# Ensure yaml module is loaded
require 'yaml'

# Read yaml node definitions to create **Update nodes.yml to reflect any changes
nodes = YAML.load_file('nodes.yml')

Vagrant.configure(2) do |config|
#  config.ssh.insert_key = false
#  config.vm.provision :shell, path: "bootstrap.sh"

  nodes.each do |nodes|
    config.vm.define nodes["name"] do |node|
      node.vm.hostname = nodes["name"]
      node.vm.box = nodes["box"]
#      node.vm.provision :shell, path: "bootstrap_ansible.sh"
      if nodes["ansible_ssh_host_ip"] != "None"
        node.vm.network "private_network", ip: nodes["ansible_ssh_host_ip"]
      end
      if nodes["config_interfaces"] == "True"
        ints = nodes["interfaces"]
        ints.each do |int|
          if int["method"] == "static" and int["type"] == "private_network" and int["network_name"] != "None" and int["auto_config"] == "True"
            node.vm.network "private_network", ip: int["ip"], virtualbox__intnet: int["network_name"]
          end
          if int["method"] == "static" and int["type"] == "private_network" and int["network_name"] != "None" and int["auto_config"] == "False"
            node.vm.network "private_network", ip: int["ip"], virtualbox__intnet: int["network_name"], auto_config: false
          end
          if int["method"] == "static" and int["type"] == "private_network" and int["network_name"] == "None" and int["auto_config"] == "True"
            node.vm.network "private_network", ip: int["ip"]
          end
          if int["method"] == "static" and int["type"] == "private_network" and int["network_name"] == "None" and int["auto_config"] == "False"
            node.vm.network "private_network", ip: int["ip"], auto_config: false
          end
          if int["method"] == "dhcp" and int["type"] == "private_network"
            node.vm.network "private_network", type: "dhcp"
          end
        end
      end
      node.vm.synced_folder ".", "/vagrant"
      node.vm.provider "virtualbox" do |v|
        v.memory = nodes["mem"]
        v.cpus = nodes["cpus"]
      end
    end
  end
  config.vm.provision :ansible do |ansible|
    ansible.playbook = "bootstrap.yml"
  end
#  if Vagrant.has_plugin?("vagrant-cachier")
#    config.cache.scope = :box
#  end
end
