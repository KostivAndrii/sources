graphite
========

Simple [Graphite and Carbon](https://graphite.readthedocs.org/) deployment for RHEL/CentOS 7.

Role Variables
--------------

You NEED to set the virtual host the web interface will run under and the Django CSRF key:

    graphite_vhost: graphite.example.com
    graphite_secret_csrf_key: eeLahch5Ahqueih8chuthi9A

The role allows you to set on which interfaces and ports the Carbon daemon listens:

    graphite_line_interface: 0.0.0.0
    graphite_line_port: 2003
    graphite_udp_enabled: false
    graphite_udp_interface: 0.0.0.0
    graphite_udp_port: 2003
    graphite_pickle_interface: 0.0.0.0
    graphite_pickle_port: 2004
    graphite_cache_query_interface: 0.0.0.0
    graphite_cache_query_port: 7002

You can optionally configure the Carbon storage schemas using this playbook:

    graphite_manage_storage_schemas: true
    graphite_storage_schemas:
    - name: carbon
      pattern: ^carbon\.
      retentions: 60:90d
    - name: default_1min_for_1day
      pattern: .*
      retentions: 60s:1d

Dependencies
------------

Needs httpd installed. To use this role you'll probably need to open the carbon ports on your firewall and configure who can access the web interface in your httpd configuration.

Example Playbook
----------------

    - hosts: servers
      roles:
         - role: nestihacky.graphite
           graphite_vhost: graphite.example.com
           graphite_secret_csrf_key: eeLahch5Ahqueih8chuthi9A

License
-------

MIT

Author Information
------------------

* based on graphite/graphite role from [Fedora Infrastructure playbooks](https://infrastructure.fedoraproject.org/cgit/ansible.git/tree/roles/graphite/graphite)
* http://base48.cz
