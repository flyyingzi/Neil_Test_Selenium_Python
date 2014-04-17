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

txt_ = file('selenium_11.txt', 'r')
txt_2 = txt_.read().split('.')
print txt_2
print len(txt_2) - 1
txt_.close()








