#coding: utf-8

"""
@Author: Well
@Date: 2013-03-12
"""

#习题33：while 循环

i = 0
numbers = []

# while 和 for-loop 写法
# while i <= 6:
#     print "at the top i is %d" % i
#     numbers.append(i)
#
#     i += 1
#     print "numbers now: ", numbers
#     print "at the bottom i is %d" % i
#
# print "the numbers:"
# for num in numbers:
#     print num

#  用for-loop和range改写
for i in range(0, 7, 2):
    print "at the top i is %d" % i
    numbers.append(i)

    print "numbers now:", numbers
    print "at the bottom i is %d" % i

print "the numbers:"

for num in numbers:
    print num
