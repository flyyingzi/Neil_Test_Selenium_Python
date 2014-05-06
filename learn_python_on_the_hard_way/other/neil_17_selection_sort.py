#coding: utf-8

"""
@Author: Well
@Date: 2014 - 05 - 04
"""


# 选择排序
# 顾名思意,就是直接从待排序数组里选择一个最小(或最大)的数字,
# 每次都拿一个最小数字出来,
# 顺序放入新数组,直到全部拿完

def selection_sort(list_):
    for i in range(0, len(list_)):
        for j in range(i + 1, len(list_)):
            # 比较大小，调换位置, 定最小数
            if list_[i] > list_[j]:
                list_[i], list_[j] = list_[j], list_[i]
    return list_

if __name__ == "__main__":
    list_2 = [5, 20, 30, 4, 9, 200, 1, 55]
    print selection_sort(list_2)
