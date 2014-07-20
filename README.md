python-ev3
==========

Program Lego Mindstorms EV3 using Python on ev3dev

## What you need


You need a working [ev3dev](https://github.com/mindboards/ev3dev) on your ev3 and have a ssh session. Please reference the [ev3dev wiki](https://github.com/mindboards/ev3dev/wiki/Getting-started-v2) to burn such system.  
Current python-ev3 is developed on [ev3dev-jessie-2014-07-12](https://github.com/mindboards/ev3dev/releases/tag/ev3dev-jessie-2014-07-12)   

## Install the python-ev3 on EV3
Install python-ev3 under a virtual env
* ```apt-get install virtualenv  virtualenvwrapper python-setuptools python-smbus```
* ```mkvirtualenv ev3```
* ```add2virtualenv /usr/lib/python2.7/dist-packages```
* ```easy_install python-ev3```

## Example
```python
(ev3)root@ev3dev:~# python
Python 2.7.8 (default, Jul  4 2014, 16:59:40)
[GCC 4.9.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from ev3.lego import MidiumMotor
>>> d = MidiumMotor()
>>> d.reset()
>>> d.run_forever(50, regulation_mode=False)
>>> d.stop()
>>> exit()
```
To exit the virtual env, type ```deactivate```

## More devices
Plese see ```test``` to know how to use other devices.  
To create new sensor class please see [How to create a new sensor class ](https://github.com/topikachu/python-ev3/wiki/How-to-create-a-new-sensor-class)
        

## Reference
* ev3 opensource project: https://github.com/mindboards/ev3sources
* ev3-dev: https://github.com/mindboards/ev3dev
