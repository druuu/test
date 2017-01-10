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
