#coding: utf-8

"""
@Author: Well
@Date: 2014 - 04 - 16
"""
# time 函数的分析

import time
print time.time()  # 到1970-01-01-00-00-00的秒数
print time.ctime()  # 类似Wed Apr 16 13:46:30 2014的格式
print time.localtime()  # 返回时间的元组
print time.strftime("%Y:%m:%d:%H:%M:%S", time.localtime(time.time()))