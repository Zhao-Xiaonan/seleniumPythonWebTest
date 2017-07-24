#-*-coding:utf-8-*-
# 线程保护threading
import threading
from time import sleep,ctime

loops = [4,2]

def loop(nloop,nsec):
	print'start loop',nloop,'at:',ctime()
	# 获取锁需要一定的时间，
	# 退出太快可能还没取到锁
	sleep(nsec)
	print'loop',nloop,'done at:',ctime()
 
def main():
	print'starting at:',ctime()
	threads = []

	# 创建线程
	for i in range(len(loops)):
		t = threading.Thread(target = loop,args = (i,loops[i]))
		threads.append(t)

	# 开始线程
	for i in range(len(loops)):
		threads[i].start()

	# 等待所有线程结束
	for i in range(len(loops)):
		threads[i].join()

	print 'all end:',ctime()

if __name__ == '__main__':
	main()