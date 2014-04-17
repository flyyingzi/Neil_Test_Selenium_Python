#coding: utf-8

"""
@Author: Well
@Date: 2014 - 04 - 11
"""

#  弹出页面

from selenium import webdriver
import time

profile = webdriver.FirefoxProfile()
profile.accept_untrusted_certs = True
#browser = webdriver.Firefox(firefox_profile=profile)
browser = webdriver.Ie()
#browser = webdriver.Chrome()

url1 = "http://piao.fanli.com/?source=12306"
url2 = "https://www.cacert.org/"


browser.get(url2)
browser.maximize_window()
time.sleep(3)


browser.find_element_by_partial_link_text("继续浏览此网站").click()
time.sleep(3)

# browser.close()
