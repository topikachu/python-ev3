python-ev3
==========

Project to program Lego Mindstorms EV3 using Python.

## What you need
 1. [LegoMindstorms EV3 (31313)](http://www.lego.com/en-us/mindstorms/products/ev3/31313).
 2. Micro SD card 1GB+ ([original instruction]((https://github.com/topikachu/python-ev3)) claims that 2GB is required, I've used 1GB and it works as well).
 3. SD -> Micro SD card adapter.
 4. [Small forceps](http://upload.wikimedia.org/wikipedia/commons/a/a4/Forceps.jpg) to remove Micro SD card from EV3 block.
 5. 6x AA rechargeable batteries.
 6. 2x AAA rechargeable batteries.

## Setup (OSX)

Tested on OSX 10.9, should work with previous versions as well.

1. Download system image from [Source Forge](http://sourceforge.net/projects/python-ev3/files/python-ev3.img.tar.gz/download) and unzip it:

    _Note: This is prebuilt system image. If you want to build it yourself follow [build instructions](https://github.com/hmml/python-ev3/tree/refactor/build-rootfs)._
    
    **Important: following system image is not up-to-date and python code below will not work! - to be updated soon. **

        $ curl -L http://sourceforge.net/projects/python-ev3/files/python-ev3.img.tar.gz/download | tar xv

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

## Python

Once you have a working environment, connect to EV3 brick and launch Python:

    root@python-ev3:~# python      
    [GCC 4.6.3] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from ev3 import ev3
    >>> ev3.open_all_devices()
    >>> ev3.get_battery()
    (6911.138911088911, 46.41822823641005, 0.0)
    >>> ev3.set_led(ev3.LED_GREEN)
    >>> ev3.close_all_devices()
    
Reading sensors:    
    
    >>> from ev3 import ev3
    >>> from ev3.sensor.lego import EV3TouchSensor
    >>> ev3.open_all_devices()
    >>> touch_sensor = EV3TouchSensor(ev3.SENSOR_1)
    >>> while True:
    ...     if touch_sensor.is_pressed(): print "pressed"
    ... 
    pressed    # I've pressed touch sensor
    (ctrl+c to break the loop)
    
## Documentation

So far code is the only documentation, you'll find it in [ev3 subdirectory](https://github.com/hmml/python-ev3/tree/refactor/ev3).

## Reference
* ev3 opensource project: https://github.com/mindboards/ev3sources
* lejos: http://sourceforge.net/projects/lejos/
* python compile instructions: http://www.droboports.com/app-repository/python-2-7-5
* ev3-dev: https://github.com/mindboards/ev3dev
