#coding: utf-8

"""
@Author: Well
@Date: 2014 - 04 - 29
"""

# s.strip(rm)        删除s字符串中开头、结尾处，位于 rm删除序列的字符
# 当rm为空时，默认删除空白符（包括'\n', '\r',  '\t',  ' ')
# s.lstrip(rm)       删除s字符串中开头处，位于 rm删除序列的字符
# s.rstrip(rm)      删除s字符串中结尾处，位于 rm删除序列的字符

import string


a1 = '   123123'
a2 = '\t\t123'
a3 = '123\r\n'

print a1.strip()
print a2.strip()
print a3.strip()
print "-----------------------"

# 删除开头和结尾
print a1.strip().strip('13')
print "-----------------------"

# 删除开头
print a1.strip().lstrip('21')
print a1.strip().lstrip('12')
print "-----------------------"

# 删除结尾
print a1.strip().rstrip('23')

# 替换固定的字符
print string.replace(a1, '1', '', 1)

