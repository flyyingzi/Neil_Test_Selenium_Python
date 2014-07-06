# coding: utf-8

"""
@Author: Well
@Date: 2014 - 04 - 20
"""

# 引用网址：http://yangsq.iteye.com/blog/128508
# 详解：  元组、列表、字典、文件


# 1.元组的特性:
# 任意对象的有序集合
# 通过偏移读取
# 一旦生成，不可改变
# 固定长度，支持嵌套

tuple_1 = (0, 'haha', (4j, 'y'))
tuple_2 = (1, 3, 'bb')

print 'tuple start' + '---------------------------------'
print tuple_1
print tuple_1[-1]
print tuple_2[2]
print tuple_2[-1]
print tuple_2[0:-1]  # 序列是包头，不包尾

print '---------------------------------'
print tuple_2 * 2  # 倍速拼接
print tuple_1 + tuple_2  # 不同元组进行拼接
print tuple_2 + ((1, 'test'),)

print '---------------------------------'
print 'bb' in tuple_2  # 判断包含关系

# 循环输出显示
for i in tuple_2:
    print i

for i in (2, (3, '1')):
    print i

print '---------------------------------'
print len(tuple_1)
print len(tuple_2)

print '---------------------------------'
# 一旦生成，就不可变了
tuple_3 = (1, 2, tuple_2)
print tuple_3
print tuple_2 in tuple_3

tuple_2 = (1, 3)
print tuple_3  # tuple_3不会因tuple_2的改变而改变
print tuple_2 in tuple_3

print 'tuple end' + '---------------------------------'

# 2. 列表的特性：
# 任意对象的有序集合；
# 可通过偏移存取，注意，列表中的元素都是可变的，这是不同于元组的；
# 长度可变，支持嵌套；
# 还有一些类似java的对象引用机制

list_1 = ['aa', 'bb', 'cc']

# 基本操作
print 'list start' + '---------------------------------'
print len(list_1)
print list_1 + ['d']
print list_1 * 3
for i in list_1 * 2:
    print i

# 索引和分片，赋值
print '---------------------------------'
print list_1[2]
print list_1[:2]
print list_1[-1]

list_1[2] = 'music'
print list_1

list_1[1:] = ['bbb', 'ccc', 'eee']
print list_1

# 添加，排序 和 删除操作
#
list_1.append(111)
print '---------------------------------'
print list_1

list_1.sort()
print list_1

del list_1[0]
print list_1

try:
    list_1.remove('22')

except ValueError:
    print 'ValueError'

finally:
    print list_1

list_1.pop(-1)
print list_1

# 有趣的用法

























