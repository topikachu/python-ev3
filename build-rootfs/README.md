Build the python-ev3 fs
=======================
The python-ev3 root fs is built from Debian Wheezy by Multistrap. It's a complete system that you can boot into.

## Things you will need
* A Debian or Ubuntu Linux box. Virtual machine is also OK (I've used VirtualBox on Windows 7 running Ubuntu 12.04 LTS).

## Getting Started
* Install all tools and clone/update ev3 python repository:

		$ ./prepare_env

* Download and setup the rootfs:

		$ sudo ./build_rootfs

* Create image file:

		$ ./makeimage.sh uImage/uImage  ../../python-ev3-rootfs/ev3-rootfs/ ../../python-ev3-rootfs/python-ev3.img

* After the image is created, use dd to copy the image to sd card - that'll all!

## Reference
* ev3 opensource project: https://github.com/mindboards/ev3sources
* lejos: http://sourceforge.net/projects/lejos/
* ev3-dev: https://github.com/mindboards/ev3dev
