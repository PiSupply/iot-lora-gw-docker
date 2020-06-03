#!/usr/bin/env bash

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


if [ ! -d "/sys/class/gpio/gpio22" ]; then
    echo "22" > /sys/class/gpio/export
fi
echo "out" > /sys/class/gpio/gpio22/direction
echo "1" > /sys/class/gpio/gpio22/value
sleep 1
echo "0" > /sys/class/gpio/gpio22/value
sleep 1
