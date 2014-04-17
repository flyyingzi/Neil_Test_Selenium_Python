#coding: utf-8

"""
@Author: Well
@Date: 2014 - 04 - 14
"""

import MySQLdb

def python_mysql_test():
    """
    try to use mysql in python
    """
conn = MySQLdb.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='neil123',
    db='test'
)
cur = conn.cursor()

show_tables = cur.execute('show tables')
print "show_tables", show_tables

conn.commit()
cur.close()
conn.close()

if __name__ == "__main__":
    python_mysql_test()
