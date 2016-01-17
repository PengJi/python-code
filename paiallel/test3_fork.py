import os
import time

r,w = os.pipe()
pid = os.fork()
total = 0
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
