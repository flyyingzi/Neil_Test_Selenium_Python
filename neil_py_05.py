#coding: utf-8

"""
@Author: Well
@Date: 2014-01-27
"""
from sys import argv
from os.path import exists

script, from_file,to_file = argv

print"copy from %s to %s" % (from_file, to_file)

in_file = open(from_file)
indata =in_file.read()

print "the input file is %d byte long" % len(indata)

print "does the output file exist? %s" % exists(to_file)
print "ready, hit return to continue, ctrl-c to abort."
raw_input()

out_file = open(to_file,'w')
out_file.write(indata)

print "Alright,all done."

out_file.close()
in_file.close()

