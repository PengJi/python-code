# -*- coding: utf-8 -*-
import functools

"""
函数的属性变化
"""

def is_admin(f):
    """ 使用 functools.wrap """
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        if kwargs.get("username") != 'admin':
            raise Exception("This user is not allowed to get food")
        return f(*args, **kwargs)
    return wrapper

def is_admin(f):
    """ 另一种方法 """
    def wrapper(*args, **kwargs):
        if kwargs.get("username") != 'admin':
            raise Exception("This is not allowed to get food")
        return f(*args, **kwargs)
    return functools.wraps(f)(wrapper)

def foobar(username='someone'):
    """Do crazy stuff"""
    pass

@is_admin
def barfoo(username='someone'):
    """Do crazy stuff"""
    pass

def main():
    print foobar.func_doc
    print foobar.__name__

    print barfoo.func_doc
    print barfoo.__name__

if __name__ == '__main__':
    main()

