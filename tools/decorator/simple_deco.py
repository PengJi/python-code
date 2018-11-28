import logging

def use_logging(func):
    def wrapper(*args, **kw):
        logging.warn("%s is running" % func.__name__)
        return func(*args, **kw)
    return wrapper

def bar():
    print('I am bar')

bar = use_logging(bar)
bar()
