local_git_deploy
================

Pushes current branch of git repo from local machine to remote machine (or
local VM). Useful for workflows like:

1. Develop in local repo
2. Push repo to remote machine
3. Compile/install the application
4. Run the application/tests
5. GOTO 1.

This role is useful for step 2, you probably also want ansible to perform steps
3 and possibly 4.

Requirements
------------

Git on remote machine. Sshd listening on the remote machine.

Role Variables
--------------

* `local_git_deploy_local_repo` (required): Path to the repository on local machine.
* `local_git_deploy_remote_repo` (required): Path to the repository on remote machine.
* `local_git_deploy_remote_branch`: (default `deploy`): Name of the branch on the remote machine to push to.
* `local_git_deploy_ssh_port` (default 22): SSH port to use when connecting to remote machine.

Dependencies
------------

No dependencies?

Example Playbook
----------------

    - hosts: myservice-devel
      roles:
         - role: local_git_deploy
           local_git_deploy_local_repo: /home/jdoe/repos/myservice
           local_git_deploy_remote_repo: /opt/myservice

License
-------

WTFPL

Author Information
------------------

* Martin Milata `<b42@srck.net>`
