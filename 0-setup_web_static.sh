#!/usr/bin/env bash
# Sets up a web server for deployment of web_static.

# Update package lists and install nginx
apt-get update
apt-get install -y nginx

# Create directories for web_static deployment
mkdir -p /var/www/html/web_static/releases/test/
mkdir -p /var/www/html/web_static/shared/

# Create a simple index.html file
echo "Holberton School" > /var/www/html/web_static/releases/test/index.html

# Create a symbolic link to the latest version of web_static
ln -sf /var/www/html/web_static/releases/test/ /var/www/html/web_static/current

# Set appropriate ownership and permissions
chown -R www-data:www-data /var/www/html/web_static/
chmod -R 755 /var/www/html/web_static/

# Configure Nginx
cat > /etc/nginx/sites-available/default <<EOF
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By \$HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /var/www/html/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://cuberule.com/;
    }

    error_page 404 /404.html;
    location = /404.html {
        root /var/www/html;
        internal;
    }
}
EOF

# Restart Nginx to apply changes
service nginx restart
