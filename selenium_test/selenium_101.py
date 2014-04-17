#coding: utf-8

"""
@Author: Well
@Date: 2014 - 04 - 16
"""


import os
from selenium import webdriver


file_path = "C:\\Users\\wei\\Documents\\GitHub\\neilpytest\\selenium_test\\png\\1.txt"
if os.path.exists(file_path):
    os.remove(file_path)
else:
    print u'文件不存在'

