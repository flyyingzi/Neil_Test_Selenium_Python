# !/usr/bin/python
#coding: utf-8

"""
@Author: Well
@Date: 2014 - 07 - 05
"""

# 引自：http://www.w3cschool.cc/python/python-pass-statement.html

"""
11.1 Python pass 语句
Python pass是空语句，是为了保持程序结构的完整性。
"""

for letter in 'Python':
    if letter == 'h':
        pass
        print 'This is pass block'
    print 'Current Letter :', letter

print "Good bye!"