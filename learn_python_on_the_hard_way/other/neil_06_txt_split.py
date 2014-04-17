#coding: utf-8

"""
@Author: Well
@Date: 2014 - 04 - 14
"""

"""
求某一个英文文本中完整句子的数目，
文本中只包含大小写字母、空格、“，”和“.”，
完整的句子是指以“.”结束，且“.”号前必须出现至少一个字母。
"""

import os

# 文件名
name_ = os.path.basename(__file__).split('.')[0]
dir_ = os.path.dirname(__file__)

# 绝对文件夹路径
# file2 = os.path.dirname(__file__)
# print file2
#
# # 绝对路径
# file3 = os.path.abspath(__file__)
# print file3

# txt文件的绝对路径
file_ = dir_ + '\\' + name_ + '.txt'

txt_ = file(file_, 'r')
txt_2 = txt_.read().split('.')
print len(txt_2) - 1
txt_.close()








