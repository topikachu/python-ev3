#!/usr/bin/python
### BEGIN INIT INFO
# Provides: ev3-shutdown
# Required-Start: 
# Required-Stop: 
# Should-Start: 
# Should-Stop: 
# Default-Start: 
# Default-Stop: 0
# Short-Description: setup poweroff flat
# Description: setup poweroff flat
### END INIT INFO

from fcntl import ioctl
import os
import struct
print "set power off flag"
power_file=os.open("/dev/lms_power",os.O_RDWR);
ioctl(power_file,0);
os.close(power_file)

ui_file=os.open("/dev/lms_ui",os.O_RDWR);
os.write(ui_file,struct.pack('BB',ord('0')+2,0))
os.close(ui_file)
