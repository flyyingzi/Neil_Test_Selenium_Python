#coding: utf-8

"""
@Author: Well
@Date: 2014 - 04 - 12
"""

# 16 上传文件


from selenium import webdriver
import time
import os.path

browser = webdriver.Chrome()
url1 = "https://anonfiles.com/"
# file_path = os.path.normcase(u"C:\\Users\\wei\\Desktop\\测试1.txt")
file_path = u"C:\\Users\\wei\\Desktop\\测试1.txt"
print file_path

browser.get(url1)
browser.maximize_window()
browser.find_element_by_class_name("long_input").send_keys(file_path)
time.sleep(2)
browser.find_element_by_name("upl").click()
time.sleep(3)






