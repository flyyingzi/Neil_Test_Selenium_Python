#coding: utf-8

"""
@Author: Well
@Date: 2014-03-09
"""

#习题19: 命名 变量 代码 函数

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "%d cheeses" % cheese_count
    print "%d boxes of crackers" % boxes_of_crackers
    print "Enough for a party. \n"


print "Give the function num directly"
cheese_and_crackers(20, 30)


print "OR, use variables from our script."
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("Do math inside too:")
cheese_and_crackers(10+20, 5+6)


print "Combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)
