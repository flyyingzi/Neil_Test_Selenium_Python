#coding: utf-8

"""
@Author: Well
@Date: 2014 - 04 - 11
"""

# 自签名证书 （ie）
# 兼容ie8及以上
# 采用javascript方法，来点击“继续浏览此网站(不推荐)”链接

from selenium import webdriver
import time

# 数据初始化
url2 = "https://vpn.rfchina.com/
# url2 = "https://www.cacert.org/"
browser = webdriver.Ie()

# 打开浏览器
browser.get(url2)
browser.maximize_window()
time.sleep(3)

# 采用javascript方法，来点击“继续浏览此网站(不推荐)。 ”链接
browser.get("javascript:document.getElementById('overridelink').click();")
time.sleep(4)

# 关闭浏览器
browser.close()
