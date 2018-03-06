#coding:utf-8

import os
import multiprocessing
import time

# http://xiaorui.cc/2014/09/08/python-multiprocessing%E8%BF%9B%E7%A8%8B%E9%80%9A%E4%BF%A1%E7%9A%84pipe%E5%92%8Cqueue%E6%96%B9%E5%BC%8F/

# 写入 worker
def inputQ(queue):
    while True:
        info = "进程号 %s : 时间: %s"%(os.getpid(),int(time.time()))
        queue.put(info)
        time.sleep(1)

# 获取 worker
def outputQ(queue,lock):
    while True:
        info = queue.get()
#        lock.acquire()
        print (str(os.getpid()) + '(get):' + info)
#        lock.release()
        time.sleep(1)

#===================
# Main
record1 = []   # store input processes
record2 = []   # store output processes
lock  = multiprocessing.Lock()    # To prevent messy print
queue = multiprocessing.Queue(3)
 
# input processes
for i in range(10):
    process = multiprocessing.Process(target=inputQ,args=(queue,))
    process.start()
    record1.append(process)
 
# output processes
for i in range(10):
    process = multiprocessing.Process(target=outputQ,args=(queue,lock))
    process.start()
    record2.append(process)
