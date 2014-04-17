#coding: utf-8

"""
@Author: Well
@Date: 2014-01-27
"""

#习题 17：更多的文件操作

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print"copy from %s to %s" % (from_file, to_file)

in_file = open(from_file)
in_data = in_file.read()

print "the input file is %d byte long" % len(in_data)

print "does the output file exist? %s" % exists(to_file)
print "ready, hit return to continue, ctrl-c to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(in_data)

print "Alright,all done."

out_file.close()
in_file.close()

