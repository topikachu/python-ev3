#!/usr/bin/env python

from distutils.core import setup

setup(name='python-ev3',
      version='0.1',
      description='Python library of Lego EV3',
      author='Gong Yi',
      author_email='topikachu@163.com',
      url='https://github.com/topikachu/python-ev3',
      packages=['ev3', 'ev3.rawdevice'],
     )