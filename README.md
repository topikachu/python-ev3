python-ev3
==========

Program Lego Mindstorms EV3 using Python on ev3dev

## What you need


You need a working [ev3dev](https://github.com/mindboards/ev3dev) on your ev3 and have a ssh session. Please reference the [ev3dev wiki](https://github.com/mindboards/ev3dev/wiki/Getting-started-v2) to burn such system.  
Current python-ev3 is developed on [ev3dev-jessie-2014-07-12](https://github.com/mindboards/ev3dev/releases/tag/ev3dev-jessie-2014-07-12)   

## Both python 2.7 and python 3.4 are supported
python-ev3 is tested on the ev3-dev in python2.7 and python3.4.


## Install the python-ev3 on EV3
### Python 2.7
* ```apt-get update```
* ```apt-get install virtualenv  virtualenvwrapper python-setuptools python-smbus python-pil```
* ```source /etc/bash_completion.d/virtualenvwrapper```
* ```mkvirtualenv ev3_py27 --python=python2.7 --system-site-packages```
* ```workon ev3_py27```
* ```easy_install python-ev3```
* type ```deactive``` to exit

### Python 3.4
* ```apt-get update```
* ```apt-get install virtualenv  virtualenvwrapper python3-setuptools python3-smbus python3-pil```
* ```source /etc/bash_completion.d/virtualenvwrapper```
* ```mkvirtualenv ev3_py34 --python=python3.4 --system-site-packages```
* ```workon ev3_py34```
* ```easy_install python-ev3```
* type ```deactive``` to exit

## Example
```python
(ev3_py27)root@ev3dev:~# python
Python 2.7.8 (default, Jul  4 2014, 16:59:40)
[GCC 4.9.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from ev3.lego import MediumMotor
>>> d = MediumMotor()
>>> d.reset()
>>> d.run_forever(50, regulation_mode=False)
>>> d.stop()
>>> exit()
```
To exit the virtual env, type ```deactivate```

## More devices
Plese see [```test```](https://github.com/topikachu/python-ev3/tree/master/test) to know how to use other devices.  
To create new sensor class please see [How to create a new sensor class ](https://github.com/topikachu/python-ev3/wiki/How-to-create-a-new-sensor-class)
        

## Reference
* ev3 opensource project: https://github.com/mindboards/ev3sources
* ev3-dev: https://github.com/mindboards/ev3dev
