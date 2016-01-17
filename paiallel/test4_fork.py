import os
import time
import signal

def onsignal_term(a,b):
    print "over"

signal.signal(signal.SIGTERM,onsignal_term)

r,w = os.pipe()
pid = os.fork()
a = 1

if pid == 0:
    os.close(r)
    #print "r=%d,w=%d" %(r,w)
    print "this is child",pid,os.getpid(),os.getppid()
    w = os.fdopen(w,"w")
    #time.sleep(1)
    #print a+1
    while True:
	a=a+1
	if a>100:
	    os.kill(os.getpid,signal.SIGTERM)
	w.write(str(a)) #write in child
	print a
    w.close()
else:
    os.close(w)
    r = os.fdopen(r,"r")
    print r.read() #read in parent
    r.close()
    print "this is parent",pid,os.getpid()
    status = os.waitpid(pid,0)
    print "parent over"
