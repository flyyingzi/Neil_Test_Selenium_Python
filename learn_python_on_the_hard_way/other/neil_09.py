#coding: utf-8

"""
@Author: Well
@Date: 2014 - 04 - 20
"""


# 学习BeautifulSoup

import urllib2
import BeautifulSoup


url = "http://www.baidu.com"
response = urllib2.urlopen(url)
page_ = response.read()
print type(page_)

# 初始化
soup = BeautifulSoup.BeautifulSoup(page_)
# find方法
head = soup.find('head')


# contents属性,list
html2 = soup.contents[2]
head2 = html2.contents
body2 = html2.contents[1]

print head2











