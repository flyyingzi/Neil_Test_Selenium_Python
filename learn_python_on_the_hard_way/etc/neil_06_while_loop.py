# !/usr/bin/python
#coding: utf-8

"""
@Author: Well
@Date: 2014 - 07 - 05
"""

# 引自：http://www.w3cschool.cc/python/python-while-loop.html

"""
6.1 Python 编程中 while 语句用于循环执行程序，即在某条件下，循环执行某段程序，以处理需要重复处理的相同任务。
执行语句可以是单个语句或语句块。判断条件可以是任何表达式，任何非零、或非空（null）的值均为true。
当判断条件假false时，循环结束。
"""
print "-------6.1-start-------"
count = 0
while count < 9:
    print 'The count is:', count
    count += 1
print "Good bye!"
print "-------6.1-end-------"


"""
6.2 while 语句时还有另外两个重要的命令 continue，break 来跳过循环，continue 用于跳过该次循环，
break 则是用于退出循环，此外"判断条件"还可以是个常值，表示循环必定成立。
"""
print "-------6.2-start-------"
i = 1
while i < 10:
    i += 1
    if i % 2 > 0:     # 非双数时跳过输出
        continue
    print i         # 输出双数2、4、6、8、10

i = 1
while 1:            # 循环条件为1必定成立
    print i         # 输出1~10
    i += 1
    if i > 10:     # 当i大于10时跳出循环
        break
print "-------6.2-end-------"


"""
6.3 无限循环
如果条件判断语句永远为 true，循环将会无限的执行下去。
如: while(True):

"""

"""
6.4 循环使用 else 语句
在 python 中，for … else 表示这样的意思，for 中的语句和普通的没有区别，
else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行，while … else 也是一样。
"""

print "-------6.4-start-------"
count = 0
while count < 5:
    print count, " is  less than 5"
    count += 1
else:
    print count, " is not less than 5"
print "-------6.4-end-------"

"""
6.5 简单语句组
类似if语句的语法，如果你的while循环体中只有一条语句，你可以将该语句与while写在同一行中
注意：无限循环你可以使用 CTRL+C 来中断循环。
"""
print "-------6.5-start-------"
flag = 1

while flag: print 'Given flag is really true!'

print "Good bye!"
print "-------6.5-end-------"




