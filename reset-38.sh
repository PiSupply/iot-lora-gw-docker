#!/usr/bin/env bash

if [ ! -d "/sys/class/gpio/gpio38" ]; then
    echo "38" > /sys/class/gpio/export
fi
echo "out" > /sys/class/gpio/gpio38/direction
echo "1" > /sys/class/gpio/gpio38/value
sleep 1
echo "0" > /sys/class/gpio/gpio38/value
sleep 1
