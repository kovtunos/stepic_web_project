#!/bin/bash

case "$1" in
mysql)
  if [ -f /etc/nginx/sites-enabled/default ]; then
    sudo rm /etc/nginx/sites-enabled/default
  fi

  # Nginx
  sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/ask.conf
  sudo /etc/init.d/nginx restart

  # Gunicorn (ver. 17.5)
  sudo ln -sf /home/box/web/etc/gunicorn_ask.conf /etc/gunicorn.d/ask
  sudo /etc/init.d/gunicorn restart

  # MySQL
  echo 'innodb_use_native_aio = 0' | sudo tee --append /etc/mysql/my.cnf
  sudo service mysql restart
  sudo mysql -uroot -e "CREATE DATABASE ask CHARACTER SET utf8 COLLATE utf8_general_ci;"
  sudo mysql -uroot -e "GRANT ALL PRIVILEGES ON ask.* TO 'ask_user'@'localhost' IDENTIFIED BY '123456789';"

  echo 'syncing db...'
  python /home/box/web/ask/manage.py syncdb
;;

sqlite)
  sudo /etc/init.d/gunicorn stop
  sudo /etc/init.d/nginx stop
  sudo /etc/init.d/mysql stop
  echo 'syncing db...'
  python /home/box/web/ask/manage.py syncdb
;;

*)
  echo "Provide an argument:"
  echo "mysql"
  echo "sqlite"
esac
exit 0
