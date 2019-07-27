Composer
========

PHP Composer role for RHEL/CentOS 7 and Fedora 22+.

Installs Composer for specified SCL PHP version,
creates wrapper for calling with SCL PHP - scl-composer-phpXY.

Role Variables
--------------

    composer_php_scl_version: 55
    composer_install_path: /usr/local/bin

Dependencies
------------

None.

Example Playbook
----------------

    ---
    - hosts: composer
      sudo: yes
        roles:
        - nestihacky.composer

License
-------

BSD

Author Information
------------------

* http://base48.cz
* https://github.com/nestihacky/ansible-role-composer
