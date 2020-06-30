#!/usr/bin/python3
import os
from time import sleep

#IoT LoRa Rebooter Script

while True:
    #Lets check the file
    f = open("/opt/iotloragateway/config/rebooter.txt", "r")
    state = str(f.read())
    f.close()

    #Restart Docker & update
    if(state == "restart"):
        #Wipe the file
        f = open("/opt/iotloragateway/config/rebooter.txt", "w")
        f.write("")
        f.close()
        #Restart the service
        os.system("systemctl restart iot-lora-gateway.service");
        #Sleep 2 Minutes
        sleep(120)

    #Reboot entire gateway
    elif(state == "reboot"):
        #Wipe the file
        f = open("/opt/iotloragateway/config/rebooter.txt", "w")
        f.write("")
        f.close()
        #Restart the service
        os.system("shutdown -r now");


    #Shutdown the gaetway
    elif(state == "shutdown"):
        #Wipe the file
        f = open("/opt/iotloragateway/config/rebooter.txt", "w")
        f.write("")
        f.close()
        #Restart the service
        os.system("shutdown -h now");


    else:
        sleep(15)
        print("Sleep")
