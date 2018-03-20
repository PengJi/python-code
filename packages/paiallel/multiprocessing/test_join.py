#encoding:utf-8

from multiprocessing import Process
import os, time, random

def r1(process_name):
    '''
    for i in range(3):
        print process_name, os.getpid()     #打印出当前进程的id
        time.sleep(1)
    '''
    print "r1 befor"
    time.sleep(3)
    print "r1 after"
    print "f1",time.time()
def r2(process_name):
    '''
    for i in range(3):
        print process_name, os.getpid()     #打印出当前进程的id
        time.sleep(2)
    '''
    print "r1 befor"
    time.sleep(1)
    print "r2 after"
    print "f2",time.time()

if __name__ == "__main__":
        print "main process run..."
        p1 = Process(target=r1, args=('process_name1', )) 
        p2 = Process(target=r2, args=('process_name2', )) 

        p1.start()
        p2.start()
        p1.join()
        print "p1",time.time()
        p2.join()
        print "p2",time.time()

        print "main process runned all lines..."
