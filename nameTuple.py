# encoding: utf-8
"""
@author: John
@contact: zhouqiang847@gmail.com
@file: nameTuple.py
@time: 2021/8/26
"""
from operator import itemgetter
from collections.abc import Iterable
from typing import TypeVar

T = TypeVar('T')


class NameTuple(tuple):
    _field_names = ('x', 'y')

    x = property(itemgetter(0))
    y = property(itemgetter(1))

    @classmethod
    def _make(cls, iterable: Iterable) -> 'NameTuple':
        return cls.__new__(cls, iterable)

    def _asdict(self) -> dict:
        return dict(zip(NameTuple._field_names, self))

    def _replace(self, **kwargs: T) -> 'NameTuple':
        return self._make(map(kwargs.pop, NameTuple._field_names, self))

