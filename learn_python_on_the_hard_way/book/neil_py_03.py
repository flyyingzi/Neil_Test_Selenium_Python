#coding: utf-8

"""
@Author: Well
@Date: 2013-01-26
"""
#习题14：提示和传递
# noinspection PyPep8
from sys import argv

script, user_name = argv
prompt = '>'

# noinspection PyPep8
print "hi %s, I'm the %s script." % (user_name, script)
print "Do you like me, %s?" % user_name
likes = raw_input(prompt)

# noinspection PyPep8
print "Where do you live, %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

# noinspection PyPep8,PyPep8
print """
Alright, so you said %r about liking me.
You live in %r,Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
