#coding: utf-8

"""
@Author: Well
@Date: 2013-12-01
"""

#2013-12-01
#测试输出
print "你好,谢谢"

#数值运算
print "15**4 = ",15**4
print "15**4 = 15*15*15*15 = ",15*15*15*15
print "15.0/4 = ",15.0/4

#%运算
print "15%4 = ",15%4
print "15.0%4 = ",15.0%4

#布朗运算
print "4>=5",4>=5
print "4<=5",4<=5
print "4>=4",4>=4

#"英寸和厘米"的单位换算
my_inch = "英寸"
my_cm = "厘米"
my_inch_value = 1
my_cm_value = 1

print "%r %s = %.2e %s" % (my_inch_value,my_inch,my_inch_value * 2.54,my_cm) #1英寸转化为厘米
print "%r %s = %.2e %s" % (my_cm_value,my_cm,my_cm_value / 2.54,my_inch) #1厘米转化成英寸

#简写变量运算
my_jianxie = "简写变量运算 %s"
my_jianxie2 = False

print my_jianxie % my_jianxie2

#转义字符
my_zhuanyi = """\t*第一行
\t*第二行
\t*第三行输出反斜杠:\\"""
print "%s" % my_zhuanyi

#输入和输出 01
my_shuru1 = raw_input("please input: ")
print "%s" % my_shuru1
