#coding: utf-8

"""
@Author: Well
@Date: 2013-03-12
"""

#习题29：如果（if）

people = 20
cats = 30
dogs = 15

if people < cats:
    print "too many cats."


if people > cats:
    print "not many cats."

if people < dogs:
    print "too many dogs."

if people > dogs:
    print "not many dogs."

dogs += 5
if people >= dogs:
    print "people are greater than or equal to dogs."

if people >= dogs:
    print "people are less than or equal to dogs."

if people >= dogs:
    print "people are dogs."
