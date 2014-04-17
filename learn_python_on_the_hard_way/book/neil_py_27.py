#coding: utf-8

"""
@Author: Well
@Date: 2014 - 03 - 27
"""

# 习题41: 物以类聚
# 习题42：对象，类，以及从属关系

# 声明 Animal
class Animal(object):
    pass

# Dog 继承 Animal
class Dog(Animal):
    def __init__(self, name):
        # 变量 name
        self.name = name

# Cat 继承 Animal
class Cat(Animal):
    def __init__(self, name):
        # 变量 name
        self.name = name

# 声明 person
class Person(object):
    def __init__(self, name):
        # 变量 name
        self.name = name
        # 变量 pet
        self.pet = None
#  employee 继承 person
class Employee(Person):
    def __init__(self, name, salary):
        # 变量 name
        super(Employee, self).__init__(name)
        # 变量 salary
        self.salary = salary

# 声明 fish
class Fish(object):
    pass

# 声明 salmon
class Salmon(Fish):
    pass

# 声明 halibut
class Halibut(Fish):
    pass

# 类的实例化
rover = Dog('Rover')
satan = Cat('Satan')
mary = Employee('mary', 1000)
print mary.name, mary.pet, mary.salary
print isinstance(mary, Person)
print issubclass(Employee, Person)
