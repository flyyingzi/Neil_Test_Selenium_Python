#coding: utf-8

"""
@Author: Well
@Date: 2014-01-26
"""

#习题13：参数，解包，变量
from sys import argv
# noinspection PyPep8,PyPep8,PyPep8
my_argv_script, my_argv_test1, my_argv_test2, my_argv_test3 = argv
# noinspection PyPep8
print "script", my_argv_script
# noinspection PyPep8
print "test1", my_argv_test1
# noinspection PyPep8
print "test2", my_argv_test2
print "test3", my_argv_test3