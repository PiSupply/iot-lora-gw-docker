#!/usr/bin/python3
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

#Configure Wi-Fi Module
#Configures the Wi-Fi Module based on the YAML File

import os
import yaml
import json
from pprint import pprint

from time import sleep

#Easiest method, replace the entire file each time.


with open("/opt/iotloragateway/config/gateway_configuration.yml", 'r') as yamlFile:
    try:
        config = yaml.safe_load(yamlFile)
        configWifi = config['wifi']
    except yaml.YAMLError as exc:
        print(exc)

wpa_supp = open("/etc/wpa_supplicant/wpa_supplicant.conf", "w")

wpa_supp.write("""
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=%s

network={
 ssid="%s"
 psk="%s"
}
""" % (configWifi['region'], configWifi['ssid'], configWifi['password']))
