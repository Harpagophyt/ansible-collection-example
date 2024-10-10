motd
=========

A simple motd example

Requirements
------------

Nothing

Role Variables
--------------

You can set `motd_message` for a custom motd message 

Dependencies
------------

Nothing

Example Playbook
----------------

You can use the role like

    - hosts: servers
      roles:
         - role: motd
           motd_message: Your custom message

License
-------

BSD

