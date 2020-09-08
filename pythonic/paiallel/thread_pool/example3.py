# -*- coding: utf-8 -*-

from Queue import Queue
from threading import Thread
import time

queue = Queue()

class ThreadNum(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        done = False
        while not done:
            num = self.queue.get()
            if num is None:
                done = True
            else:
                print("retrieved ", num)
            time.sleep(1)
            self.queue.task_done()


def main():
    for i in range(5):
        t = ThreadNum(queue)
        t.setDaemon(True)
        t.start()

    for num in range(10):
        queue.put(num)

    queue.join()
    time.sleep(100)
    for i in range(10):
        queue.put(None)
        print('None')
    time.sleep(200)


if __name__ == '__main__':
    start = time.time()
    main()
    print("Elapsed Time: {}".format(time.time() - start))

