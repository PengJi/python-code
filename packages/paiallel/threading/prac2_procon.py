# -*- coding: utf-8 -*-

import threading
from time import sleep
from Queue import Queue
from random import randint

#个性化自己的线程类 

class MyThread(threading.Thread):
    def __init__(self, func, args):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        
    def run(self):
        apply(self.func, self.args)

    
#生产方法
def produce(queue, loops):
    for i in range(loops):
        queue.put('product', 1)
        print 'Producted 1 product...    The No. of products now is: %d' %queue.qsize() 
        sleep(randint(1, 3))
        

#消费方法
def consume(queue, loops):
    for i in range(loops):
        queue.get(1)
        print 'Consumed 1 product...    The No. of products now is: %d' %queue.qsize()
        sleep(randint(2, 5))


if __name__ == '__main__':
    queue = Queue(30)
    threads = []
    print 'start...'
    
    threadP = MyThread(produce, (queue, 10))
    threadC = MyThread(consume, (queue, 10))
    threads.append(threadP)
    threads.append(threadC)
        
    noOfThreads = range(len(threads))
    
    for i in noOfThreads:
        threads[i].start()
        
    for i in noOfThreads:
        threads[i].join()
        
    print 'done...'
