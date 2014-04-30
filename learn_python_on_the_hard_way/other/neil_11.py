#coding: utf-8

"""
@Author: Well
@Date: 2014 - 04 - 28
"""

import os
from selenium import webdriver

command = "dir"
a = os.system(command)

print a.decode('utf-8').encode('gb2312')
