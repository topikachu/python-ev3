#! /bin/sh
echo -ne "\033[9;0]" >/dev/tty1
setterm -cursor off > /dev/tty1
setterm -blank 0 > /dev/tty1
setterm -linewrap off > /dev/tty1
setterm -clear > /dev/tty1 