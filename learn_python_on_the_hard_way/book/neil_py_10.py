#coding: utf-8

"""
@Author: Well
@Date: 2013-03-12
"""

#习题21:函数可以返回东西

def add(a, b):
    print "ADD %d + %d " % (a, b)
    return a + b


def subtract(a, b):
    print "SUBTRACT %d - %d" % (a, b)
    return a - b


def multiply(a, b):
    print "MULTIPLY %d * %d" % (a, b)
    return a * b


def divide(a, b):
    print "DIVIDE %d / %d" % (a, b)
    return a / b


print "DO math with just functions."

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "age: %d, height: %d, weight: %d,iq: %d" % (age, height, weight, iq)

print "here is a puzzle"

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print "that becomes:", what, "can you do it by hand."
