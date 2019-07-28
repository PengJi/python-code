# -*- coding: utf-8 -*-

from celery import Celery
from task import add
import celeryconfig


app = Celery(__name__, include=["task"])
# 1.引入配置文件
app.config_from_object(celeryconfig)
# 2.直接加载配置
# app.conf.update(
#         task_serializer='json',
#         accept_content=['json'],
#         result_serializer='json',
#         timezone='Europe/Oslo',
#         enable_utc=True,
#     )


if __name__ == '__main__':
    result = add.delay(30, 42)