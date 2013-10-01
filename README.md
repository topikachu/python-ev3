python-ev3
==========

a project to run lego ev3 in python
##Things you will need
A linux box. Virtual Machine is also OK.
The latest lejos bootable sdcard: http://sourceforge.net/p/lejos/wiki/Home/
An arm linux versio python. https://www.dropbox.com/s/pk621lqpwi3s9i3/ev3.python.tar.gz
## Getting Started
Burn the lejos sdcard at your linux machine
Extract python and copy to sdcard 2nd partition (LMS2012_EXT) /home/root
Use lejos to boot ev3
Connect ev3 either by wireless or usb. The latest lejos provide tcp over usb.
Use ssh to connect ev3 for example
`ssh root@10.0.1.1`
password is empty
`export LD_LIBRARY_PATH=/home/root/python2/lib`
`export PATH=/home/root/python2/bin:$PATH`



