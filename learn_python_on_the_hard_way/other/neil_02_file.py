#coding: utf-8

"""
@Author: Well
@Date: 2014 - 04 - 16
"""

# 判断文件是否存在，存在的话，直接删除

import os

file_path = r"C:\Users\wei\Documents\GitHub\neilpytest\selenium_test\png\TestCase001.png"
if os.path.exists(file_path):
    os.remove(file_path)
else:
    print u'文件不存在'