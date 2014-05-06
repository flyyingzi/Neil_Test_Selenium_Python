#coding: utf-8

"""
@Author: Well
@Date: 2014 - 04 - 20
"""


# 学习BeautifulSoup
# from: http://blog.csdn.net/a2bgeek/article/details/23252647

import urllib
from bs4 import BeautifulSoup


url = "http://www.weather.com.cn/weather/101020100.shtml"
raw_data = urllib.urlopen(url)
# 初始化
soup = BeautifulSoup(raw_data)

# head
# print soup.find('head')
# print soup.head
# print soup.find(id='weather6h')
# print soup.title
# print soup.find(class_='weatherYubao')
# print soup.find(class_='weatheH1')


# 得到id="7d"的div
tag_7d = soup.find(id="7d")
# 得到class="weatherYubaoBox"的div
tag_weatherYubaoBox = tag_7d.contents[3]
# 这里我只想取当天、明天、后天的天气，也就是class="yuBaoTable"的前三个table，接下来就可以循环去数据了。
resul_test = [tag_weatherYubaoBox.contents[5].find_all("a"), tag_weatherYubaoBox.contents[9].find_all("a"),
              tag_weatherYubaoBox.contents[13].find_all("a")]
result = []
for item in resul_test:
    tmp_dict = {}
    tmp_dict["date"] = item[0].string
    tmp_dict["imgurl"] = ''.join(["http://www.weather.com.cn", item[1].contents[1]["src"]])
    tmp_dict["weather"] = item[2].string
    #中 国天气网的数据在6点以后就没有白天的数据了，所以这里判断了一下。
    if len(item) == 6:
        tmp_dict["low"] = ' '.join([u"夜间", item[3].contents[1].contents[0], item[3].contents[1].contents[1].string])
    else:
        tmp_dict["high"] = ' '.join([u"白天", item[3].contents[1].contents[0], item[3].contents[1].contents[1].string])
        tmp_dict["low"] = ' '.join([u"夜间", item[8].contents[1].contents[0], item[8].contents[1].contents[1].string])
    result.append(tmp_dict)

# 输出显示
for i in result:
    print "------------------------"
    for key, value in i.items():
        print key, value












