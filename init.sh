#!/bin/bash

if [ -f /etc/nginx/sites-enabled/default ]; then
  sudo rm /etc/nginx/sites-enabled/default
fi

# Nginx
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

# Gunicorn
sudo ln -sf /home/box/web/etc/gunicorn_hello.conf /etc/gunicorn.d/test
sudo ln -sf /home/box/web/etc/gunicorn_ask.conf /etc/gunicorn.d/ask
sudo /etc/init.d/gunicorn restart

# MySQL
sudo service mysql restart
sudo mysql -uroot -e "CREATE DATABASE qa CHARACTER SET utf8 COLLATE utf8_general_ci;"
sudo mysql -uroot -e "GRANT ALL PRIVILEGES ON qa.* TO 'qa_user'@'localhost' IDENTIFIED BY '123456789';"
