#coding: utf-8

"""
@Author: Well
@Date: 2014 - 05 - 14
"""
# python2 默认为ascii编码
# 中文无法用ascii解码

# ok
print "%s-%s" % (u"中国", u"2233")
print "%s-%s" % (u"中国", "2233")

#
# print "%s-%s" % ("中国", u"2233")
print "%s-%s" % ("中国", "2233")

print isinstance(u"中国", unicode)
print isinstance("中国", unicode)

print u"中国".encode("gb2312")

# print u"中国".decode("utf-8")

s = u"中文"

#s=u"中文"
if isinstance(s, unicode):
    print s.encode('utf-8')
#s="中文"
else:
    print s.decode('utf-8').encode('utf-8')