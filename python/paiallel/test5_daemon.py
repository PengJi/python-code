import os
import sys

def daemon_test():
    pid = os.fork()
    if pid > 0:
	sys.exit(0)

    os.setsid()
    os.umask(0)

    pid = os.fork()
    if pid > 0:
	sys.exit(0)

    f = open("test.txt",'w')
    a = 1
    while True:
	a = a+1
	f.write(str(a))
    f.close()

if __name__=='__main__':
    daemon_test()

