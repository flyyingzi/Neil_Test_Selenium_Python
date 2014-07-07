# !/usr/bin/python
#coding: utf-8

"""
@Author: Well
@Date: 2014 - 07 - 05
"""

# 引自： http://www.w3cschool.cc/python/python-lists.html

"""
14.1 列表
(列表是最常用的Python数据类型，它可以作为一个方括号内的逗号分隔值出现。列表的数据项不需要具有相同的类型)

序列是Python中最基本的数据结构。序列中的每个元素都分配一个数字 - 它的位置，或索引，第一个索引是0，第二个索引是1，依此类推。
序列都可以进行的操作包括索引，切片，加，乘，检查成员。
此外，Python已经内置确定序列的长度以及确定最大和最小的元素的方法。
"""


"""
14.2 访问列表中的值
使用下标索引来访问列表中的值，同样你也可以使用方括号的形式截取字符
如：
list1[0]
list2[1:5]
"""


"""
14.3 更新列表
你可以对列表的数据项进行修改或更新，你也可以使用append()方法来添加列表项
也可以使用append()方法来添加列表项
"""
print "-------14.3-start-------"
list_ = ['physics', 'chemistry', 1997, 2000]

print "Value available at index 2 : "
print list_[2]
list_[2] = 2001
print "New value available at index 2 : "
print list_[2]
print "-------14.3-end-------"


"""
14.4 删除列表元素
可以使用 del 语句来删除列表的的元素
如：
list_ = ['physics', 'chemistry', 1997, 2000]
del list_[2]
"""


"""
14.5 列表脚本操作符

Python表达式	结果 	描述
len([1, 2, 3])	3	长度
[1, 2, 3] + [4, 5, 6]	[1, 2, 3, 4, 5, 6]	组合
['Hi!'] * 4	['Hi!', 'Hi!', 'Hi!', 'Hi!']	重复
3 in [1, 2, 3]	True	元素是否存在于列表中
for x in [1, 2, 3]: print x,	1 2 3	迭代
"""


"""
14.6 列表截取

Python的列表截取与字符串操作类型, 如下：
L = ['spam', 'Spam', 'SPAM!']

操作：
L[2]	'SPAM!'	读取列表中第三个元素
L[-2]	'Spam'	读取列表中倒数第二个元素
L[1:]	['Spam', 'SPAM!']	从第二个元素开始截取列表
"""


"""
14.7 列表函数&方法

Python包含以下函数:
cmp(list1, list2)  比较两个列表的元素
len(list)  列表元素个数
max(list)  返回列表元素最大值
min(list)  返回列表元素最小值
list(seq)  将元组转换为列表

Python包含以下方法:

list.append(obj)    在列表末尾添加新的对象
list.count(obj)     统计某个元素在列表中出现的次数
list.extend(seq)    在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list.index(obj)     从列表中找出某个值第一个匹配项的索引位置
list.insert(index, obj)     将对象插入列表
list.pop(obj=list[-1])      移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
list.remove(obj)    移除列表中某个值的第一个匹配项
list.reverse()      反向列表中元素
list.sort([func])       对原列表进行排序
"""

