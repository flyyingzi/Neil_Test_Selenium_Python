#coding: utf-8

"""
@Author: Well
@Date: 2013 - 03 - 28
"""

# 习题44： 继承 inheritance VS 合成 Composition
# 隐式继承
# 显式继承
# 运行前或者运行后 复写

# 隐式继承

class Parent(object):
    def implicit(self):
        print "PARENT implicit()"

# 隐式继承
class Child(Parent):
    pass

# 显式继承
class Child2(Parent):
    def override(self):
        print "CHILD override()"

# 运行前或者运行后 复写
class Child3(Parent):
    def altered(self):
        print("Before PARENT implicit() ")
        super(Child3, self).implicit()
        print("After PARENT implicit() ")


range(0, 10, 2)


dad = Parent()
son = Child()
son2 = Child2()
son3 = Child3()

dad.implicit()
son.implicit()
son2.override()
son3.altered()
