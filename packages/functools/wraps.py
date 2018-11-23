# -*- coding: utf-8 -*-

from functools import wraps

def trace(func):
    """ 装饰器 """

    #@wraps(func)
    def callf(*args, **kwargs):
        """ A wrapper function """
        print("Calling function:{}".format(func.__name__))  # Calling function:foo
        res = func(*args, **kwargs)
        print("Return value:{}".format(res))  # Return value:9
        return res

    return callf

@trace
def foo(x):
    """ 返回给定数字的平方 """
    return x * x

if __name__ == '__main__':
    print(foo(3))
    print(foo.__doc__)
    help(foo)
    print(foo.__name__)
    # print(foo.__globals__)
    t = trace(foo)
    print(t)
