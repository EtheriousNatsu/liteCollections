# encoding: utf-8
"""
@author: john
@contact: zhouqiang847@gmail.com
@file: test_orderdict.py
@time: 2021/9/2 上午1:39
@desc:
"""
from unittest import TestCase

from orderDict import OrderDict


class TestOrderDict(TestCase):
    def setUp(self) -> None:
        self.dict = OrderDict()
        self.dict['x'] = 1
        self.dict['y'] = 2

    def test_get(self):
        self.assertEqual(1, self.dict['x'])

    def test_pop(self):
        self.assertEqual(1, self.dict.pop('x'))

    def test_iterate(self):
        for k in self.dict:
            self.assertIn(k, ['x', 'y'])
