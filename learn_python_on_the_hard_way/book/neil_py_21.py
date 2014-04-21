#coding: utf-8

"""
@Author: Well
@Date: 2013-03-12
"""

# 习题34：访问列表的元素 pass
# 习题35： 分支和函数

from sys import exit

def gold_room():
    print "this room is full of gold. how much do you take?"

    next = raw_input("> ")
    global how_much
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("man, learn to type number.")

    if how_much < 50:
        print "nice, you win!"
        exit(0)
    else:
        dead("you greedy bastard.")

def bear_room():
    print("here is a bear.")
    print("the bear has a bunch of honey.")
    print ("the fat bear is in front of another door.")
    print ("how are you going to move the bear?")
    brear_moved = False

    while True:
        next = raw_input("> ")

        if next == "take honey":
            dead("the bear eats your face.")
        elif next == "taunt bear" and not brear_moved:
            print "the bear go away, you can go through it now."
            brear_moved = True
        elif next == "taunt bear" and brear_moved:
            dead("the bear eats your legs.")
        elif next == "open door" and brear_moved:
            gold_room()
        else:
            print "i got no idea what that means."


def cthulhu_room():
    print "here is the great evil Cthulhu."
    print "whatever stares at you and you go insane."
    print "do you flee for your life or eat your head?"

    next = raw_input("> ")
    if "flee" in next:
        start()
    elif "head" in next:
        dead("well, that was tasty.")
    else:
        cthulhu_room()

def dead(why):
    print why, "good job!"
    exit(0)

def start():
    print "you are in a dark room."
    print "there is a door to your right and left."
    print "which one do you take?"

    next = raw_input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("you stumble around the room until you starve.")

start()
