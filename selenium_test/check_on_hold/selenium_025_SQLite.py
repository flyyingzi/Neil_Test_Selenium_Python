# !/usr/bin/python
#coding: utf-8

"""
@Author: Well
@Date: 2014 - 06 - 25
"""


import sqlite3

conn = sqlite3.connect('/tmp/sqlite_db')
cur = conn.cursor()