gitolite
========

Gitolite.

Role Variables
--------------

See also `defaults/main.yml`.

Dependencies
------------

* nestihacky.git_core https://github.com/nestihacky/ansible-role-git-core
* nestihacky.git_daemon https://github.com/nestihacky/ansible-role-git-daemon

Example Playbook
----------------

    ---
    - hosts: gitolite
      sudo: yes
        roles:
        - nestihacky.gitolite

License
-------

BSD

Author Information
------------------

* http://base48.cz
* https://github.com/nestihacky/ansible-role-gitolite
