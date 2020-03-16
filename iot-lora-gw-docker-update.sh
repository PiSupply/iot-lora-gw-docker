#!/bin/bash
#Move into directory
cd /opt/iotloragateway/iot-lora-gw-docker
#Pull latest updates from git
git pull

#Reset GPIO Pins
python3 gpioReset.py

#Run 4G Part
/opt/iotloragateway/iot-lora-gw-docker/4GInserted.sh

#Python Script that updates the 4G Config
python3 configure4Gmodule.py
