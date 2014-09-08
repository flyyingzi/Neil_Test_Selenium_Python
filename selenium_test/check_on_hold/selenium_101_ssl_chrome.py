#coding: utf-8

"""
@Author: Well
@Date: 2014 - 05 - 26
"""

#  自签名证书（chrome）：默认跳过验证证书

from selenium import webdriver
import time

# 数据初始化

url2 = "https://vpn.rfchina.com/"
browser = webdriver.Chrome()

# 打开浏览器
browser.get(url2)
browser.maximize_window()
time.sleep(3)

# 关闭浏览器
browser.close()