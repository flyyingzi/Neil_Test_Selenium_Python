# !/usr/bin/python
#coding: utf-8

"""
@Author: Well
@Date: 2014 - 06 - 18
"""


import os

a = os.popen("adb get-state").read()
print a == 'device'


