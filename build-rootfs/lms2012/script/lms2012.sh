#! /bin/sh
### BEGIN INIT INFO
# Provides: ev3-lms2012
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
LMS2012_MODULES=/lib/lms2012/modules
var=$(printf 'HostStr=%s SerialStr=%s' $(cat ${LMS2012_SETTINGS}/BrickName) $(cat ${LMS2012_SETTINGS}/BTser))
echo $var > ${LMS2012_SETTINGS}/UsbInfo.dat

# insmod ${LMS2012_MODULES}/d_iic.ko `cat ${LMS2012_SETTINGS}/HwId`
# insmod ${LMS2012_MODULES}/d_uart.ko `cat ${LMS2012_SETTINGS}/HwId`
insmod ${LMS2012_MODULES}/d_power.ko `cat ${LMS2012_SETTINGS}/HwId`
# insmod ${LMS2012_MODULES}/d_pwm.ko `cat ${LMS2012_SETTINGS}/HwId`
insmod ${LMS2012_MODULES}/d_ui.ko `cat ${LMS2012_SETTINGS}/HwId`
# insmod ${LMS2012_MODULES}/d_analog.ko `cat ${LMS2012_SETTINGS}/HwId`

# insmod ${LMS2012_MODULES}/d_usbhost.ko
# insmod ${LMS2012_MODULES}/d_sound.ko `cat ${LMS2012_SETTINGS}/HwId`
# insmod ${LMS2012_MODULES}/d_bt.ko `cat ${LMS2012_SETTINGS}/HwId`

# chmod 666 /dev/lms_pwm
# chmod 666 /dev/lms_motor
# chmod 666 /dev/lms_analog
# chmod 666 /dev/lms_dcm
chmod 666 /dev/lms_ui
# chmod 666 /dev/lms_uart
chmod 666 /dev/lms_power

# chmod 666 /dev/lms_usbhost
# chmod 666 /dev/lms_sound
# chmod 666 /dev/lms_iic
# chmod 666 /dev/lms_bt
