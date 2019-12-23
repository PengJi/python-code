# -*- coding: utf-8 -*-
import time
import logging
from multiprocessing.dummy import Pool as ThreadPool

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s [%(levelname)s] %(message)s')
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger

def process(item):
    log = get_logger(item)
    log.info("item: %s" % item)
    time.sleep(2)


items = ['apple', 'bananan', 'cake', 'dumpling']
pool = ThreadPool()
pool.map(process, items)
pool.close()
pool.join()


def func(msg):
    print('msg:', msg)
    time.sleep(2)
    print('end:')


pool = ThreadPool(processes=3)
for i in range(1, 5):
    msg = 'hello %d' % (i)
    # pool.apply_async(func, (msg,))  # 非阻塞
    # pool.apply(func,(msg,))       # 阻塞,apply()源自内建函数，用于间接的调用函数，并且按位置把元祖或字典作为参数传入。
    # pool.imap(func,[msg,])        # 非阻塞, 注意与apply传的参数的区别
    pool.map(func, [msg, ])       # 阻塞

print('Mark~~~~~~~~~~~~~~~')
pool.close()
pool.join()  # 调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
print('sub-process done')