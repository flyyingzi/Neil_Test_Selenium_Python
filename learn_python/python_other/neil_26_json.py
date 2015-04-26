#!/usr/bin/env python
#coding: utf-8

"""
@Author: Well
@Date: 2014 - 06 - 18
"""

# JSON = JavaScript Object Notation
# 序列化（Serialization）：将对象的状态信息转换为可以存储或可以通过网络传输的过程，传输的格式可以是JSON、XML等。反序列化就是从
# -存储区域（JSON，XML）读取反序列化对象的状态，重新创建该对象。
# 引用网址：http://www.cnblogs.com/coser/archive/2011/12/14/2287739.html

import json
import urllib

# url
url = r'http://ip.taobao.com/service/getIpInfo.php?ip=101.225.56.104'
data = urllib.urlopen(url).read()
encoded_data = json.dumps(data)

# to String
print "DATA:", repr(data)
# to json
print "JSON:", encoded_data

decode_data = json.loads(encoded_data)
print type(decode_data)
# print decode_data["data"]
print decode_data












