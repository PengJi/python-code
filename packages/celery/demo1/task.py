# -*- coding: utf-8 -*-

from main import app


@app.task
def add(x, y):
    return x + y