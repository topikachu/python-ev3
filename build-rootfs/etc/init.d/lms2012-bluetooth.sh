
# configure Bluetooth
hciconfig hci0 lm MASTER
# make us discoverable
hciconfig hci0 piscan
# set default pin
bluetooth-agent 1234 &


