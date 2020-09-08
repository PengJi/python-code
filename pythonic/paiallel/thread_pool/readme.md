自己实现线程池

# 线程池原理
我们把任务放进队列中去，然后开N个线程，每个线程都去队列中取一个任务，执行完了之后告诉系统说我执行完了，然后接着去队列中取下一个任务，直至队列中所有任务取空，退出线程。

* daemon说明：  
如果某个子线程的daemon属性为False，主线程结束时会检测该子线程是否结束，如果该子线程还在运行，则主线程会等待它完成后再退出；
如果某个子线程的daemon属性为True，主线程运行结束时不对这个子线程进行检查而直接退出，同时所有daemon值为True的子线程将随主线程一起结束，而不论是否运行完成。
daemon=True 说明线程是守护线程，守护线程外部没法触发它的退出，所以主线程退出就直接让子线程跟随退出

* queue.task_done() 说明：  
queue.join()的作用是让主程序阻塞等待队列完成，就结束退出，但是怎么让主程序知道队列已经全部取出并且完成呢？queue.get() 只能让主程序知道队列取完了，但不代表队列里的任务都完成，所以程序需要调用queue.task_done() 告诉主程序，又一个任务完成了，直到全部任务完成，主程序退出

## 队列（queue）
Queue模块提供的队列（FIFO）适用于多线程编程，在生产者(producer)和消费者(consumer)之间线程安全(thread-safe)地传递消息或其它数据，因此多个线程可以共用同一个Queue实例。常用方法:
* Queue.qsize()：返回queue的大小。
* Queue.empty():判断队列是否为空，通常不太靠谱。
* Queue.full():判断是否满了。
* Queue.put(item, block=True, timeout=None): 往队列里放数据。
* Queue.put_nowait(item):往队列里存放元素，不等待
* Queue.get(item, block=True, timeout=None): 从队列里取数据。
* Queue.get_nowait(item):从队列里取元素，不等待
* Queue.task_done()：表示队列中某个元素是否的使用情况，使用结束会发送信息。
* Queue.join()：一直阻塞直到队列中的所有元素都执行完毕。


# 参考
[Python 线程池原理及实现](https://www.jianshu.com/p/afd9b3deb027)  
[Python 使用threading+Queue实现线程池](https://blog.csdn.net/u012474535/article/details/79570011)