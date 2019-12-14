#!/bin/bash
#Move into directory
cd /opt/iotloragateway/iot-lora-gw-docker
#Pull latest updates from git
git pull
#Pull latest containers from docker
docker-compose pull
#Update service
install -m 644 iot-lora-gateway.service /lib/systemd/system/
#Reload services
systemctl daemon-reload
#Re-enable service
systemctl enable iot-lora-gateway.service

#Update 4G Configuration
