#coding: utf-8

"""
@Author: Well
@Date: 2014 - 05 - 07
"""

# lambda
# “相对地址”转换成“绝对地址”

import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

print PATH("../../book")

# “相对地址”转换成“绝对地址”
print os.path.basename("../../book")
# 父路径地址
print os.path.dirname(__file__)
# 路径的最后一个节点
print os.path.basename(__file__)
# 当前脚本运行的路径
print os.getcwd()
# 文件列表
print os.listdir(os.getcwd())
# 当前目录
print os.path.abspath("./")
# 当前目录的上一级目录
print os.path.abspath("../")
# 当前目录的上两级目录
print os.path.abspath("../../")