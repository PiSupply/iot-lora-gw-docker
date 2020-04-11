#!/bin/bash

#Move into directory
cd /opt/iotloragateway/iot-lora-gw-docker
#Update the OS
apt-get update
apt-get upgrade -y

docker-compose down -v

#Pull latest containers from docker
docker-compose pull

#Start docker container
docker-compose up
