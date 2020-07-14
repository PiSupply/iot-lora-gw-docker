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

#This program will check if it can ping the server below for internet connectivity
#On each interface one by one and change the priority accordingly.

#Gateways can be configured with 3 methods, The onboard ethernet, Wi-Fi & LTE.
#Priority should be Ethernetm Then Wi-FI (if detected) then LTE.
#We don't need to ping via LTE as if the other connections are not up then even
#if LTE is down then it won't matter.

import os
from time import sleep
from pythonping import ping
import ifcfg
import json
import subprocess


#Let's ping google dns
PING_SERVER = "8.8.8.8" #If we can't access google, there's a 99.99% chance it's our internet.
WI_FI = 0 #As default we'll say there is no wi-fi module.
LTE = 0 #As default we'll say there is no LTE module.
CURRENT_INTERFACE = 0 #Use this to keep track of the interface being used

#Check if Wi-Fi or LTE adaptors are plugged in
for name, interface in ifcfg.interfaces().items():
    # do something with interface
    device = interface['device']
    if(device  == "wlan0"):
        WI_FI = 1
    if(device == "wwan0"):
        LTE = 1

#If WiFi or LTE are not plugged in then there is no point in running, go into endless sleep loop.

if(WI_FI == 0 and LTE == 0):
    print("No Wi-Fi or LTE adaptors detected.")
    while True:
        sleep(300)

#Lets re-assign priorities anyway to be in an order.
#eth0 = 10, wlan0 = 20, wwan = 30, if the device goes offline we add 30
#so eth would = 40, wlan would equal 50. WWAN should never need changing.

#Set the eth0
subprocess.call(['ifmetric', "eth0", "10"])

print("Network interfaces detected:")
if(WI_FI):
    print("Wi-Fi Adaptor Found")
    subprocess.call(['ifmetric', "wlan0", "20"])
if(LTE):
    print("LTE Adaptor Found")
    subprocess.call(['ifmetric', "wwan0", "30"])

print("Priorities reconfigured")



while True:
    #First check eth0
    eth0_ping = subprocess.call(['ping', '-I','eth0', '-c' ,'1', '-t' , '15', '127.0.0.2'])
    if(eth0_ping>0):
        print("Connection lost")
        if(WI_FI):
            #lets try WiFi
            wlan_ping = subprocess.call(['ping', '-I','wlan0', '-c' ,'1', '-t' , '15', PING_SERVER])
        elif(LTE):
            #lets try LTE
            lte_ping = subprocess.call(['ping', '-I','wwan0', '-c' ,'1', '-t' , '15', PING_SERVER])
        else:
            print("Complete failure?")



    sleep(60)
