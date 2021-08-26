# encoding: utf-8
"""
@author: John
@contact: zhouqiang847@gmail.com
@file: liteNameTuple.py	
@time: 2021/8/26	
"""
from operator import itemgetter


class NameTuple(tuple):
    _field_names = ('x', 'y')

    x = property(itemgetter(0))
    y = property(itemgetter(1))

    @classmethod
    def _make(cls, iterable):
        return cls.__new__(cls, iterable)

    def _asdict(self):
        return dict(zip(NameTuple._field_names, self))

    def _replace(self, **kwargs):
        return self._make(map(kwargs.pop, NameTuple._field_names, self))


if __name__ == '__main__':
    point = NameTuple([1, 2])
    print(point[0] + point[1])
    print(point.x + point.y)
    x, y = point
    print(x, y)

