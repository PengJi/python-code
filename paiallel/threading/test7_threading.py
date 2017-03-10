import threading
import time

mylock = threading.RLock()
count = 0

class aa(threading.Thread):
    def __init__(self,no,interval):
	"""Constructor"""
	threading.Thread.__init__(self)
        self.no = no
	self.intervalu = interval
        self.isstop = False

    def run(self):
	global count
	a = 0
	while a<10:
	    mylock.acquire()
	    count +=1 
	    mylock.release()
	    print 'thread %d=%d' %(self.no,count)
	    a+=1

    def stop(self):
	self.isstop = True

def factory():
    t1 = aa(1,2)
    t1.start()
    t2 = aa(2,1)
    t2.start()
    time.sleep(10)
    t1.stop()
    t2.stop()

if __name__=='__main__':
    factory()

