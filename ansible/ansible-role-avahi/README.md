avahi
=====

Avahi role for RHEL/CentOS 7 and Fedora 22+.

Installs and enables avahi-daemon so we can reach our development
instance via `nestihacky.local`.

Role Variables
--------------

None.

Dependencies
------------

None.

Example Playbook
----------------

    ---
    - hosts: avahi
      sudo: yes
        roles:
        - nestihacky.avahi

License
-------

BSD

Author Information
------------------

* http://base48.cz
* https://github.com/nestihacky/ansible-role-template
