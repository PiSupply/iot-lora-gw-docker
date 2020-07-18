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

#Configure 4G Module
#Configures the 4G Module based on the YAML File
import os
import yaml
import json
from pprint import pprint
from time import sleep
import subprocess

#Open the YAML
with open("/opt/iotloragateway/config/gateway_configuration.yml", 'r') as yamlFile:
    try:
        config = yaml.safe_load(yamlFile)
        configLte = config['lte-modem']
    except yaml.YAMLError as exc:
        print(exc)

connectionName = "iot5g"

#Take the connection down
subprocess.call(['nmcli', "connection", "down" , connectionName])

#Reconfigure all the things
#First the phone number, altough this is rare to change
subprocess.call(['nmcli', "connection", "modify" , connectionName, "gsm.number", configWifi['number']])
#APN
subprocess.call(['nmcli', "connection", "modify" , connectionName, "gsm.apn", configWifi['apn']])
#Username
subprocess.call(['nmcli', "connection", "modify" , connectionName, "gsm.username", configWifi['username']])
#Password
subprocess.call(['nmcli', "connection", "modify" , connectionName, "gsm.password", configWifi['password']])

#And... Back up
subprocess.call(['nmcli', "connection", "up" , connectionName])
