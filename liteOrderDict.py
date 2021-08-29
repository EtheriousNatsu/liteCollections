# encoding: utf-8
"""
@author: john
@contact: zhouqiang847@gmail.com
@file: liteOrderDict.py
@time: 2021/8/28 下午12:43
@desc:
"""


class Link:
    def __init__(self):
        self.key = None
        self.prev = None
        self.next = None


class LiteOrderDict(dict):
    def __init__(self):
        self.__mapping = {}
        self.__root = root = Link()
        root.next = root.prev = root

    def __setitem__(self, key, value):
        if key not in self:
            self.__mapping[key] = link = Link()
            root = self.__root
            last = root.next
            link.next, link.prev, link.key = root, last, key
            last.next = link
            root.prev = link

        super().__setitem__(key, value)

    def __delitem__(self, key):
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

    def pop(self, key, default=_marker):
        if key in self:
            result = self[key]
            del self[key]
            return result
        if default is self._marker:
            raise KeyError(key)
        return default

    def __iter__(self):
        root = self.__root
        curr = root.next
        while curr is not root:
            yield curr.key
            curr = curr.next


if __name__ == '__main__':
    d = LiteOrderDict()
    d['two'] = 1
    d['one'] = 2

    for k in d:
        print(k, d[k])
