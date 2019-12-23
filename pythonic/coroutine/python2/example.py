#coding=utf-8
import time

# https://zhuanlan.zhihu.com/p/70155189


def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            continue
        print('[CONSUMER] Consuming %s...' % n)
        time.sleep(2)
        r = '200 OK'


def produce(c):
    c.next()
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


if __name__ == '__main__':
    c = consumer()
    produce(c)