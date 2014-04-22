#coding: utf-8

"""
@Author: Well
@Date: 2014 - 04 - 19
"""

# 5 打印消息
# title
# current_url
# 通过一些差异的信息进行断言

from selenium import webdriver
import time

base_url = 'http://www.baidu.com'
browser = webdriver.Chrome()

browser.get(base_url)
title_ = browser.title
url_ = browser.current_url

# 断言
assert u'百度' in title_
assert 'baidu' in url_

browser.quit()