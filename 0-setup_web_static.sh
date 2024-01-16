#!/usr/bin/env bash
# Setting up web server for deployment
# installing nginx web server
 apt-get -y update
 apt-get -y install nginx

# creating the required directories
if [ ! -e /data/ ]; then
	 mkdir -p /data/
fi
if [ ! -e /data/web_static/ ]; then
         mkdir -p /data/web_static/
fi
if [ ! -e /data/web_static/releases/ ]; then
         mkdir -p /data/web_static/releases/
fi
if [ ! -e //data/web_static/shared ]; then
         mkdir -p /data/web_static/shared/
fi
if [ ! -e  /data/web_static/releases/test/ ]; then
         mkdir -p  /data/web_static/releases/test/
fi

# creating an HTML file
if [ ! -e /data/web_static/releases/test/index.html ]; then
	 touch  /data/web_static/releases/test/index.html

	# Filling the html file with data
	line1='<!DOCTYPE html>'
	line2='<html lang="en">'
	line3='<head>'
	line31='<meta charset="UTF-8">'
	line32='<meta name="viewport" content="width=device-width, intial-scale=1">'
	line33='<title>Website Deployment</title>'
	line4='</head>'
	line5='<body>'
	line51='<p>Welcome to Web Deployment using Fabric API</p>'
	line6='</body>'
	line7='</html>'
	echo -e "$line1\n$line2\n\t$line3\n\t\t$line31\n\t\t$line32\n\t\t$line33\n\t$line4\n\t$line5\n\t\t$line51\n\t$line6\n$line7" |  tee -a /data/web_static/releases/test/index.html
fi
# creating a symbolic link to dir /data/web_static/releases
if [ -L '/data/web_static/current' ]; then
	 rm -f '/data/web_static/current'
fi
 ln -s '/data/web_static/releases/test' '/data/web_static/current'

# change ownership and group of /data folder to ubuntu
 chown -R ubuntu /data
 chgrp -R ubuntu /data

# updating nginx configuration to serve content of /test/index.html when path is hbnb_static
line1='location /hbnb_static {'
if ! grep -q "$line1" /etc/nginx/sites-available/default; then
	line2='rewrite ^/hbnb_static$ /hbnb_static/;'
	line3='alias /data/web_static/current/;'
	line4='}'
	 sed -i "/location \/ {/i \ \t$line1\n\t\t$line2\n\t\t$line3\n\t$line4" /etc/nginx/sites-available/default

	# restart Nginx
	 service nginx restart
fi

# ensure program exits succcessfully
exit 0
