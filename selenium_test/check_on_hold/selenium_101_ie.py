#coding: utf-8

"""
@Author: Well
@Date: 2014 - 04 - 11
"""

#  自签名证书 （ie）

from selenium import webdriver
import time

# 数据初始化
url2 = "https://vpn.rfchina.com/"
browser = webdriver.Ie()

# 打开浏览器
browser.get(url2)
browser.maximize_window()
time.sleep(3)

# 点击“继续浏览此网站”链接，继续访问
browser.find_element_by_partial_link_text(u"继续浏览此网站").click()
time.sleep(3)

# 关闭浏览器
browser.close()