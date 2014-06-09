#coding=utf-8

import os
import time

def myfork():
    a = 1
    pid = os.fork()
    if pid == 0:
        print "this is child %d--%d--%d" % (pid,os.getpid(),os.getppid())
	time.sleep(1)
        print a+1
    else :
	#status = os.waitpid(pid,0)
        print "this is parent %d--%d--%d" % (pid,os.getpid(),os.getppid())
	#time.sleep(1)
        print a+3
	#time.sleep(1)
        
if __name__ == '__main__':
    myfork()
