#coding: utf-8

"""
@Author: Well
@Date: 2014 - 04 - 17
"""

# 3 操作测试对象
# clear() send_keys() click() submit()
# size text get_attribute() is_displayed()

from selenium import webdriver
import time


base_url = "http://www.baidu.com/"
browser = webdriver.Chrome()
browser.get(base_url)

# size
size = browser.find_element_by_id("kw1").size
print size

# text
text = browser.find_element_by_name("tj_baike").text
print text

# get_attribute()
# 输入输入框中的输入值
browser.find_element_by_id('kw1').send_keys("selenium test")
attribute = browser.find_element_by_id('kw1').get_attribute('value')
time.sleep(5)
print attribute

# is_displayed()
is_displayed = browser.find_element_by_name('ie').is_selected()
print is_displayed

browser.quit()

