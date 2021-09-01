# encoding: utf-8
"""
@author: john
@contact: zhouqiang847@gmail.com
@file: orderDict.py
@time: 2021/8/28 下午12:43
@desc:
"""
from typing import Generator, TypeVar

K = TypeVar('K')
V = TypeVar('V')
T = TypeVar('T')


class Link:
    def __init__(self) -> None:
        self.key = None
        self.prev = None
        self.next = None


class OrderDict(dict):
    def __init__(self) -> None:
        self.__mapping = {}
        self.__root = root = Link()
        root.next = root.prev = root

    def __setitem__(self, key: K, value: V) -> None:
        if key not in self:
            self.__mapping[key] = link = Link()
            root = self.__root
            last = root.next
            link.next, link.prev, link.key = root, last, key
            last.next = link
            root.prev = link

        super().__setitem__(key, value)

    def __delitem__(self, key: K) -> None:
        super().__delitem__(key)
        link = self.__mapping[key]
        link_next = link.next
        link_prev = link.prev
        link_prev.next = link_next
        link_next.prev = link_prev
        link_next = None
        link_prev = None
        link.key = None

    _marker = object()

    def pop(self, key: K, default: T = _marker):
        if key in self:
            result = self[key]
            del self[key]
            return result
        if default is self._marker:
            raise KeyError(key)
        return default

    def __iter__(self) -> Generator[T, None, None]:
        root = self.__root
        curr = root.next
        while curr is not root:
            yield curr.key
            curr = curr.next
