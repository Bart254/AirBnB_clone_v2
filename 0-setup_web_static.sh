#!/usr/bin/env bash
# Setting up web server for deployment
# installing nginx web server
 apt-get -y update
 apt-get -y install nginx

# creating the required directories
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

# creating an HTML file
touch  /data/web_static/releases/test/index.html
line1='<html>'
line3='  <head>'
line4='  </head>'
line5='  <body>'
line51='    <p>'
line52='     Holberton School'
line53='    </p>'
line6='  </body>'
line7='</html>'
echo -e "$line1\n$line3\n$line4\n$line5\n$line51\n$line52\n$line53\n$line6\n$line7" > /data/web_static/releases/test/index.html

# creating a symbolic link to dir /data/web_static/releases
 ln -sf '/data/web_static/releases/test' '/data/web_static/current'

# change ownership and group of /data folder to ubuntu
chown -R ubuntu /data
chgrp -R ubuntu /data
chmod -R 755 /data/
# updating nginx configuration to serve content of /test/index.html when path is hbnb_static
sudo sed -i '48 i \\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
# restart Nginx
service nginx restart
# ensure program exits succcessfully
exit 0
