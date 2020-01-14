#!/bin/bash
#Move into directory
cd /opt/iotloragateway/iot-lora-gw-docker
#Update the OS
apt-get update
apt-get upgrade -y
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



#Python Script that updates the 4G Config
python3 configure4Gmodule.py
