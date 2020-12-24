# -*- coding: utf-8 -*-


class Foo(object):
    labels = [5, 6, 7]

    def ins_func(self):
        return 'some'


def some_func():
    instance = Foo()
    print(instance.labels)
    return instance.ins_func()
