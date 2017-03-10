# -*- coding: utf-8 -*-

import threading
import time

class Producer(threading.Thread):
    def run(self):
        global count
        while True:
            if condition.acquire():
                if count >= 200:
                    condition.wait()
                else:
                    count = count+20
                    print self.name + ' produced 20 product, The count now is %d' %count
                    condition.notifyAll()
                condition.release()
                time.sleep(2)

class Consumer(threading.Thread):
    def run(self):
        global count
        while True:
            if condition.acquire():
                if count <= 0:
                    condition.wait()
                else:
                    count = count-20
                    print self.name + ' consumed 20 product, The count now is %d' %count
                    condition.notifyAll()
                condition.release()
                time.sleep(3)

count = 0
condition = threading.Condition()

    
if __name__ == '__main__':
    threads = []
    for i in range(5):
        p = Producer()
        threads.append(p)
        c = Consumer()
        threads.append(c)        
        
    noOfThreads = range(len(threads))    
    for i in noOfThreads:
        threads[i].start()
