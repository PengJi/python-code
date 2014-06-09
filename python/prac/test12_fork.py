#coding=utf-8

import os

def myfork():
    pid = os.fork()
    if pid == 0:
        print "this is child",pid
    else :
        print "this is parent",pid
        
if __name__ == '__main__':
    myfork()


#多进程
fork 派生多进程、多线程
wait 父进程控制子进程
waitpid 父进程控制子进程
pipe singal 多进程之间通信
守护进程