#coding: utf-8

"""
@Author: Well
@Date: 2014 - 04 - 12
"""

# 16 上传文件


from selenium import webdriver
import time
import os.path

# 数据初始化
browser = webdriver.Chrome()
base_url = "https://anonfiles.com/"
file_path = os.path.dirname(__file__) + '\\' + 'html' + '\\' + 'test.txt'

# 打开url
browser.get(base_url)
browser.maximize_window()

# 定位上传browser
browser.find_element_by_class_name("long_input").send_keys(file_path)
time.sleep(2)
# 定位上传按钮
browser.find_element_by_name("upl").click()
time.sleep(3)






