#coding: utf-8

"""
@Author: Well
@Date: 2014 - 05 - 04
"""

# quick_sort

# 1. 从数列中挑出一个元素，称为 "基准"（pivot），
# 2. 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。
# 在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作。
# 3. 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序.


import sys
import random

lenth = 30

def qsort(arr,left,right):
    key = arr[right]
    lp = left
    rp = right
    if lp == rp: return
    while True:
        while (arr[lp] >= key) and (rp > lp):
            lp = lp + 1
        while (arr[rp] <= key) and (rp > lp):
            rp = rp - 1
        arr[lp], arr[rp] = arr[rp], arr[lp]
        if lp >= rp : break
    arr[rp], arr[right] = arr[right], arr[rp]
    if left < lp:
        qsort(arr,left,lp-1)
    qsort(arr,rp,right)


def main():
    arr = []
    sys.setrecursionlimit(100000)
    for i in range(lenth):
        arr.append(random.randint(0,1000))
    qsort(arr,0,lenth-1)
    print arr

if __name__ == '__main__':
    for i in range(10):
        main()