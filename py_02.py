#coding: utf-8

"""
@Author: Well
@Date: 2014-03-09
"""

#习题20: 函数和文件


current_file = "neil_txt_sample3.txt"
data = open(current_file)
# current_line = 1
# while current_line <= 6:
#     print current_line
#     current_line += 1
file_len = len(data.readlines())
print file_len