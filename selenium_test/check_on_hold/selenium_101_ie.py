#coding: utf-8

"""
@Author: Well
@Date: 2014 - 04 - 11
"""

#  自签名证书 （ie）
#  将 证书 添加到 “受信任的根证书颁发机构”
#  方法如：http://bbs.pcbeta.com/forum.php?mod=viewthread&tid=601017

from selenium import webdriver
import time

# 数据初始化
url2 = "https://vpn.rfchina.com/"
browser = webdriver.Ie()

# 打开浏览器
browser.get(url2)
browser.maximize_window()
time.sleep(3)


# 关闭浏览器
browser.close()
