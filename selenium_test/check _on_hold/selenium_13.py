#coding: utf-8

"""
@Author: Well
@Date: 2014 - 04 - 19
"""

from selenium import webdriver
import os
import time

base_url = os.path.dirname(__file__) + '\\' + 'alert.html'
browser = webdriver.Chrome()

browser.get(base_url)
browser.find_element_by_class_name('ui-link').click()

time.sleep(5)
print browser.switch_to_alert().text
browser.switch_to.alert.accept()
print browser.page_source