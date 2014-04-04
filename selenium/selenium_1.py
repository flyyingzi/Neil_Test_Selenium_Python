#coding: utf-8

"""
@Author: Well
@Date: 2014 - 04 - 02
"""
# http://www.cnblogs.com/fnng/p/3160606.html
# 熟悉selenium python 代码样式
# time.sleep()  添加休眠时间
# print   打印输出信息

from selenium import webdriver
import time  # 引入time函数

browser = webdriver.Chrome()

browser.get("http://www.baidu.com")
print browser.title  # 把页面title 打印出来
time.sleep(1)  # 休眠1秒

browser.find_element_by_id("kw1").send_keys("selenium")
browser.find_element_by_id("su1").click()
time.sleep(3)  # 休眠3秒

browser.quit()  # close()为关闭当前窗口，quit()为关闭所有窗口



