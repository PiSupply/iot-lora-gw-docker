#!/usr/bin/env bash

#This script runs on the boot of the container

#We need to check that 1) There is an SSL Certificate and 2) The Cert has 7 Days left on it

if [ ! -f "/opt/iotloragateway/ssl/iotloragateway.key" ]; then
  openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /opt/iotloragateway/ssl/iotloragateway.key -out /opt/iotloragateway/ssl/iotloragateway.crt  -subj "/C=GB/ST=Kent/L=Tunbridge Wells/O=Global Security/OU=IT Department/CN=iotloragateway"
fi
if [ ! -f "/opt/iotloragateway/ssl/dhparam.pem" ]; then
  openssl dhparam -out /opt/iotloragateway/ssl/dhparam.pem 2048
fi

if [ ! -f "/opt/iotloragateway/config/gateway_configuration.yml" ]; then
  cp /opt/iotloragateway/controller/gateway_configuration.yml /opt/iotloragateway/config/gateway_configuration.yml
  chmod 755 /opt/iotloragateway/config/gateway_configuration.yml
fi

#For development only overwrite the configuration file
#cp /opt/iotloragateway/controller/gateway_configuration.yml /opt/iotloragateway/config/gateway_configuration.yml

chown www-data:www-data /opt/iotloragateway/config/gateway_configuration.yml
chmod 755 /opt/iotloragateway/config/gateway_configuration.yml


service php7.3-fpm start
nginx -g "daemon off;"
