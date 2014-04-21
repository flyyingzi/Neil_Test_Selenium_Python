#coding: utf-8

"""
@Author: Well
@Date: 2013-03-09
"""

#习题18: 命名 变量 代码 函数

def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)


def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)


def print_one(arg1):
    print "arg1: %r" % arg1


def print_none():
    print "I get nothing"


print_two("test1", "test2")
print_two_again("test1", "test2")
print_one("first")
print_none()