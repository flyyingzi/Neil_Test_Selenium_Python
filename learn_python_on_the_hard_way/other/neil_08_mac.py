#coding: utf-8

"""
@Author: Well
@Date: 2014 - 04 - 19
"""


import uuid

def get_mac_address():
    # 没有以：隔开，输出显示
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    # 每隔两个字符，添加一个"："
    mac_a = []
    for i in range(0, 11, 2):
        print ":".join(mac[i:i + 2])

    print mac

    print ":".join([mac[e:e + 2] for e in range(0, 11, 2)])

get_mac_address()