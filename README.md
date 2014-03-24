python-ev3
==========

Custom Debian distribution to program Lego Mindstorms EV3 using Python.

## What's this repository for?

Use this repository to create bootable system for Lego Mindstorms EV3 brick. If don't want to go through the whole [process](https://github.com/hmml/python-ev3/tree/refactor/build-rootfs) yourself, you can download prebuild system image from [here](https://db.tt/f7eBqYNo).

Once you have the system, you'll be more interested in the [ev3 repository](https://github.com/hmml/ev3) which is the Python API to program EV3 brick.

-_Notice, the python module is moved to [hmml repository](https://github.com/hmml/ev3). This one is only used for script to build SD image._

## What you need:

 1. [LegoMindstorms EV3 (31313)](http://www.lego.com/en-us/mindstorms/products/ev3/31313).
 2. Micro SD card 1GB+ ([original instruction]((https://github.com/topikachu/python-ev3)) claims that 2GB is required, I've used 1GB and it works as well).
 3. SD -> Micro SD card adapter.
 4. [Small forceps](http://upload.wikimedia.org/wikipedia/commons/a/a4/Forceps.jpg) to remove Micro SD card from EV3 block.
 5. 6x AA rechargeable batteries, two sets - the go flat pretty quickly.
 6. 2x AAA rechargeable batteries.

## Prepare SD card with system

Tested on OSX 10.9, should work with previous versions as well.

1. Download [system image](https://db.tt/f7eBqYNo) and unzip it:

    _Note: This is prebuilt system image. If you want to build it yourself follow [build instructions](https://github.com/hmml/python-ev3/tree/refactor/build-rootfs)._
    
        $  curl -L https://db.tt/f7eBqYNo | tar xj

2. Copy downloaded image to sd card. First, get the device `<NUMBER>` by inspecting output from:

        $ diskutil list 
        
   _Note: You may need to call `unmountDisk` instead of `unmount` if sd card comes with valid filesystem._
   
        $ sudo diskutil unmount /dev/disk<NUMBER>
        $ sudo dd if=./python-ev3.img of=/dev/rdisk<NUMBER> bs=1m
        $ sudo diskutil eject /dev/disk<NUMER>        
3. Turn off your robot, insert micro sd card and turn it on again (it may take some time).
4. Connect robot via USB cable.
5. Establish connection:
        
        $ ssh root@10.0.1.1
        
   Password is *password*.
6. Turning off:

        root@python-ev3:~# shutdown -h now
        
### Notes
* It takes a long time at first boot.
* The system is built using debian wheezy.
* A modified lejos kernel is used.
* The bluetooth is not stable enough. You may or may not connect to EV3 by bluetooth network.

## Reference
* ev3 opensource project: https://github.com/mindboards/ev3sources
* lejos: http://sourceforge.net/projects/lejos/
* python compile instructions: http://www.droboports.com/app-repository/python-2-7-5
* ev3-dev: https://github.com/mindboards/ev3dev
* the ev3 python module https://github.com/hmml/ev3
