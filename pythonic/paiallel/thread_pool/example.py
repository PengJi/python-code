# -*- coding: utf-8 -*-

import time
import threading
from threading import Thread
from Queue import Queue

# 创建队列实例， 用于存储任务
queue = Queue()


# 定义需要线程池执行的任务
def do_job():
    while True:
        i = queue.get()
        time.sleep(1)
        print 'index %s, curent: %s' % (i, threading.current_thread())
        queue.task_done()


if __name__ == '__main__':
    # 创建包括3个线程的线程池
    for i in range(3):
        t = threading.Thread(target=do_job)
        t.daemon=True  # 设置线程daemon  主线程退出，daemon线程也会推出，即时正在运行
        t.start()

    # 模拟创建线程池3秒后塞进10个任务到队列
    time.sleep(3)
    for i in range(10):
        queue.put(i)

    queue.join()

# 流程描述如下：
# 1. 创建Queue.Queue()实例，然后对它填充数据或任务
# 2. 生成守护线程池，把线程设置成了daemon守护线程
# 3. 每个线程无限循环阻塞读取queue队列的项目item，并处理
# 4. 每次完成一次工作后，使用queue.task_done()函数向任务已经完成的队列发送一个信号
# 5. 主线程设置queue.join()阻塞，直到任务队列已经清空了，解除阻塞，向下执行

# 这个模式下有几个注意的点：
# 1. 将线程池的线程设置成daemon守护进程，意味着主线程退出时，守护线程也会自动退出，如果使用默认
# daemon=False的话， 非daemon的线程会阻塞主线程的退出，所以即使queue队列的任务已经完成
# 线程池依然阻塞无限循环等待任务，使得主线程也不会退出。
#
# 2. 当主线程使用了queue.join()的时候，说明主线程会阻塞直到queue已经是清空的，
# 而主线程怎么知道queue已经是清空的呢？就是通过每次线程queue.get()后并处理任务后，
# 发送queue.task_done()信号，queue的数据就会减1，直到queue的数据是空的，queue.join()解除阻塞，向下执行。
#
# 3. 这个模式主要是以队列queue的任务来做主导的，做完任务就退出，由于线程池是daemon的，所以主退出线程池所有线程都会退出。
# 有别于我们平时可能以队列主导thread.join()阻塞，这种线程完成之前阻塞主线程。看需求使用哪个join()：
# 如果是想做完一定数量任务的队列就结束，使用queue.join()，比如爬取指定数量的网页
# 如果是想线程做完任务就结束，使用thread.join()

