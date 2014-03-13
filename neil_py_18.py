#coding: utf-8

"""
@Author: Well
@Date: 2014-03-12
"""

#习题31：做出决定

print "you enter a dark room with two doors. go #1 door or #2 door?"

door = raw_input("> ")

if door == "1":
    print "a bear and a cake with you, do what?"
    print "1. take the cake"
    print "2. scream at the bear"

    bear = raw_input("> ")

    if bear == "1":
        print "bear eat your face."
    elif bear == "2":
        print "bear eat your legs."
    else:
        print "do %s is better.bear runs away." % bear

elif door == "2":
    print "you stare into the endless abyss at cthulhu's retina"
    print "1.blueberries"
    print "2.yellow jacket clothespins"
    print "3.understanding revolvers yelling melodies"

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "more power with your body."
    else:
        print "insanity rots your eyes into a pool of muck."

else:
    print "stumble and die."
