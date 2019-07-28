# -*- coding: utf-8 -*-

"""
app.task装饰add函数成一个Task实例，add.delay函数将task实例序列化后，
通过librabbitmq库的方法将任务发送到rabbitmq；

该过程创建一个名字为celery的exchange交换机，类型为direct（直连交换机）;
创建一个名为celery的queue，队列和交换机使用路由键celery绑定；
"""

from celery import Celery
app = Celery('tasks', broker='amqp://guest:guest@localhost:5672//',backend='redis://localhost:6379/0')

@app.task
def add(x, y):
    return x + y

if __name__ == '__main__':
    result = add.delay(30, 42)