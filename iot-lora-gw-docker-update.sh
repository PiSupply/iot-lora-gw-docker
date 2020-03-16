#!/bin/bash
#Move into directory
cd /opt/iotloragateway/iot-lora-gw-docker
#Pull latest updates from git
git pull

#Reset GPIO Pins
/opt/iotloragateway/iot-lora-gw-docker/reset-22.sh
/opt/iotloragateway/iot-lora-gw-docker/reset-38.sh
/opt/iotloragateway/iot-lora-gw-docker/reset-39.sh

#Run 4G Part
/opt/iotloragateway/iot-lora-gw-docker/4GInserted.sh

#Python Script that updates the 4G Config
python3 configure4Gmodule.py
