mediawiki
=========

(experimental) MediaWiki role for RHEL/CentOS 7 and Fedora 22+.

Installs and enables MediaWiki with extensions.
Designed to work with SCL (Software collections).

Role Variables
--------------

See defaults/main.yml

Dependencies
------------

- nestihacky.apache
- nestihacky.memcached
- nestihacky.scl
- nestihacky.composer
- nestihacky.mailserver

Example Playbook
----------------

    ---
    - hosts: mediawiki
      sudo: yes
        roles:
        - nestihacky.mediawiki

License
-------

BSD

Author Information
------------------

* http://base48.cz
* https://github.com/nestihacky/ansible-role-mediawiki
