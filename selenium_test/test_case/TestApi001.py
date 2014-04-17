#coding: utf-8

"""
@Author: Well
@Date: 2014 - 04 - 17
"""

import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
