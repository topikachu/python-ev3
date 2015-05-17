python-ev3
==========

Program Lego Mindstorms EV3 using Python on ev3dev

## What you need


You need a working [ev3dev](https://github.com/mindboards/ev3dev) on your ev3 and have a ssh session. Please reference the [ev3dev site](http://www.ev3dev.org/docs/getting-started/) to burn such system.  
Current python-ev3 is developed on [ev3dev-jessie-2015-05-01](https://github.com/ev3dev/ev3dev/releases/tag/ev3dev-jessie-2015-05-01)   

## Both python 2.7 and python 3.4 are supported
python-ev3 is tested on the ev3-dev in python2.7 and python3.4.
I have no all lego devices, so if there's something wrong or not working, please file an issue or create a pull request. I'm quite happy to receive more devices code.

## virtualenv
Current python-ev3 is not stable enough, virtualenv is recommend. Below examples are in virtualenv. However, python-ev3 should work in a native python environment.

## Install the python-ev3 on EV3
### Python 2.7
* ```apt-get update```
* ```apt-get install virtualenv  virtualenvwrapper python-setuptools python-smbus python-pil```
* ```source /etc/bash_completion.d/virtualenvwrapper```
* ```mkvirtualenv ev3_py27 --python=/usr/bin/python2.7 --system-site-packages```
* ```workon ev3_py27```
* ```easy_install python-ev3```
* type ```deactive``` to exit

### Python 3.4
* ```apt-get update```
* ```apt-get install virtualenv  virtualenvwrapper python3-setuptools python3-smbus python3-pil```
* ```source /etc/bash_completion.d/virtualenvwrapper```
* ```mkvirtualenv ev3_py34 --python=/usr/bin/python3.4 --system-site-packages```
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

## Python3 vs Python2 performance 
[@fuzzycow](https://github.com/fuzzycow) found there's some performance problem when using Python3. Please see https://github.com/topikachu/python-ev3/issues/22
        

## Reference
* ev3-dev: http://www.ev3dev.org/
