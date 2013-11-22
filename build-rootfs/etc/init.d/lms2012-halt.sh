#! /bin/sh
### BEGIN INIT INFO
# Provides: ev3-exit
# Required-Start: 
# Required-Stop: ${ev3-shutdown}
# Should-Start: 
# Should-Stop: 
# Default-Start: 
# Default-Stop: 0
# Short-Description: power off
# Description: power off when unload power module 
### END INIT INFO

# System is going down remove loaded modules. Removig the power module
# after the power off flag has been set will power the EV3 off
echo "remove lms2012 modules"
# rmmod d_bt
modprobe -r d_ui
# # d_analog removes buffering for linux prompt
# rmmod d_analog
# # d_uart must be removed after d_analog
# rmmod d_uart
# rmmod d_pwm
# #rmmod d_usbdev
# rmmod d_usbhost
# rmmod d_sound
# rmmod d_iic
sync
modprobe -r d_power

