#!/usr/bin/env python
#coding: utf-8

"""
@Author: Well
@Date: 2014 - 06 - 16
"""

# lambda
d = (lambda x: x ** i for i in range(4))
print d
for i in d:
    print i(4)