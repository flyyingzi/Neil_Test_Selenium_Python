#coding: utf-8

"""
@Author: Well
@Date: 2014-03-14
"""

# 习题39: 字典，可爱的字典_1

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["happy birthday to you",
                   "i don't want to get sued",
                   "so i'll stop right there"])

bulls_on_parade = Song(["they rally around the family",
                        "with pockets full of shells"])

happy_bday.sing_me_a_song()
print('\n')
bulls_on_parade.sing_me_a_song()