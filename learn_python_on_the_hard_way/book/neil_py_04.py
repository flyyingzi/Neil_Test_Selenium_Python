#coding: utf-8

"""
@Author: Well
@Date: 2013-01-26
"""

#习题15; 读取文件

from sys import argv
import codecs

script, filename = argv
txt = open(filename).read()

print "here's your file %r:" % filename

#文本文件格式为utf-8或者无bom utf-8,需要处理下
if txt[:3] == codecs.BOM_UTF8:
    txt = txt[3:]
print txt.decode("utf-8")

print "type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)
data = txt_again.read()
#文本文件格式为utf-8或者无bom utf-8,需要处理下
if data[:3] == codecs.BOM_UTF8:
    data = data[3:]
print data.decode("utf-8")
