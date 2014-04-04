#coding: utf-8

"""
@Author: Well
@Date: 2014 - 03 - 30
"""

import math
a = []
flag = True

for i in range(2, 101):
    for j in range(2, int(math.sqrt(i) + 1)):
        if i % j == 0:
            flag = False
    if flag:
        a.append(i)
    flag = True
print a