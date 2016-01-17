#!/usr/bin/python
#coding=utf-8

'''
http://www.lai18.com/content/2443755.html
'''

import threading,subprocess
from time import ctime,sleep,time
from colorama import Fore, Back, Style
import Queue

queue=Queue.Queue()

class ThreadUrl(threading.Thread):
  def __init__(self,queue):
    threading.Thread.__init__(self)
    self.queue=queue

  def run(self):
    while True:
      host=self.queue.get()
      ret=subprocess.call('ping -c 1 -w 1 '+host,shell=True,stdout=open('/dev/null','w'))
      if ret:
        print Fore.GREEN + "%s is available" % host
      else:
        print Fore.RED + "%s is used" % host
      self.queue.task_done()

def main():
  for i in range(100):
    t=ThreadUrl(queue)
    t.setDaemon(True)
    t.start()
  for host in b:
    queue.put(host)
  queue.join()

b=['192.168.100.'+str(x) for x in range(1,254)]
start=time()
main()
print "Elasped Time:%s" % (time()-start)
print(Style.RESET_ALL)

