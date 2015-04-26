#!/usr/bin/env python
# coding: utf-8

"""
@Author: Well
@Date: 2015 - 04 - 24
"""

import requests
import json

url = 'http://shanghaicity.openservice.kankanews.com/public/bus/Getstop'
payload = {'stoptype': '1', 'stopid': '5', 'sid': 'ef4c4d9b38f74a2c80206314cdc63e57'}
r = requests.post(url, data=payload)

print r.status_code
print r.raise_for_status()
print r.json()[0]
print type(r.json()[0]['terminal'])
print r.json()[0]['terminal']
print repr(r.json()[0]['terminal'].encode('gb2312'))
print r.headers
print r.cookies
