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


##Block All incoming and outgoing traffic except for specific IP

* Create a shell script with name block.sh and following contents:

    ```
    #!/bin/sh

    iptables --policy INPUT DROP
    iptables -P FORWARD DROP
    
    iptables -A INPUT -s your_ip_address -j ACCEPT

    iptables-save
    ```
 * Replace your_ip_address with your ip address
* Make the file executable:

    ```
    sudo chmod +x block.sh
    ```
* Run the script:

    ```
    sudo sh block.sh
    ```
