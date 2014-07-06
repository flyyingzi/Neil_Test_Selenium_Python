#coding: utf-8

"""
@Author: Well
@Date: 2014 - 05 - 03
"""

# join 来连接字符串
# split 拆分字符串

# join
list_1 = ['my', 'name', 'is', 'neil']
print ''.join(list_1)
print '--'.join(list_1)
print ' '.join(list_1)
print '..'.join(list_1)
print '------------------------------'
# split
list_2 = 'my..name..is..neil'

print list_2.split()
print list_2.split('..')
print list_2.split('..', 1)
print list_2.split('..', 2)
print list_2.split('..', 2)  # 输出效果等同于 print list_2.split('..')

# 输出结果：
# mynameisneil
# my--name--is--neil
# my name is neil
# my..name..is..neil
# ------------------------------
# ['my..name..is..neil']
# ['my', 'name', 'is', 'neil']
# ['my', 'name..is..neil']
# ['my', 'name', 'is..neil']
# ['my', 'name', 'is..neil']

