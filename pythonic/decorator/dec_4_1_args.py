# -*- coding: utf-8 -*-

"""
给装饰器传递参数
"""

import functools

def is_admin(admin='admin'):
    def decorated(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            if kwargs.get("username") != admin:
                raise Execption("This user is not allowed to get food")
            return f(*args, **kwargs)
        return wrapper
    return decorated

@is_admin(admin='root')
def barfoo(username='someone'):
    """ do crazy stuff """
    print '{0} get food'.format(username)

if __name__ == '__main__':
    barfoo(username='root')

