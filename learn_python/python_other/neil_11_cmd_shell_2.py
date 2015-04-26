#!/usr/bin/env python
#coding: utf-8

"""
@Author: Well
@Date: 2014 - 06 - 17
"""

# 引用 http://wangwei007.blog.51cto.com/68019/1106857
# linux 下面的 bash shell

import os

print "hello"

# 创建文件 test
file_path = "/home/py/test"
os.mknod(file_path)

# 判断文件 test 是否存在
if os.path.exists(file_path):
    os.remove(file_path)
    print "remove ok"

# 切换到etc目录，创建文件test
os.system("cd /etc")
os.system("mkdir test")