##Enable SSH access

* Create **.ssh** directory in the home directory if doesn't exist.

    ```
    mkdir ~/.ssh
    ```
* Create a file with name **authorized\_keys** and copy your public key.

    ```
    nano ~/.ssh/authorized_keys
    ```
* Restart ssh service.

    ```
    sudo service ssh restart
    ```


##Disable SSH Password Authentication

* Open /etc/ssh/sshd_config and add the following line

    ```
    PasswordAuthentication no
    ```
* Restart ssh service.
    
    ```
    sudo service ssh restart
    ```


##Block All incoming and outgoing traffic except for specified IP

    ```
    #!/bin/sh

    iptables --policy INPUT DROP
    iptables -P FORWARD DROP
    
    iptables -A INPUT -s 183.82.113.154 -j ACCEPT
    ```
