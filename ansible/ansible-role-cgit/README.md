cgit
====

cgit on apache2 setup

Role Variables
--------------

See also `defaults/main.yml`.

Dependencies
------------

* nestihacky.common https://github.com/nestihacky/ansible-role-common
* nestihacky.git_core https://github.com/nestihacky/ansible-role-git-core

Example Playbook
----------------

    ---
    - hosts: cgit
      sudo: yes
        roles:
        - nestihacky.cgit


License
-------

BSD

Author Information
------------------

* http://base48.cz
* https://github.com/nestihacky/ansible-role-cgit
