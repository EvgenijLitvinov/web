# !/bin/bash

# Nginx
sudo ln -sf /home/andrtem/stepik/repo/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

# Gunicorn
sudo gunicorn -c hello.py hello:wsgi_app &
cd ask
sudo gunicorn -b 0.0.0.0:8000 ask.wsgi:application

