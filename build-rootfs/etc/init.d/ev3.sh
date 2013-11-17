#! /bin/sh
### BEGIN INIT INFO
# Provides:       ev3
# Required-Start: 
# Required-Stop:  $halt
# Should-Start:   
# Should-Stop:    
# X-Start-Before:
# X-Stop-After:   
# Default-Start:  2 3 4 5
# Default-Stop:   0
# Description:    ev3
### END INIT INFO

case "$1" in
  start)
    echo "start ev3"
    dpkg --configure -a #continue config which is not sucessfully
    /etc/init.d/isc-dhcp-server start
    /lib/lms2012/script/ev3init.sh
    /lib/lms2012/script/lms2012.sh
    /lib/lms2012/script/startnetwork.sh
    echo "."
    ;;
  stop)
    echo "stop ev3"
    /lib/lms2012/script/shutdownflag.py
    /lib/lms2012/script/exit.sh
    echo "."
    ;;
  *)
    echo "Usage: /etc/init.d/ev3.sh {start|stop}"
    exit 1
esac

exit 0
