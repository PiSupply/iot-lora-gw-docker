#Update 4G Configuration
nmcli connection down iot3g
ip link set dev wwan0 down
echo Y > /sys/class/net/wwan0/qmi/raw_ip
ip link set dev wwan0 up
nmcli connection up iot3g
