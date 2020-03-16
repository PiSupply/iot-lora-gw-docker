#!/bin/bash
#Move into directory
cd /opt/iotloragateway/iot-lora-gw-docker
#Pull latest updates from git
git pull

/opt/iotloragateway/iot-lora-gw-docker/4GInserted.sh

#Python Script that updates the 4G Config
python3 configure4Gmodule.py
