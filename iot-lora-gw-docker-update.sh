#!/bin/bash

#IoT LoRa Gateway Image Software
#Copyright (C) 2018-2019  Nebra LTD. T/a Pi Supply
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <https://www.gnu.org/licenses/>.


#Move into directory
cd /opt/iotloragateway/iot-lora-gw-docker

#Pull latest updates from git
git pull

install -m 644 iot-lora-gateway.service /lib/systemd/system/
install -m 644 iot-lora-gateway-restarter.service /lib/systemd/system/
install -m 644 iot-lora-gateway-eth-switcher.service /lib/systemd/system/
systemctl daemon-reload
systemctl enable iot-lora-gateway.service
systemctl enable iot-lora-gateway-restarter.service
systemctl enable iot-lora-gateway-eth-switcher.service
#Reset GPIO Pins
/opt/iotloragateway/iot-lora-gw-docker/reset-22.sh
/opt/iotloragateway/iot-lora-gw-docker/reset-38.sh
/opt/iotloragateway/iot-lora-gw-docker/reset-39.sh

#Run 4G Part
/opt/iotloragateway/iot-lora-gw-docker/4GInserted.sh

#Python Script that updates the 4G Config
/opt/iotloragateway/iot-lora-gw-docker/configure4Gmodule.py
#And to update the wifi
/opt/iotloragateway/iot-lora-gw-docker/configureWiFi.py
