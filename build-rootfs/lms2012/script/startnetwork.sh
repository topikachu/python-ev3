#! /bin/sh
NETADDRESS=10.0.1.1


# create the bridge and configure it
brctl addbr br0
ifconfig br0 ${NETADDRESS}
brctl setfd br0 0
brctl stp br0 off
# setup the USB interface
modprobe g_ether
ifconfig usb0 0.0.0.0
brctl addif br0 usb0


# configure Bluetooth
hciconfig hci0 lm MASTER
# make us discoverable
hciconfig hci0 piscan
# set default pin
bluetooth-agent -a hci0 1234 &


/etc/init.d/isc-dhcp-server restart
