python-ev3
==========

a project to run lego ev3 in python
##Things you will need
* A linux box. Virtual Machine is also OK.
* A micro SD card >2G


## Getting Started
* Downlaod from http://sourceforge.net/projects/python-ev3/files/python-ev3.img.tar.gz/download and extract the image (it's 1G file after uncompressed)
* Copy the whole image to the SD card  
`umount /dev/<all sdcard patitons>`  
`dd if=python-ev3.img of=/dev/<sdcard device> bs=2m`
* Insert the sd card into ev3
* Boot the ev3
* Connect ev3 with the usb cable.  
`ssh root@10.0.1.1`  
password is "password"  

## Notice
* It takes a long time at first boot.
* The system is built at debian wheezy
* A modified lejos kernel is used.
* The bluetooth is not stable enough. You may or may not connect to ev3 by bluetooth network

## Reference
* ev3 opensource project: https://github.com/mindboards/ev3sources
* lejos: http://sourceforge.net/projects/lejos/
* python compile instructions: http://www.droboports.com/app-repository/python-2-7-5
* ev3-dev: https://github.com/mindboards/ev3dev
