#coding: utf-8

"""
@Author: Well
@Date: 2013 - 04 - 04
"""

# 习题45：你来制作一个游戏 pass
# 习题46：一个项目骨架 pass
# 习题47：自动化测试  pass
# 习题48：更复杂的用户输入

# split 方法
words = " 你好 , study python. "
for i in words.split():
    print i


# 异常 和 数字
def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

print convert_number(-1)
print convert_number('aaa')







