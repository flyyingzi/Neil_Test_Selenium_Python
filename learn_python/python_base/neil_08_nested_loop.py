#!/usr/bin/env python
#coding: utf-8

"""
@Author: Well
@Date: 2014 - 07 - 05
"""

# 引自：http://www.w3cschool.cc/python/python-nested-loops.html

"""
8.1 Python 语言允许在一个循环体里面嵌入另一个循环。
你可以在循环体内嵌入其他的循环体，如在while循环中可以嵌入for循环，
反之，你可以在for循环中嵌入while循环。
"""

i = 2
while i < 100:
    j = 2
    while j <= (i / j):
        if not (i % j): break
        j += 1
    if j > i / j: print i, " 是素数"
    i += 1

print "Good bye!"


