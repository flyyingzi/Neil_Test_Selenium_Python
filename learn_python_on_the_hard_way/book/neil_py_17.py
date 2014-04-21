#coding: utf-8

"""
@Author: Well
@Date: 2013-03-12
"""

#习题30:else 和 if

people = 30
cars = 40
buses = 15

# 比较cars 和 people
if cars > people:
    print "we should take the cars."
elif cars < people:
    print "we should not take the cars."
else:
    print "we can't decide."

#比较 buses 和 cars
if buses > cars:
    print"that's too many buses."
elif buses < cars:
    print"maybe we could take the buses."
else:
    print "we still can't decide."

#比较 people 和 buses
if people > buses:
    print "alright, let's just take the buses."
else:
    print "fine,let's stay home"


