# !/usr/bin/python
# coding: utf-8

"""
@Author: Well
@Date: 2014 - 07 - 05
"""


file_1 = r'C:\Users\wei\Documents\GitHub\neil_test_selenium\learn_python_on_the_hard_way\etc\neil_01_base.py'

file_data = open(file_1).read()

for i in range(22, 33):
    file_path = r'C:\Users\wei\Documents\GitHub\neil_test_selenium\learn_python_on_the_hard_way\etc' + '\\' + 'neil_' \
                + str(i) + '_.py'
    open(file_path, 'w+').write(file_data)