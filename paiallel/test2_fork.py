import os
import time

r,w = os.pipe()
pid = os.fork()
total = 0

if pid == 0:
    os.close(r)
    #print "r=%d,w=%d" %(r,w)
    print "this is child",pid,os.getpid(),os.getppid()
    time.sleep(2)
    w = os.fdopen(w,"w")
    w.write("100")
    print "+100"
    total = total+100
    print "total in child=%d" %total
else:
    os.close(w)
    r = os.fdopen(r,"r")
    money = r.read()
    total = total+int(money)
    #print "r = %d,w = %d" %(r,w)
    print "this is parent",pid,os.getpid()
    status = os.waitpid(pid,0)
    print "parent over"
    print "total: %d" % total
