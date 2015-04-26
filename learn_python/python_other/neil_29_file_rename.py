#!/usr/bin/env python
#coding: utf-8

"""
@Author: Well
@Date: 2014 - 07 - 20
"""

import os

file_1 = u'C:\FDownload\新楚留香（任贤齐版）\合并'

file_list = os.listdir(file_1)

for line in file_list:
    file_s_1 = line[2:4]
    file_s_2 = line[14:16]
    if file_s_1 != file_s_2:
        line_rep = line.replace(line[2:4], line[14:16], 1)
        print line_rep
        os.rename(file_1 + '\\' + line, file_1 + '\\' + line_rep)

