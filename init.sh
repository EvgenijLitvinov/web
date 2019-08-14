sudo ln -sf /home/andrtem/stepik/repo/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo gunicorn -c hello.py hello:wsgi_app &
#sudo gunicorn -c dj_gun_conf.py ask.wsgi:application &


