#!/usr/bin/env bash
whoami
if [ ! -d "/sys/class/gpio/gpio39" ]; then
    echo "39" > /sys/class/gpio/export
fi
echo "out" > /sys/class/gpio/gpio39/direction
echo "1" > /sys/class/gpio/gpio39/value
sleep 1
echo "0" > /sys/class/gpio/gpio39/value
sleep 1
