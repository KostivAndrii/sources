Role Name
========

Ansible role which installs and configures PostgreSQL, extensions, databases and users.


Role Variables
--------------
```yaml
# Basic settings
postgresql_encoding: 'UTF-8'
postgresql_locale: 'en_US.UTF-8'

postgresql_admin_user: "postgres"
postgresql_default_auth_method: "trust"

# List of databases to be created (optional)
postgresql_databases:
  - name: foobar
    hstore: yes         # flag to install the hstore extensions on this database (yes/no)

# List of users to be created (optional)
postgresql_users:
  - name: john
    pass: pass
    encrypted: no       # denotes if the password is already encrypted.

# List of user privileges to be applied (optional)
postgresql_user_privileges:
  - name: john         # user name
    db: foobar         # database
    priv: "ALL"        # privilege string format: example: INSERT,UPDATE/table:SELECT/anothertable:ALL
                       #   N.B. ALL only provides all *database* privileges, but
                       #   no table privileges

# List of object privileges to be applied
postgresql_user_object_privileges:
  - name: john             # user name
    db: foobar             # database
    type: table            # type of db object on which to set privilege
    priv: ALL              # list of privileges (e.g. INSERT,SELECT)
    objs: 'ALL_IN_SCHEMA'  # list of db objects on which to set privilege
  - name: john             # user name
    db: foobar             # database
    type: sequence         # type of db object on which to set privilege
    priv: ALL              # list of privileges (e.g. INSERT,SELECT)
    objs: 'ALL_IN_SCHEMA'  # list of db objects on which to set privilege
```

Dependencies
------------

No other roles are needed.

Example Playbook
-------------------------
```yaml
# file: localrepo.yml
- hosts: postgres
  sudo: yes
  sudo_user: root
  roles:
    - nestihacky.postgresql
```
License
-------

MIT

Author Information
------------------

* http://base48.cz
* https://github.com/nestihacky/ansible-role-postgresql
* Based on https://github.com/Open-Future-Belgium/PostgreSQL/
