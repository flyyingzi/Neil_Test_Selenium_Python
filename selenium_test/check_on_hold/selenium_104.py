#coding: utf-8

"""
@Author: Well
@Date: 2014 - 04 - 25
"""


from selenium import webdriver
import time


browser = webdriver.Ie()
url = "http://www.baidu.com"

browser.get(url)
element_ = browser.find_element_by_id("kw1")
element_.clear()
element_.send_keys("12306")
element_.clear()
browser.close()

