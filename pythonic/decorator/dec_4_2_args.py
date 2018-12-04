# -*- coding: utf-8 -*-

"""
给装饰器传递参数
"""

import time
import functools
import signal

def timeout(seconds, error_message='function call time out'):
    def decorated(func):
        def _handle_timeout(signum, frame):
            raise Exception(error_message)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return functools.wraps(func)(wrapper)

    return decorated

@timeout(1, 'function slow; aborted')
def slow_function():
    time.sleep(5)

slow_function()
