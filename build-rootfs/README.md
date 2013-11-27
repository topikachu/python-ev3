build the python-ev3 fs
==========
The python-ev3 root fs is built from debian wheezy by Multistrap

##Things you will need
* A debain or ubuntu linux box. Virtual Machine is also OK.

## Getting Started
* First time, run the ./prepare_env to install all tool
* Run sudo ./build_rootfs to download and setup the rootfs
* Run ./makeimage.sh <uImage> <rootfs dir> <image name>  
`./makeimage.sh uImage/uImage  ../../python-ev3-rootfs/ev3-rootfs/ ../../python-ev3-rootfs/python-ev3.img`
* After the image is created, use dd to copy the image to sd card  

## Reference
* ev3 opensource project: https://github.com/mindboards/ev3sources
* lejos: http://sourceforge.net/projects/lejos/
* ev3-dev: https://github.com/mindboards/ev3dev
