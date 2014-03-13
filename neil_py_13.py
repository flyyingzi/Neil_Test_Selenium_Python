#coding: utf-8

"""
@Author: Well
@Date: 2014-03-12
"""

#习题25: 更多更多的练习 -2

import neil_py_12

sentence = "all good things come to those who wait"
words = neil_py_12.break_words(sentence)
sorted_words = neil_py_12.sort_words(words)

print words
print sorted_words
neil_py_12.print_first_word(words)
neil_py_12.print_last_word(words)
print words
neil_py_12.print_first_word(sorted_words)
neil_py_12.print_last_word(sorted_words)
neil_py_12.print_first_and_last(sentence)
neil_py_12.print_first_and_last_sorted(sentence)