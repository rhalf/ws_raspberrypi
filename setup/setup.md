1. download os from https://www.raspberrypi.org/software/operating-systems/

2.1 install via raspberrypi-imager
    2.1.1 reformat
    2.1.2 write to sd card

2.2 install via 3rd party
    2.2.1 reformat using sdcarf formatter
    2.2.2 write to sd card using win32 disk imager

3. insert sd card to the raspberry pi
4. set location language and keboard
5. set password
6. connect to wifi
7. auto update will prompt
    7.1 download updates
    7.2 install updates
    7.3 reboot
8. go to raspi-configuration
    8.1 boot on cli.
    8.2 enable all except serial console
    8.3 reboot
    
9. login
    9.1 install pip
        sudo apt-get install python3-pip
    9.2 install python3 mysql driver
        sudo apt-get install python3-mysqldb
    9.3 install mariadb server
        sudo apt install mariadb-server

10. setup mariadb server using
    sudo mysql_secure_installation

    10.1  just hit enter
    10.2  set password? yes
    10.3  password: "raspberry"
    10.4  remove anonymous? yes
    10.5 disallow root remotely? no
    10.6 remove test db? no
    10.7 reload privilege? yes

11. setup privilege mariadb server

    11.1 enter
       GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'raspberry';

    11.2 update server conf
        sudo nano /etc/mysql/mariadb.conf.d/50-server.cnf
        update bind-address = 127.0.0.1 to bind-address=*

12. copy connection.py from raspberry/day3 then run

13. set wifi to respective group.

14. copy using raspberry pi copier