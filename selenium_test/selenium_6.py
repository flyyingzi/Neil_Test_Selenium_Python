#coding: utf-8

"""
@Author: Well
@Date: 2014 - 04 - 03
"""

# 补
# http://www.cnblogs.com/fnng/p/3202299.html
# 操作对象：
# · click 点击对象
# · send_keys 在对象上模拟按键输入
# · clear 清除对象的内容，如果可以的话
#
# WebElement  另一些常用方法：
#
# · text  获取该元素的文本
# · submit  提交表单 (和click 效果相同)
# · get_attribute  获得属性值


from selenium_test import webdriver
import time  # 引入time函数

browser = webdriver.Chrome()
url = "http://www.baidu.com"  # 将url分离，单独配置

browser.get(url)
time.sleep(1)  # 休眠1秒

browser.find_element_by_id("kw1").send_keys("clear")
time.sleep(1)  # 休眠1秒
browser.find_element_by_id("kw1").clear()
time.sleep(1)  # 休眠1秒
browser.find_element_by_id("kw1").send_keys("selenium")
time.sleep(1)  # 休眠1秒

# text 用法
data = browser.find_element_by_id("cp").text
print data   # 打印信息

browser.find_element_by_id("su1").click()
time.sleep(1)  # 休眠1秒


browser.quit()




