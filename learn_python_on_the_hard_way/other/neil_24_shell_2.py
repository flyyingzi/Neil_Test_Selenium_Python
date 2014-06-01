#!/usr/bin/python
#coding: utf-8

"""
@Author: Well
@Date: 2014 - 05 - 31
"""

# OS is linux

import os

print "hello"

file_path = "/home/py/test"
os.mknod(file_path)
if os.path.exists(file_path):
    os.remove(file_path)
    print "remove ok"

os.system("cd /etc")
os.system("mkdir test")
