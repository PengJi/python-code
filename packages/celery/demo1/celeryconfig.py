# -*- coding: utf-8 -*-

BROKER_URL =  'amqp://guest:guest@localhost:5672//'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_TASK_SERIALIZER = 'msgpack'
CELERY_RESULT_SERIALIZER = 'msgpack'
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24   # 任务过期时间
CELERY_ACCEPT_CONTENT = ["msgpack"]            # 指定任务接受的内容序列化的类型.