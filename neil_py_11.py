#coding: utf-8

"""
@Author: Well
@Date: 2014-03-12
"""

#习题22: 到现在你学到了哪些东西（pass）
#习题23：读代码 （pass）
#习题24：更多练习

print "Practise everything."
print 'You\'d need to know \'about escapes with \\ that do \n newlines and \t table '

poem = """
\t the first line
the second line
the third line \n the fourth line
the fifth line
the sixth line
\n\t the seventh line
"""
print "----------"
print poem
print "----------"

five = 10 - 2 + 3 - 6
print "this should be five: %s" % five


def secret_formula(started):
    jelly_beans = started * 500
    jelly_jars = jelly_beans / 1000
    jelly_crates = jelly_jars / 100
    return jelly_beans, jelly_jars, jelly_crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "starting point: %d" % start_point
print "we have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point /= 10

print "we can also do that this way."
print "we have %d beans, %d jars, and %d crates." % (secret_formula(start_point))