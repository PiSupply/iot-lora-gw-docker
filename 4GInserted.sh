<<<<<<< HEAD
##Update 4G Configuration#
nmcli connection down iot5g
=======
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


#Update 4G Configuration
nmcli connection down iot3g
>>>>>>> 3376e3a7b822fd2c532b5f83b2e9fe71a9542385
ip link set dev wwan0 down
echo Y > /sys/class/net/wwan0/qmi/raw_ip
ip link set dev wwan0 up
nmcli connection up iot5g
