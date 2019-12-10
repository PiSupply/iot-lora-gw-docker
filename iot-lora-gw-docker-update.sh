#!/bin/bash
cd /opt/iotloragateway/iot-lora-gw-docker
git pull
docker-compose pull
install -m 644 iot-lora-gateway.service /lib/systemd/system/
systemctl daemon-reload
systemctl enable iot-lora-gateway.service
