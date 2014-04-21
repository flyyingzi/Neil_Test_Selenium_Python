#coding: utf-8

"""
@Author: Well
@Date: 2014 - 04 - 20
"""


# 10 定位 frame 中的对象

from selenium import webdriver
import os
import time

browser = webdriver.Chrome()
base_url = os.path.dirname(__file__) + '\\' + 'html' + '\\' + 'frame.html'
browser.implicitly_wait(30)


browser.get(base_url)
# 切换到frame1(id 和 name都可以)
browser.switch_to.frame('f1')
# 切换到frame2
browser.switch_to.frame('f2')

# 元素操作
browser.find_element_by_id("kw1").send_keys("selenium")
browser.find_element_by_id("su1").click()
time.sleep(5)

browser.quit()
