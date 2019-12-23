# -*- coding: utf-8 -*-

def check_is_admin(f):
    """
    把参数检查和业务逻辑完全分离开来，让代码先的清晰
    """
    def wrapper(*args, **kwargs):
        if kwargs.get('username') != 'admin':
            raise Exception("This user is not allowed to get food")
        return f(*args, **kwargs)
    return wrapper

class Storage(object):
    @check_is_admin
    def get_food(self, username, food):
        return self.storage.get(food)

    @check_is_admin
    def put_food(self, username, food):
        return storage.put(food)

