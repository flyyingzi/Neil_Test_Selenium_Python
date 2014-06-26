#coding: utf-8

"""
@Author: Well
@Date: 2014 - 04 - 20
"""

# 引用网址：http://www.cnblogs.com/buro79xxd/archive/2011/05/23/2054493.html
# range

# list 的创建
a = [y + 1 for y in range(12)]
b = range(12)
c = list(range(12))
print a, b, c

# if 循环
list_1 = [x ** 2 for x in range(0, 20) if x % 3 == 0]
print list_1

# 多个for循环
list_2 = [(x, y) for x in range(0, 5) for y in range(0,3)]
print list_2

# lambda
d = (lambda x: x ** i for i in range(4))
print d
for i in d:
    print i(4)