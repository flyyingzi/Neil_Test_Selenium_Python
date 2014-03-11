#coding: utf-8

"""
@Author: Well
@Date: 2014-01-27
"""

#习题 16：读写文件

from sys import argv

#filename 设置为 neil_txt_sample3.txt
script, filename = argv

print "Erase %r" % filename
print "If you don't want that, hit CTRL-C."
print "If you do want that,hit RETURN."

raw_input("?")

print "Opening the file"
target = open(filename, 'r+')

print "Truncating the file.Goodbye!"
target.truncate()

print "Ask you for three lines."

line1 = raw_input("line1:")
line2 = raw_input("line2:")
line3 = raw_input("line3:")

print "Write three lines to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

target.seek(0)
for line in target:
    print line

print "Finally, close it"

target.close()


