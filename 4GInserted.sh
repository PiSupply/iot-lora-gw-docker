#Update 4G Configuration
nmcli connection down smarty
ip link set dev wwan0 down
echo Y > /sys/class/net/wwan0/qmi/raw_ip
ip link set dev wwan0 up
nmcli connection up smarty
