#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@IDE    ：PyCharm
@Author ：shengbo.tang
@Email  : t975426031@163.com
@Date   ：2021/9/5 22:49
=================================================="""
import unittest


class TestCaseDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('setUpClass')

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass')

    def setUp(self) -> None:
        print('setup')

    def tearDown(self) -> None:
        print('tearDown')

    def test01(self):
        print('1')

    def test02(self):
        print('2')


if __name__ == '__main__':
    unittest.main()
