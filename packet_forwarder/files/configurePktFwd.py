#Configure Packet Forwarder Program
#Configures the packet forwarder based on the YAML File and Env Variable
import os
import yaml
moduleId = int(os.environ['LORAMODULE'])




with open("/opt/iotloragateway/config/gateway_configuration.yml", 'r') as stream:
    try:
        if(moduleId == 0):
            config = yaml.safe_load(stream)['packet-forwarder-1']
        elif(moduleId == 1):
            config = yaml.safe_load(stream)['packet-forwarder-2']
        else:
            die()
    except yaml.YAMLError as exc:
        print(exc)
print(config)
