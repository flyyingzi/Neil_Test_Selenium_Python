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

print""
bulls_on_parade.sing_me_a_song()

# 字典例子
happy_bday1 = {'1st': 'happy birthday to you', '2nd': 'i don\'t want to get sued', '3rd': "so i'll stop right there"}

# 字典中查找元素
print ""
# print happy_bday1['1st']
# print happy_bday1['3rd']
print happy_bday1

# 字典中添加元素
# happy_bday1[1] = "add a line"
# # happy_bday1[2] = "add other line"
# print happy_bday1

# # 字典中删除
# del happy_bday1[1]
# del happy_bday1['1st']
# print happy_bday1