#! /bin/sh
### BEGIN INIT INFO
# Provides:       lms2012-runonce
# Required-Start: 
# Required-Stop:
# Should-Start:   
# Should-Stop:    
# X-Start-Before:
# X-Stop-After:   
# Default-Start:  2 3 4 5
# Default-Stop:   0
# Description:    lms2012-runonce
### END INIT INFO

dpkg --configure -a #continue config which is not sucessfully on pc
locale-gen
if [ -e /etc/init.d/lms2012-runonce.sh ]; then
            update-rc.d -f lms2012-runonce.sh remove
fi