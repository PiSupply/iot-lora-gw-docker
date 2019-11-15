#Configure Packet Forwarder Program
#Configures the packet forwarder based on the YAML File and Env Variable
import os
import yaml
import json
from pprint import pprint
moduleId = int(os.environ['LORAMODULE'])
#moduleId = 0

with open("/opt/iotloragateway/config/gateway_configuration.yml", 'r') as yamlFile:
    try:
        if(moduleId == 0):
            config = yaml.safe_load(yamlFile)
            configLora = config['packet-forwarder-1']
        elif(moduleId == 1):
            config = yaml.safe_load(yamlFile)
            configLora = config['packet-forwarder-2']
        else:
            die()
    except yaml.YAMLError as exc:
        print(exc)
#print(config)

#print(configLora)


with open('local_conf.json') as jsonFile:
    newConfig = json.load(jsonFile)



#Fill out the JSON File from the YAML File
newConfig['gateway_conf']['contact_email'] = config['user']['email-address']
newConfig['gateway_conf']['description'] = config['gateway-info']['gateway-description']
newConfig['gateway_conf']['gateway_ID'] = configLora['packet-forwarder-eui']

newConfig['gateway_conf']['ref_altitude'] = config['location']['alt']
newConfig['gateway_conf']['ref_latitude'] = config['location']['lat']
newConfig['gateway_conf']['ref_longitude'] = config['location']['lon']


newConfig['gateway_conf']['servers'][0]['server_address'] = configLora['router']
#if ttn
if(configLora['providerType'] == "TTN"):
    newConfig['gateway_conf']['servers'][0]['serv_type'] = "ttn"
    newConfig['gateway_conf']['servers'][0]['serv_gw_key'] = configLora['packet-forwarder-key']
    newConfig['gateway_conf']['servers'][0]['serv_gw_id'] = configLora['packet-forwarder-id']
    newConfig['gateway_conf']['servers'][0]['serv_port_up'] = 1700
    newConfig['gateway_conf']['servers'][0]['serv_port_down'] = 1700

#If Loriot
elif(configLora['providerType'] == "LORIOT"):
    newConfig['gateway_conf']['servers'][0]['serv_type'] = "semtech"
    newConfig['gateway_conf']['servers'][0]['serv_port_up'] = 1700
    newConfig['gateway_conf']['servers'][0]['serv_port_down'] = 1700

else:
    newConfig['gateway_conf']['servers'][0]['serv_type'] = "semtech"
    newConfig['gateway_conf']['servers'][0]['serv_port_up'] = 1700
    newConfig['gateway_conf']['servers'][0]['serv_port_down'] = 1700

#GPS Module
if(config['gps']['enabled'] == True):
    newConfig['gateway_conf']['gps'] = True;
    newConfig['gateway_conf']['fake_gps'] = False;

else:
    newConfig['gateway_conf']['gps'] = True;
    newConfig['gateway_conf']['fake_gps'] = False;

#pprint(newConfig)

with open('local_conf.json', 'w') as jsonOut:
    json.dump(newConfig, jsonOut)
