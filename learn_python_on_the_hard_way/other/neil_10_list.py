#coding: utf-8

"""
@Author: Well
@Date: 2014 - 04 - 20
"""

a = [y + 1 for y in range(12)]
b = range(12)
c = list(range(12))

print a, b, c
d = (lambda x: x ** i for i in range(4))
print d
for i in d:
    print i(4)