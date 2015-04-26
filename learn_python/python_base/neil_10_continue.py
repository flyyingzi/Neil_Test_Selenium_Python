#!/usr/bin/env python
#coding: utf-8

"""
@Author: Well
@Date: 2014 - 07 - 05
"""

# 引自：http://www.w3cschool.cc/python/python-continue-statement.html

"""
10.1 Python continue 语句
Python continue 语句跳出本次循环，而break跳出整个循环。
continue 语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环。
continue语句用在while和for循环中。
"""

for letter in 'Python':     # First Example
    if letter == 'h':
        continue
    print 'Current Letter :', letter

var = 10                    # Second Example
while var > 0:
    var -= 1
    if var == 5:
        continue
    print 'Current variable value :', var
print "Good bye!"