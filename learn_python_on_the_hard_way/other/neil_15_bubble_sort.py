#coding: utf-8

"""
@Author: Well
@Date: 2014 - 05 - 03
"""

# bubble_sort
# 冒泡的原理
# 1.比较相邻的元素。如果第一个比第二个大，就交换他们两个。
# 2.对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。在这一点，最后的元素应该会是最大的数。
# 3.针对所有的元素重复以上的步骤，除了最后一个。
# 4.持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较

def bubble_sort(list_):
    len_ = len(list_)
    # 至少两个数才能比较，所以len_ >= 2
    while len_ >= 2:
        for i in range(0, len_ - 1):
            if list_[i] > list_[i + 1]:
                list_[i], list_[i + 1] = list_[i + 1], list_[i]
        len_ -= 1
    return list_

if __name__ == "__main__":
    list_2 = [5, 20, 30, 4, 9, 200, 1, 55]
    list_3 = [3, 2, 1]
    print bubble_sort(list_2), '\n', bubble_sort(list_3)



