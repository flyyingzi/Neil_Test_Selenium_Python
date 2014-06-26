# !/usr/bin/python
#coding: utf-8

"""
@Author: Well
@Date: 2014 - 06 - 16
"""

A = ('123', '321', '123', '213', '312')
B = ('123', 'abc', '321', 'bca', 'cba', 'abc')
OnlyA = ()
OnlyB = ()
Same = ()

t = (0, 'haha', (4j, 'y'))
print t
print t[2]
print t[-1]
print t[0:-1]
for i in t:
    print i