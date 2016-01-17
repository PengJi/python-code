import thread
import time

c=1

def funt(no,a):
    global c
    while True:
	a=a+1
	print 'thread no %d = %d' %(no,a)

def testt():
    print 'start'
    thread.start_new_thread(funt,(1,2))
    thread.start_new_thread(funt,(2,2))
    time.sleep(2) #testt() is main program,when the progras is quit,thread will quit as well,so let main progress wait 2 seconds,child thread running 2 seconds
    #print 'end'

if __name__=='__main__':
    testt()

#testt()
