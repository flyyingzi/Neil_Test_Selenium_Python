#coding: utf-8

"""
@Author: Well
@Date: 2014 - 04 - 03
"""

# 补
# http://www.cnblogs.com/fnng/p/3190966.html
# 定位一组元素

from selenium import webdriver
import time
import os

browser = webdriver.Chrome()
 # 绝对路径
file_path = os.path.dirname(__file__) + '\\' + 'checkbox.html'
print os.path.dirname(__file__)
print file_path
browser.get(file_path)

# 选择页面上所有的input，然后从中过滤出所有的checkbox并勾选之
inputs = browser.find_elements_by_tag_name('input')
for input_ in inputs:
    if input_.get_attribute('type') == 'checkbox':
        input_.click()

time.sleep(2)

browser.quit()