clear
ifconfig |awk '/inet/ {print $2}'



