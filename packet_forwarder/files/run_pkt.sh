#!/usr/bin/env bash

#Run Packetforward
#This script runs on the boot of the container

python3 configurePktFwd.py

#Run the configuration script for the packet forwarder

#Reset the packet forwarder

if [ ! -d "/sys/class/gpio/gpio22" ]; then
    echo "22" > /sys/class/gpio/export
fi
echo "out" > /sys/class/gpio/gpio22/direction
echo "1" > /sys/class/gpio/gpio22/value
sleep 1
echo "0" > /sys/class/gpio/gpio22/value
sleep 1

#Run the packet forwarder
./packetforwarder_hat
