#coding: utf-8

"""
@Author: Well
@Date: 2013 - 03 - 27
"""
# 习题40：模块 类 和对象
# 模块和字典差不多
# 类和模块差不多
# 对象相当于迷你版的 import

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

# 遍历列表
happy_day = Song(["Happy birthday to you",
                  "I don't want to get sued",
                  "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_day.sing_me_a_song()
print ('')
bulls_on_parade.sing_me_a_song()

# 遍历元组
test = ('a', 'b', 'c')
for x in range(len(test)):
    print x, test[x]

# 遍历字典
test2 = {2: 'fly1', 'no2': 'fly2', 'hello': 'fly3'}
for key in test2.keys():
    print key, '\n', test2[key]

