#!/usr/bin/env python
# coding: utf-8

"""
@Author: Well
@Date: 2014 - 07 - 05
"""

# 引自：http://www.w3cschool.cc/python/python-for-loop.html

"""
7.1 Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。
"""
print "-------7.1-start-------"
for letter in 'Python':  # First Example
    print 'Current Letter :', letter

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:  # Second Example
    print 'Current fruit :', fruit

print "Good bye!"
print "-------7.1-end-------"

"""
7.2 通过序列索引迭代。
另外一种执行循环的遍历方式是通过索引
"""

print "-------7.2-start-------"
fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print 'Current fruit :', fruits[index]

print "Good bye!"
print "-------7.2-end-------"

"""
7.3 循环使用 else 语句
在 python 中，for … else 表示这样的意思，for 中的语句和普通的没有区别，
else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行，while … else 也是一样。
"""

print "-------7.3-start-------"
for num in range(10, 20):  # to iterate between 10 to 20
    for i in range(2, num):  # to iterate on the factors of the number
        if num % i == 0:  # to determine the first factor
            j = num / i  # to calculate the second factor
            print '%d equals %d * %d' % (num, i, j)
            break  # to move to the next number, the #first FOR
    else:  # else part of the loop
        print num, 'is a prime number'
print "-------7.3-end-------"


















