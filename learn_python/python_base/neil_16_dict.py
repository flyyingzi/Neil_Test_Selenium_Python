#!/usr/bin/env python
#coding: utf-8

"""
@Author: Well
@Date: 2014 - 07 - 05
"""

# 引自： http://www.w3cschool.cc/python/python-dictionary.html

"""
16.1 字典是另一种可变容器模型，且可存储任意类型对象，如其他容器模型。
字典由键和对应值成对组成。字典也被称作关联数组或哈希表。
基本语法如下:
dict1 = { 'abc': 456 }
dict2 = { 'abc': 123, 98.6: 37 }

注意：
1）每个键与值用冒号隔开（:），每对用逗号，每对用逗号分割，整体放在花括号中（{}）。
2）键必须独一无二，但值则不必。
3）值可以取任何数据类型，但必须是不可变的，如字符串，数或元组。
"""


"""
16.2 访问字典里的值
把相应的键放入熟悉的方括弧。
如：
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

print "dict['Name']: ", dict['Name']
print "dict['Age']: ", dict['Age']

注意：如果用字典里没有的键访问数据，会输出错误
"""


"""
16.3 修改字典
向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对
如：
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry


print "dict['Age']: ", dict['Age']
print "dict['School']: ", dict['School']
"""


"""
16.4 删除字典元素
能删单一的元素也能清空字典，清空只需一项操作。
如：
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

del dict['Name'] # 删除键是'Name'的条目
dict.clear()     # 清空词典所有条目
del dict         # 删除词典

"""

"""
16.5 字典内置函数&方法
"""
"""
内置函数:
cmp(dict1, dict2)
比较两个字典元素。

len(dict)
计算字典元素个数，即键的总数。

str(dict)
输出字典可打印的字符串表示。

type(variable)
返回输入的变量类型，如果变量是字典就返回字典类型。
"""
"""
还包含以下内置函数：
radiansdict.clear()
删除字典内所有元素

radiansdict.copy()
返回一个字典的浅复制

radiansdict.fromkeys()
创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值

radiansdict.get(key, default=None)
返回指定键的值，如果值不在字典中返回default值

radiansdict.has_key(key)
如果键在字典dict里返回true，否则返回false

radiansdict.items()
以列表返回可遍历的(键, 值) 元组数组

radiansdict.keys()
以列表返回一个字典所有的键

radiansdict.setdefault(key, default=None)
和get()类似, 但如果键不已经存在于字典中，将会添加键并将值设为default

radiansdict.update(dict2)
把字典dict2的键/值对更新到dict里

radiansdict.values()
以列表返回字典中的所有值
"""


















