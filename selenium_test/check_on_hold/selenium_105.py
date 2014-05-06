#coding: utf-8

"""
@Author: Well
@Date: 2014 - 05 - 02
"""


from selenium import webdriver

browser = webdriver.PhantomJS()
browser.get("http://www.baidu.com")

print browser.find_element_by_link_text(u"百科").get_attribute("href")
