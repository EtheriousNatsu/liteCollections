# encoding: utf-8
"""
@author: john
@contact: zhouqiang847@gmail.com
@file: test_nametuple.py
@time: 2021/9/2 上午12:50
@desc:
"""
import unittest

from nameTuple import NameTuple


class TestNameTuple(unittest.TestCase):

    def setUp(self) -> None:
        self.t: NameTuple = NameTuple([1, 2])

    def test_acdict(self) -> None:
        self.assertDictEqual(self.t._asdict(), {'x': 1, 'y': 2})

    def test_replace(self) -> None:
        self.assertDictEqual(self.t._replace(x=3)._asdict(), {'x': 3, 'y': 2})

    def test_make(self) -> None:
        tt: tuple = (11, 12)
        self.assertDictEqual(NameTuple._make(tt)._asdict(), {'x': 11, 'y': 12})
