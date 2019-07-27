memcached
=========

Memcached role for RHEL/CentOS 7 and Fedora 22+.

Installs and enables memcached.

Role Variables
--------------

    memcached_port: 11211
    memcached_user: memcached
    memcached_maxconn: 1024
    memcached_cachesize: 64
    memcached_options:  # additional options to pass to memcached

Dependencies
------------

None.

Example Playbook
----------------

    ---
    - hosts: memcached
      sudo: yes
        roles:
        - nestihacky.memcached

License
-------

BSD

Author Information
------------------

* http://base48.cz
* https://github.com/nestihacky/ansible-role-memcached
