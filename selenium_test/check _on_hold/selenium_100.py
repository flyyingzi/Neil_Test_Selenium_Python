#coding: utf-8

"""
@Author: Well
@Date: 2014 - 04 - 03
"""
# 连接mysql数据库，进行操作
# 用的是官方mysql connector/python

from mysql import connector
import sys

user = 'root'
password = ''
host = 'localhost'
port = 3306
db = 'test'

# 创建
create_table_sql = "create table student(id int ,name varchar(20),class varchar(30),age varchar(10))"
# 插入
insert_sql = ""
# 查询
select_sql = ""

conn = connector.connect(user=user, password=password, host=host, port=port, db=db)
cur = conn.cursor()

try:
    cur.execute(create_table_sql)
except connector.Error as err:
    print "create table 'student' failed"
    print("Error:{}".format(err.msg))
    sys.exit()

conn.commit()
cur.close()
conn.close




# cur.execute("delete from student where age='9'")


cur.close()
conn.commit()
conn.close()



