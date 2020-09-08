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
        while True:
            num = self.queue.get()
            print("retrieved ", num)
            time.sleep(1)
            self.queue.task_done()

        print("finished")


def main():
    # 创建一个 thread pool, 这里开启5个并发
    for i in range(5):
        t = ThreadNum(queue)
        t.setDaemon(True)
        t.start()

    # 往队列中填数据
    for num in range(10):
        queue.put(num)

    queue.join()

if __name__ == '__main__':
    main()


# 具体工作步骤描述如下：
# 1、创建一个 Queue.Queue() 的实例，然后使用数据对它进行填充。
# 2、将经过填充数据的实例传递给线程类，后者是通过继承 threading.Thread 的方式创建的。
# 3、生成守护线程池。
# 4、每次从队列中取出一个项目，并使用该线程中的数据和 run 方法以执行相应的工作。
# 5、在完成这项工作之后，使用 queue.task_done() 函数向任务已经完成的队列发送一个信号。
# 6、对队列执行 join 操作，实际上意味着等到队列为空，再退出主程序。
# 在使用这个模式时需要注意一点：通过将守护线程设置为 true，程序运行完自动退出。好处是在退出之前，可以对队列执行 join 操作、或者等到队列为空。
