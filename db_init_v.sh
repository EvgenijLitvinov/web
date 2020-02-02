# !/bin/bash

sudo /etc/init.d/mysql start
mysql -uroot -e "create database first_db;"
mysql -uroot -e "grant all privileges on first_db.* to 'uuserr'@'localhost' with grant option;"
python3 ask/manage.py makemigrations
python3 ask/manage.py migrate
