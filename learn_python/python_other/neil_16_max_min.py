#coding: utf-8

"""
@Author: Well
@Date: 2014 - 05 - 03
"""

# 求list中的最大数和最小数

# max
def list_max(list_):
    max_ = list_[0]
    for i in list_:
        max_ = max_ if (max_ > i) else i
    return max_

# min
def list_min(list_):
    min_ = list_[0]
    for i in list_:
        min_ = min_ if (min_ < i) else i
    return min_

list2 = [5, 20, 30, 4, 9, 200, 1, 55]
print list_max(list2), list_min(list2)


