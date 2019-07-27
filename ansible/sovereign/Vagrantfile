# -*- mode: ruby -*-

Vagrant.configure("2") do |config|
  #
  # Common Settings
  #

  config.vm.hostname = "sovereign.local"
  config.vm.network "private_network", ip: "192.168.222.2"

  config.vm.provision :ansible do |ansible|
    ansible.playbook = "site.yml"
    ansible.host_key_checking = false
    ansible.extra_vars = { ansible_ssh_user: "vagrant", testing: true }

    # ansible.tags = ["blog"]
    # ansible.skip_tags = ["openvpn"]
    ansible.verbose = "v"
  end

  config.vm.provider :virtualbox do |v|
    v.memory = 512
  end

  config.vm.provider :vmware_fusion do |v|
    v.vmx["memsize"] = "512"
  end

  ##
  ## vagrant-cachier
  ##
  ## Install the plugin by running: vagrant plugin install vagrant-cachier
  ## More information: https://github.com/fgrehm/vagrant-cachier
  ##

  #if Vagrant.has_plugin? "vagrant-cachier"
  #  config.cache.enable :apt
  #  config.cache.scope = :box
  #end

  #
  # Centos 7
  #

  config.vm.define "centos", primary: true do |centos|
    centos.vm.box = "centos/7"
  end
end
