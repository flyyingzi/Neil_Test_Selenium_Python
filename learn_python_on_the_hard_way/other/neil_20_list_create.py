#coding: utf-8

"""
@Author: Well
@Date: 2014 - 05 - 04
"""
# if 写法
list_1 = [x ** 2 for x in range(0, 20) if x % 3 == 0]
print list_1

# 多个for循环
list_2 = [(x, y) for x in range(0, 5) for y in range(0,3)]
print list_2