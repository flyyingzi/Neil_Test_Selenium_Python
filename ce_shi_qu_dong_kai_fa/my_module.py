#coding: utf-8

"""
@Author: Well
@Date: 2014 - 03 - 20
"""


class Money(object):
    # 初始化
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    # 乘法
    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)

    # 比较相等（数量和货币单位）
    def equals(self, other):
        return self.amount == other.amount and self.currency == other.currency

    # dollar 静态方法
    @staticmethod
    def dollar(amount):
        return Money(amount, 'USD')

    # franc 静态方法
    @staticmethod
    def franc(amount):
        return Money(amount, 'CHF')

    # 根据 currency，兑换货币
    def reduce(self, currency):
        rate = 1.0 if (self.currency == currency) else 2.0
        if self.currency == 'USD':
            return Money(self.amount * rate, currency)
        if self.currency == 'CHF':
            return Money(self.amount / rate, currency)
        else:
            print ('currency is wrong.')

    # 加法（已考虑不同货币）
    def plus(self, other):
        return Sum(self, other)

    # 加法（已考虑不同货币）（静态方法）
    @staticmethod
    def sum(augend, addend):
        amount = augend.amount + addend.reduce(augend.currency).amount
        if augend.currency == 'USD':
            return Money.dollar(amount)
        if augend.currency == 'CHF':
            return Money.franc(amount)
        else:
            print "currency is wrong."

class Dollar(Money):
    pass

class Franc(Money):
    pass

class Sum(Money):
    # 属性：augend, addend
    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend
        self.amount = augend.amount + addend.reduce(augend.currency).amount
        self.currency = augend.currency

class Bank(object):
    # 属性： currency_from, currency_to, rate
    def __init__(self, currency_from, currency_to, rate):
        self.currency_from = currency_from
        self.currency_to = currency_to
        self.rate = rate

    @staticmethod
    def add_rate(currency_from, currency_to, rate):
        return Bank(currency_from, currency_to, rate)

    @staticmethod
    def rate(currency_from, currency_to):
        if currency_from == currency_to:
            return 1
        else:
            if currency_from == 'USD':
                return 2.0
            else:
                return 1 / 2.0

    @staticmethod
    def reduce(money, currency):
        return Money.reduce(money, currency)

class Pair(object):
    def __init__(self, currency_from, currency_to):
        self.currency_from = currency_from
        self.currency_to = currency_to

    def hash_code(self):
        return 0