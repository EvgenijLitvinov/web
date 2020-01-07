# !/bin/bash

sudo /etc/init.d/mysql start
sudo mysql -uroot -e "create database first_db;"
sudo mysql -uroot -e "create user 'uuserr'@'localhost';"
sudo mysql -uroot -e "grant all privileges on first_db.* to 'uuserr'@'localhost' with grant option;"

