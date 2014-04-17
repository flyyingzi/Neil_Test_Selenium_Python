#coding: utf-8

"""
@Author: Well
@Date: 2014 - 04 - 02
"""

# 简单对象的定位
# · id
# · name
# · class name
# · link text
# · partial link text
# · tag name
# · xpath
# · css selector

from selenium import webdriver
import time  # 引入time函数

browser = webdriver.Chrome()
url = "http://www.baidu.com"  # 将url分离，单独配置

browser.get(url)
time.sleep(1)  # 休眠1秒


#通过id方式定位
browser.find_element_by_id("kw1").send_keys("selenium")

#通过name方式定位
browser.find_element_by_name("wd").send_keys("selenium")

#通过tag name方式定位
browser.find_element_by_tag_name("input").send_keys("selenium")

#通过class name 方式定位
browser.find_element_by_class_name("s_ipt")

#通过CSS方式定位
browser.find_element_by_css_selector("#kw1").send_keys("selenium")

#通过xpath方式定位
browser.find_element_by_xpath("//input[@id='kw1']").send_keys("selenium")

browser.find_element_by_id("su1").click()
time.sleep(1)  # 休眠1秒

browser.quit()



