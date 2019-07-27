mailman
=======

Mailman configuration role.

Role Variables
--------------

Role supports following variables:

    mailman_admin: admin@example.org
    mailman_domain: lists.example.org
    mailman_password: CHANGE_ME

See also `defaults/main.yml`.

Dependencies
------------

- nestihacky.apache
- nestihacky.mailserver

License
-------

This role is based on the Sovereign playbooks (https://github.com/sovereign/sovereign) which are
under GPLv3 except files and templates based on third-party software which should be considered
under their respective licenses.

Author Information
------------------

* http://base48.cz
* https://github.com/nestihacky/ansible-role-mailman
