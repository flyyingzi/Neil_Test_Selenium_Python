#coding: utf-8

"""
@Author: Well
@Date: 2014 - 03 - 19
"""

import unittest
import my_module


class TestNeil01(unittest.TestCase):

    # def setUp(self):
    # def tearDown(self):

    # 货币乘法验证 page28
    def test_multiplication(self):
        five = my_module.Money.dollar(5)
        self.assertTrue(my_module.Money.dollar(10).equals(five.times(2)))
        self.assertTrue(my_module.Money.dollar(15).equals(five.times(3)))

    # 货币比较（不同数值和货币单位） page42
    def test_equality(self):
        self.assertTrue(my_module.Money.dollar(5).equals(my_module.Money.dollar(5)))
        self.assertFalse(my_module.Money.dollar(5).equals(my_module.Money.dollar(10)))
        self.assertFalse(my_module.Money.dollar(5).equals(my_module.Money.franc(5)))
        self.assertFalse(my_module.Money.dollar(5).equals(my_module.Money.franc(10)))

    # 法郎货币乘法比较 page29
    def test_franc_multiplication(self):
        five = my_module.Money.franc(5)
        self.assertTrue(my_module.Money.franc(10), five.times(2))
        self.assertTrue(my_module.Money.franc(15), five.times(3))

    # 验证实例货币单位 page31
    def test_currency(self):
        self.assertTrue('USD', my_module.Money.dollar(1).currency)
        self.assertTrue('CHF', my_module.Money.franc(1).currency)

    # 不同类进行初始化 page42
    def test_different_class_equality(self):
        self.assertTrue(my_module.Money(10, 'CHF').equals(my_module.Money.franc(10)))

    # 货币加法 page48
    def test_simple_addition(self):
        five = my_module.Money.dollar(5)
        sum_ = five.plus(five)
        reduced = my_module.Money.reduce(sum_, 'USD')
        self.assertTrue(my_module.Money.dollar(10).equals(reduced))

    # 货币加法 page49 (可以伪实现)
    # def test_plus_return_sum(self):
    #     five = my_module.Money.dollar(5)
    #     result = five.plus_money(five)
    #     self.assertTrue(five.equals(result.augend))
    #     self.assertTrue(five.equals(result.augend))

    # page49
    def test_reduce_sum(self):
        sum_ = my_module.Money.sum(my_module.Money.dollar(3), my_module.Money.dollar(4))
        result = my_module.Bank.reduce(sum_, 'USD')
        # result = sum_.reduce('USD')
        self.assertTrue(my_module.Money.dollar(7).equals(result))

    # page50
    def test_reduce_money(self):
        result = my_module.Bank.reduce(my_module.Money.dollar(1), 'USD')
        #result = my_module.Money.reduce(my_module.Money.dollar(1), 'USD')
        self.assertTrue(my_module.Money.dollar(1).equals(result))

    # page53
    def test_reduce_money_different_currency(self):
        bank = my_module.Bank
        bank.add_rate('USD', 'CHF', 2)
        result = bank.reduce(my_module.Money.franc(2), 'USD')
        self.assertTrue(my_module.Money.dollar(1), result)

    # page54 object 无法直接比较
    # def test_array_equals(self):
    #     self.assertEqual(object({'abc'}), object({'abc'}))

    # page

    # page59
    def test_mixed_addition(self):
        five_dollars = my_module.Money.dollar(5)
        ten_francs = my_module.Money.franc(10)
        bank = my_module.Bank
        bank.add_rate('CHF', 'USD', 0.5)
        result = bank.reduce(five_dollars.plus(ten_francs), 'USD')
        self.assertTrue(my_module.Money.dollar(10).equals(result))

    #page61
    def test_sum_plus_money(self):
        five_dollars = my_module.Money.dollar(5)
        ten_francs = my_module.Money.franc(10)
        bank = my_module.Bank
        bank.add_rate('CHF', 'USD', 0.5)
        sum_ = my_module.Sum(five_dollars, ten_francs).plus(five_dollars)
        result = sum_.reduce('USD')
        self.assertTrue(my_module.Money.dollar(15).equals(result))

    #page62
    def test_sum_times(self):
        five_dollars = my_module.Money.dollar(5)
        ten_francs = my_module.Money.franc(10)
        bank = my_module.Bank
        bank.add_rate('CHF', 'USD', 0.5)
        sum_ = my_module.Sum(five_dollars, ten_francs).times(2)
        result = sum_.reduce('USD')
        self.assertTrue(my_module.Money.dollar(20).equals(result))

    #page63
    def test_plus_same_currency_return_money(self):
        sum_ = my_module.Money.dollar(1).plus(my_module.Money.dollar(1))
        self.assertTrue(isinstance(sum_, my_module.Money))

     #page56
    def test_identity_rate(self):
        self.assertEqual(1, my_module.Bank.rate('USD222', 'USD2'))


if __name__ == '__main__':
    unittest.main()