# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.

# Ensure yaml module is loaded
require 'yaml'

# Read yaml node definitions to create
# **Update environment.yml to reflect any changes
environment = YAML.load_file(File.join(File.dirname(__FILE__), 'environment.yml'))
nodes = environment['nodes']

# Define global variables
#

Vagrant.configure(2) do |config|
  # Iterate over nodes to get a count
  # Define as 0 for counting the number of nodes to create from environment.yml
  groups = [] # Define array to hold ansible groups
  num_nodes = 0
  populated_ansible_groups = {} # Create hash to contain iterated groups

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
        group_nodes.push(node['name']) if nodegroup == group
      end
      populated_ansible_groups[group] = group_nodes
    end
  end

  # Dynamic Ansible Groups iterated from environment.yml
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

  # Iterate over nodes
  nodes.each do |node_id|
    config.vm.define node_id['name'] do |node|
      if node_id['disable_synced_folders'].nil?
        if node_id['synced_folder'].nil?
          config.vm.synced_folder 'playbooks', '/playbooks'
          config.vm.synced_folder 'scripts', '/scripts'
        else
          unless node_id['synced_folder']['type'].nil?
            if node_id['synced_folder']['type'] == 'rsync'
              config.vm.synced_folder '.',
                                      '/vagrant',
                                      type: 'rsync',
                                      rsync__args: ['--verbose', '--archive',
                                                    '--delete', '-z']
              config.vm.synced_folder 'playbooks',
                                      '/playbooks',
                                      type: 'rsync',
                                      rsync__args: ['--verbose', '--archive',
                                                    '--delete', '-z']
              config.vm.synced_folder 'scripts',
                                      '/scripts',
                                      type: 'rsync',
                                      rsync__args: ['--verbose', '--archive',
                                                    '--delete', '-z']
            else
              config.vm.synced_folder '.',
                                      '/vagrant',
                                      type: node_id['synced_folder']['type']
              config.vm.synced_folder 'playbooks',
                                      '/playbooks',
                                      type: node_id['synced_folder']['type']
              config.vm.synced_folder 'scripts',
                                      '/scripts',
                                      type: node_id['synced_folder']['type']
            end
          end
        end
        unless environment['synced_folders'].nil?
          environment['synced_folders'].each do |folder|
            config.vm.synced_folder folder['src'], folder['mountpoint'],
                                    type: folder['type']
          end
        end
      else
        if node_id['disable_synced_folders']
          config.vm.synced_folder '.', '/vagrant', disabled: true
        else
          config.vm.synced_folder '.', '/vagrant'
          config.vm.synced_folder 'playbooks', '/playbooks'
          config.vm.synced_folder 'scripts', '/scripts'
        end
      end

      node.vm.box = node_id['box']
      if node_id['manage_hostname'].nil?
        node.vm.hostname = node_id['name']
      else
        node.vm.hostname = node_id['name'] if node_id['manage_hostname']
      end

      # Setup Windows communication
      unless node_id['windows'].nil?
        if node_id['windows']
          node.vm.guest = :windows
          node.vm.communicator = :winrm
          # config.winrm.transport = :ssl
          # config.winrm.ssl_peer_verification = false
        end
      end

      node.vm.provider 'virtualbox' do |vbox|
        # Use linked clones - default: true unless defined in environment.yml
        # Define linked_clone: true|false in environment.yml per node
        vbox.linked_clone = node_id['linked_clone'] ||= true

        vbox.memory = node_id['mem']
        vbox.cpus = node_id['vcpu']

        # Setup desktop environment
        unless node_id['desktop'].nil?
          if node_id['desktop']
            vbox.gui = true
            vbox.customize ['modifyvm', :id, '--accelerate3d', 'on']
            # This is commented out until resolution has been found for proper
            # usage. For now it will use the default graphics controller.
            vbox.customize ['modifyvm', :id, '--graphicscontroller', 'vmsvga']
            # vbox.customize ['modifyvm', :id, '--graphicscontroller', 'vboxvga']
            vbox.customize ['modifyvm', :id, '--hwvirtex', 'on']
            vbox.customize ['modifyvm', :id, '--ioapic', 'on']
            vbox.customize ['modifyvm', :id, '--vram', '128']
            vbox.customize ['modifyvm', :id, '--audio', 'none']
          end
        end

        # Setup Windows Server
        unless node_id['windows'].nil?
          if node_id['windows']
            vbox.default_nic_type = '82540EM'
            # We set this to false because we can use vagrant rdp
            # vbox.gui = false
            vbox.customize ['modifyvm', :id, '--accelerate2dvideo', 'on']
            vbox.customize ['modifyvm', :id, '--accelerate3d', 'on']
            vbox.customize ['modifyvm', :id, '--graphicscontroller', 'vboxsvga']
            vbox.customize ['modifyvm', :id, '--clipboard', 'bidirectional']
            vbox.customize ['modifyvm', :id, '--vram', '128']
          end
        end

        # Add additional disk(s)
        unless node_id['disks'].nil?
          # Start at 1 to account for 2 disks in box image
          # May need to figure out another way to do this, but for now it works
          dnum = 1
          node_id['disks'].each do |disk_num|
            dnum = (dnum.to_i + 1)
            ddev = "#{node_id['name']}_Disk#{dnum}.vdi"
            dsize = disk_num['size'].to_i * 1024
            unless File.file?(ddev.to_s)
              vbox.customize ['createhd', '--filename', ddev.to_s, \
                              '--variant', 'Fixed', '--size', dsize]
            end
            vbox.customize ['storageattach', :id, '--storagectl', \
                            (disk_num['controller']).to_s, '--port', dnum, \
                            '--device', 0, '--type', 'hdd', \
                            '--medium', ddev.to_s]
          end
        end
      end

      %w[vmware_desktop vmware_fusion].each do |vmware|
        node.vm.provider vmware do |vmw|
          # Use linked clones - default: true unless defined in environment.yml
          # Define linked_clone: true|false in environment.yml per node
          vmw.linked_clone = node_id['linked_clone'] ||= true

          vmw.vmx['memsize'] = node_id['mem']
          vmw.vmx['numvcpus'] = node_id['vcpu']

          # Enable nested virtualization
          unless node_id['nested_virtualization'].nil?
            vmw.vmx['vhv.enable'] = true if node_id['nested_virtualization']
          end

          # Allow public IP SSH connection
          unless node_id['ssh_use_public_ip'].nil?
            vmw.ssh_info_public = if node_id['ssh_use_public_ip']
                                    true
                                  else
                                    false
                                  end
          end

          # Function HGFS in guest
          unless node_id['functional_hgfs'].nil?
            vmw.functional_hgfs = if node_id['functional_hgfs']
                                    true
                                  else
                                    false
                                  end
          end

          # Setup desktop environment
          unless node_id['desktop'].nil?
            if node_id['desktop']
              vmw.gui = true
              vmw.vmx['mks.enable3d'] = true
            end
          end

          # Setup Windows Server
          unless node_id['windows'].nil?
            if node_id['windows']
              # vmw.vmx['ethernet0.virtualdev'] = 'e1000'
              # We set this to false because we can use vagrant rdp
              # vmw.gui = false
              vmw.vmx['mks.enable3d'] = true
              # else
              #   vmw.vmx['ethernet0.pcislotnumber'] = '33'
            end
          end

          # Add additional disk(s)
          unless node_id['disks'].nil?
            vdiskmanager = 'vmware-vdiskmanager'
            dnum = 1
            vmdk_path = File.dirname(__FILE__)
            node_id['disks'].each do |disk_num|
              dnum = (dnum.to_i + 1)
              ddev = File.join(vmdk_path, "#{node_id['name']}_Disk#{dnum}.vmdk")
              dsize = "#{disk_num['size']}GB"
              unless File.file?(ddev)
                `#{vdiskmanager} -c -s #{dsize} -a lsilogic -t 0 #{ddev}`
              end
              vmw.vmx["scsi0:#{dnum}.filename"] = ddev.to_s
              vmw.vmx["scsi0:#{dnum}.present"] = true
              vmw.vmx["scsi0:#{dnum}.redo"] = ''
            end
          end
        end
      end

      # Provision network interfaces
      unless node_id['interfaces'].nil?
        node_id['interfaces'].each do |int|
          if int['method'] == 'dhcp'
            if int['network_name'] == 'None'
              node.vm.network 'private_network',
                              type: 'dhcp'
            end
            if int['network_name'] != 'None'
              node.vm.network 'private_network',
                              virtualbox__intnet: int['network_name'],
                              type: 'dhcp'
            end
          end
          next unless int['method'] == 'static'

          if int['network_name'] == 'None'
            node.vm.network 'private_network',
                            ip: int['ip'],
                            auto_config: int['auto_config']
          end
          next unless int['network_name'] != 'None'

          node.vm.network 'private_network',
                          virtualbox__intnet: int['network_name'],
                          ip: int['ip'],
                          auto_config: int['auto_config']
        end
      end

      # Port Forwards
      unless node_id['port_forwards'].nil?
        node_id['port_forwards'].each do |pf|
          node.vm.network 'forwarded_port', guest: pf['guest'],
                                            host: pf['host']
        end
      end

      # Windows RDP
      unless node_id['windows'].nil?
        if node_id['windows']
          node.vm.network 'forwarded_port', guest: 3389, host: 3389,
                                            host_ip: '127.0.0.1'
        end
      end

      # Provisioners
      unless node_id['provision'].nil?
        if node_id['provision']
          unless node_id['windows'].nil?
            # runs initial script
            if node_id['windows']
              node.vm.provision 'shell', path: 'scripts/bootstrap.ps1'
            else
              node.vm.provision 'shell', path: 'scripts/bootstrap.sh'
            end
          end
          unless node_id['provisioners'].nil?
            node_id['provisioners'].each do |provisioner|
              if provisioner['type'] == 'shell'
                unless provisioner['inline'].nil?
                  $script = <<-SCRIPT
                  #{provisioner['inline']}
                  SCRIPT
                  node.vm.provision 'shell',
                                    inline: $script,
                                    privileged: provisioner['privileged']
                end
                unless provisioner['path'].nil?
                  provisioner['path'].each do |script|
                    node.vm.provision 'shell',
                                      path: script,
                                      privileged: script['privileged']
                  end
                end
              elsif provisioner['type'] == 'ansible_local'
                provisioner['playbooks'].each do |playbook|
                  node.vm.provision 'ansible_local' do |ansible|
                    ansible.install_mode = 'pip'
                    ansible.playbook = playbook
                  end
                end
              end
            end
          end
          unless environment['provisioners'].nil?
            environment['provisioners'].each do |provisioner|
              if provisioner['type'] == 'shell'
                unless provisioner['inline'].nil?
                  $script = <<-SCRIPT
                  #{provisioner['inline']}
                  SCRIPT
                  node.vm.provision 'shell',
                                    inline: $script,
                                    privileged: provisioner['privileged']
                end
                unless provisioner['path'].nil?
                  provisioner['path'].each do |script|
                    node.vm.provision 'shell',
                                      path: script,
                                      privileged: script['privileged']
                  end
                end
              elsif provisioner['type'] == 'ansible_local'
                provisioner['playbooks'].each do |playbook|
                  node.vm.provision 'ansible_local' do |ansible|
                    ansible.install_mode = 'pip'
                    ansible.playbook = playbook
                  end
                end
              end
            end
          end
          if node_id == num_nodes
            # We only run Ansible playbooks when our host is not Windows
            # This does not affect ansible_local provisioners
            unless Vagrant::Util::Platform.windows?
              node.vm.provision 'ansible' do |ansible|
                ansible.limit = 'all'
                # Sets up host_vars
                ansible.playbook = 'playbooks/prep_host_vars.yml'
                ansible.groups = ansible_groups
              end
              node.vm.provision 'ansible' do |ansible|
                ansible.limit = 'all'
                # runs bootstrap Ansible playbook
                ansible.playbook = 'playbooks/bootstrap.yml'
                ansible.groups = ansible_groups
              end
              unless environment['provisioners'].nil?
                environment['provisioners'].each do |provisioner|
                  next unless provisioner['type'] == 'ansible'

                  provisioner['playbooks'].each do |playbook|
                    node.vm.provision 'ansible' do |ansible|
                      ansible.limit = 'all'
                      ansible.playbook = playbook
                      ansible.groups = ansible_groups
                    end
                  end
                end
              end
              # We run this last to ensure all previous provisioning completes
              node.vm.provision 'ansible' do |ansible|
                ansible.limit = 'all'
                # runs Ansible playbook for installing roles/executing tasks
                ansible.playbook = 'playbooks/playbook.yml'
                ansible.groups = ansible_groups
              end
            end
          end
        end
      end
    end
  end
end
