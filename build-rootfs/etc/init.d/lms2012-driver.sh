#! /bin/sh
### BEGIN INIT INFO
# Provides: lms2012-driver
# Required-Start: $ev3-init
# Required-Stop: 
# Should-Start: 
# Should-Stop: 
# Default-Start: 2 3 4 5
# Default-Stop:
# Short-Description: load lms2012 modules
# Description: load lms2012 modules
### END INIT INFO
sync
LMS2012_SETTINGS=/mnt/ramdisk/settings


modprobe d_iic `cat ${LMS2012_SETTINGS}/HwId`
modprobe d_uart `cat ${LMS2012_SETTINGS}/HwId`
modprobe d_power `cat ${LMS2012_SETTINGS}/HwId`
modprobe d_pwm `cat ${LMS2012_SETTINGS}/HwId`
modprobe d_ui `cat ${LMS2012_SETTINGS}/HwId`
modprobe d_analog `cat ${LMS2012_SETTINGS}/HwId`

#modprobe d_usbhost
modprobe d_sound `cat ${LMS2012_SETTINGS}/HwId`
#modprobe d_bt `cat ${LMS2012_SETTINGS}/HwId`

chmod 666 /dev/lms_pwm
chmod 666 /dev/lms_motor
chmod 666 /dev/lms_analog
chmod 666 /dev/lms_dcm
chmod 666 /dev/lms_ui
chmod 666 /dev/lms_uart
chmod 666 /dev/lms_power

# chmod 666 /dev/lms_usbhost
chmod 666 /dev/lms_sound
chmod 666 /dev/lms_iic
#chmod 666 /dev/lms_bt
