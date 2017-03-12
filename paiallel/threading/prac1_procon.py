# -*- coding: utf-8 -*-

import threading
import Queue
import random
import time

'''
主程序中，启动2个线程，一个生产者，两个消费者。
一个产品池队列，生产者如果池子少于10个就产生5个随机数。
消费者如果池子内有超过8个就消费3个
'''
pool= Queue.Queue()   #空池子，用来存放生产者产生的随机数
con = threading.Condition()

class Producer(threading.Thread):
      def __init__(self,no):
            threading.Thread.__init__(self)
            self.no = no
            self.isStop = False

      def run(self):
            global pool
            while True:
                  con.acquire()
                  if pool.qsize()>10:
                        con.wait()
                        print 'The length of queue : %d' %pool.qsize()
                        print 'Producer %d wait' %self.no
                  else:
                        for i in range(5):
                              o =random.randrange(0,100)
                              pool.put(o)
                              print "producer produce : " + str(o)
                        con.notify()
                  con.release()
                  time.sleep(2)
                  
      def stop(self):
            self.isStop = True

class Consumer(threading.Thread):
      def __init__(self,no):
            threading.Thread.__init__(self)
            self.no = no
            self.isStop = False
            
      def run(self):
            global pool
            while True:
                  con.acquire()
                  if pool.qsize()<8:
                        con.wait()
                        print 'The length of queue : %d' %pool.qsize()
                        print 'consumer %d  wait' %self.no
                  else:
                        for i in range(3):
                              o=pool.get()
                              print "consumer%d  consume  : %s" %(self.no, str(o))
                        con.notify()
                  con.release()
                  time.sleep(2)
            
      def stop(self):
            self.isStop = True
                 

def test_thread():
      c1 = Consumer(1)
      c2 = Consumer(2)
      p1 = Producer(1)
      p2 = Producer(2)
      p1.start()
      p2.start()
      c1.start()
      c2.start() 
      time.sleep(1)
      c1.stop()
      c2.stop()
      p1.stop()           
      p2.stop()
 

if __name__ == '__main__':
      test_thread()

      
