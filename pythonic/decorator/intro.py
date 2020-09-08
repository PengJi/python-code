# -*- coding: utf-8 -*-

"""
装饰器介绍
"""


# 简单装饰器
def my_decorator(func):
    def wrapper():
        print('wrapper of decorator')
        func()
    return wrapper


# 第二种调用方式
def greet():
    print('hello world')

greet = my_decorator(greet)
greet()


# 第二种调用方式：更优雅的调用方式，使用@
@my_decorator
def greet():
    print('hello world')

greet()


# 带参数的装饰器
def my_decorator(func):
    def wrapper(message):
        print('wrapper of decorator')
        func(message)
    return wrapper

@my_decorator
def greet(message):
    print(message)

greet('hello world')


# 可传入任务参数的装饰器
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('wrapper of decorator')
        func(*args, **kwargs)
    return wrapper


# 带有自定义参数的装饰器
def repeat(num):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num):
                print('wrapper of decorator')
                func(*args, **kwargs)
        return wrapper
    return my_decorator

@repeat(4)
def greet(message):
    print(message)
