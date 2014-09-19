python-ev3
==========

Program Lego Mindstorms EV3 using Python on ev3dev

## What you need


You need a working [ev3dev](https://github.com/mindboards/ev3dev) on your ev3 and have a ssh session. Please reference the [ev3dev wiki](https://github.com/mindboards/ev3dev/wiki/Getting-started-v2) to burn such system.  
Current python-ev3 is developed on [ev3dev-jessie-2014-07-12](https://github.com/mindboards/ev3dev/releases/tag/ev3dev-jessie-2014-07-12)   

## Both python 2.7 and python 3.4 are supported
python-ev3 is tested on the ev3-dev in python2.7 and python3.4.

Examples and documentations may refer to ```ev3_pyXX```. Substitute ```ev3_py27``` or ```ev3_py34``` depending on which version of Python you are using.


## Install the python-ev3 on EV3
### Python 2.7
* ```apt-get update```
* ```apt-get install python-virtualenv  virtualenvwrapper python-smbus python-imaging```
* ```source /etc/bash_completion.d/virtualenvwrapper```
* ```mkvirtualenv ev3_py27 --python=python2.7 --system-site-packages```
* ```workon ev3_py27```
* ```easy_install python-ev3```
* type ```deactive``` to exit

### Python 3.4
* ```apt-get update```
* ```apt-get install python-virtualenv  virtualenvwrapper python3-smbus python3-imaging```
* ```source /etc/bash_completion.d/virtualenvwrapper```
* ```mkvirtualenv ev3_py34 --python=python3.4 --system-site-packages```
* ```workon ev3_py34```
* ```easy_install python-ev3```
* type ```deactive``` to exit

## Using virtual environments

If you don't see ```(env3_pyXX)``` in the terminal prompt, then you must 
activate the virtual environment.

```bash
root@ev3dev:~# workon ev3_pyXX
(env3_pyXX)root@ev3dev:~#
```
Note how the second line starts with ```(env_pyXX)```.

To exit the virtual env, type ```deactivate```.

For more detail about Python virtual environments, see
[http://docs.python-guide.org/en/latest/dev/virtualenvs/]

## Example

This example is similar to the program at **examples/medium_motor.py**

Activate the virtual environment.
```bash
root@ev3dev:~# workon env_pyXX
```

Use the Python Shell to enter this short test program.

```python
(ev3_pyXX)root@ev3dev:~# python
Python X.Y.Z (default, Jul  4 2014, 16:59:40)
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

## More Examples

There are more example programs in the **examples** folder.

Activate the virtual env.

Run as many example programs as you want. For example:
```bash
(ev3_pyXX)root@ev3dev:~# python examples/medium_motor.py 
```

Deactivate the virtual env.

## More devices
Plese see [```test```](https://github.com/topikachu/python-ev3/tree/master/test) to know how to use other devices.
To create new sensor class please see [How to create a new sensor class ](https://github.com/topikachu/python-ev3/wiki/How-to-create-a-new-sensor-class)
        

## Reference
* ev3 opensource project: https://github.com/mindboards/ev3sources
* ev3-dev: https://github.com/mindboards/ev3dev
