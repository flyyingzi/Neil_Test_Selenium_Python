#coding: utf-8

"""
@Author: Well
@Date: 2014 - 04 - 20
"""

# 12 多浏览器窗口处理

from selenium import webdriver
import time

browser = webdriver.Chrome()
base_url = 'http://www.youdao.com'

browser.get(base_url)

# 获取当前窗口的句柄
handle_1 = browser.current_window_handle

# 新标签中打开有道字典
browser.find_element_by_class_name('dict').click()

# 获取所有窗口的句柄
handle_2 = browser.current_window_handle

time.sleep(5)
browser.switch_to.window(handle_1)
time.sleep(5)

browser.quit()



