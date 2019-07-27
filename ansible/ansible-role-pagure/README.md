pagure
======

Pagure deployment role for RHEL/CentOS 7 and Fedora 22+.

Role Variables
--------------

See `defaults/main.yml`.

Dependencies
------------

* nestihacky.common https://github.com/nestihacky/ansible-role-common
* nestihacky.gitolite https://github.com/nestihacky/ansible-role-gitolite
* nestihacky.apache https://github.com/nestihacky/ansible-role-apache
* nestihacky.postgresql https://github.com/nestihacky/ansible-role-postgresql
* nestihacky.mailserver https://github.com/nestihacky/ansible-role-mailserver

Example Playbook
----------------

    ---
    - hosts: pagure
      sudo: yes
        roles:
        - nestihacky.pagure

License
-------

BSD

Author Information
------------------

* http://base48.cz
* https://github.com/nestihacky/ansible-role-template
