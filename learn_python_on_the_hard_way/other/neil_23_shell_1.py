#coding: utf-8

"""
@Author: Well
@Date: 2014 - 05 - 31
"""


# OS is linux

import os

str_ = os.popen("pwd").read()
a = str_.split("\n")
for b in a:
   print b