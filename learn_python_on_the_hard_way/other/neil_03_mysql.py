#coding: utf-8

"""
@Author: Well
@Date: 2014 - 04 - 03
"""
# 连接mysql数据库，进行操作
# 用的是官方mysql connector/python
# 参考网页
# http://www.cnblogs.com/fnng/p/3565912.html

from mysql import connector

# 定义连接数据库的信息
user = 'root'
password = ''
host = '127.0.0.1'
port = 3306
db = 'test'
# 创建table
# create_sql1 = "create table student(id int,name varchar(20),class varchar(30),age varchar(10))"
# create_sql2 = "create table a(Id int,Name varchar(20))"
# create_sql3 = "create table a(Id int,Name varchar(20))"
# 插入数据
insert_sql1 = "insert into a values(%s, %s)"
insert_sql2 = "insert into b values(%s, %s)"
list1 = [('1', u'张三'), ('2', u'李四'), ('3', u'王五'), ('4', u'刘六'), ('5', u'赵七')]
list2 = [('1', u'张三'), ('2', u'李四'), ('6', u'金八'), ('7', u'肖九'), ('8', u'钱十')]
# 查询
# 内连接
select_sql1 = "select a.*,b.* from a inner join b on a.id = b.id"
# 左外连接
select_sql2 = "select a.*,b.* from a left join b on a.id = b.id"
# 右外连接
select_sql3 = "select * from a right join b on a.id = b.id"
# 全外连接
# select_sql4 = "select a.*,b.* from a full join b on a.id = b.id"
# 自连接
select_sql5 = "select * from a a1 left join a a2  on a1.id = a2.id"
# a和b表中，id仅存在b中的用户名
select_sql6 = "select b.name from a right join b on a.id = b.id where a.id is null"

# 修改
update_sql = ""

# 连接数据库
conn = connector.connect(user=user, password=password, host=host, port=port, db=db)
cur = conn.cursor()

# # 往a中插入多条数据
# try:
#     cur.executemany(insert_sql1, list1)
# except:
#     print "insert table a failed"
#
#
# # 往b中插入多条数据
# try:
#     cur.executemany(insert_sql2, list2)
# except:
#     print "insert table b failed"


# 查询
# 内连接
print "--------------------1------------------------"
cur.execute(select_sql1)
print cur
print cur.fetchmany(1)
# 游标从2开始输出
print cur.fetchall()
for i in cur:
    print i
print "--------------------2------------------------"
# 左外连接
cur.execute(select_sql2)
for i in cur:
    print i
print "--------------------3------------------------"
# 右外连接
cur.execute(select_sql3)
for i in cur:
    print i
print "--------------------4------------------------"
# 自连接
cur.execute(select_sql5)
for i in cur:
    print i
print "--------------------5------------------------"
cur.execute(select_sql6)
for i in cur:
    print i
print "---------------------------------------------"

cur.execute('show tables')
for i in cur:
    print i


# 关闭游标
cur.close()
# 提交数据
conn.commit()
# 关闭数据库
conn.close