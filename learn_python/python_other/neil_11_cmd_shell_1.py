#!/usr/bin/env python
#coding: utf-8

"""
@Author: Well
@Date: 2014 - 04 - 28
"""

# 引用 http://wangwei007.blog.51cto.com/68019/1106857
# windows下的cmd
# os.system 仅仅在一个子终端运行系统命令，而不能获取命令执行后的返回信息
# os.popen  该方法不但执行命令还返回执行后的信息对象

import os

#
command_1 = "dir"
# a = os.system(command_1)
b = os.popen(command_1)
# print type(a)
print type(b)


# str_list = os.popen("dir").readlines()
# print str_list
# for i in str_list:
#     print i.decode('gbk')
#     print "-------------------------"

import subprocess
p = subprocess.Popen('dir', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
print p.stdout.readlines()
for line in p.stdout.readlines():
    print line


import commands
commands.getoutput('dir')
commands.getstatusoutput('dir')

