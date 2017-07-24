#-*-coding:utf-8-*-
# 只在*nix上运行
# queue先进先出
import os
import multiprocessing
import time

# input
def inputQ(queue):
	info = str(os.getpid()) + '(put):' + str(time.time())
	queue.put(info)

# output
def outputQ(queue,lock):
	info = queue.get()
	lock.acquire()
	print (str(os.getpid()) + '(get):' + info)
	lock.release()

# main
record1 = [] # store input processes
record2 = [] # store output processes
# 加锁，防止散乱的打印
lock = multiprocessing.Lock()
queue = multiprocessing.Queue(3)

# input processes
for i in range(10):
	process = multiprocessing.Process(target = inputQ,args = (queue,))
	process.start()
	record1.append(process)

# output processes
for i in range(10):
	process = multiprocessing.Process(target = outputQ,args = (queue,lock))
	process.start()
	record2.append(process)

for p in record1:
	p.join()

queue.close() #没有更多的对象进来，关闭queue

for p in record2:
	p.join()