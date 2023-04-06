#!/usr/bin/env bash
# sets up web servers for deployment of static content
sudo apt-get update -y
sudo apt-get install -y nginx
path='/data/web_static/current'
if [ -e $path ]
    then
        sudo rm /data/web_static/current
fi

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "<html>
 <head>
 </head>
 <body>
  Holberton School
 </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
name=$(hostname)
echo "server {
listen 80 default_server;
listen [::]:80 default_server;
root /var/www/html;
index index.html;
add_header X-Served-By $name;
location /redirect_me {
return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
}
error_page 404 /404.html;
location = /404.html{
internal;
}
location /hbnb_static/ {
alias /data/web_static/current/;
autoindex off;
}
}" > default
sudo mv -f default /etc/nginx/sites-available/default
sudo service nginx restart
