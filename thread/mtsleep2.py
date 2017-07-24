#-*-coding:utf-8-*-
# 锁的使用
import thread
from time import sleep,ctime

loops = [4,2]

def loop(nloop,nsec,lock):
	print'start loop',nloop,'at:',ctime()
	# 获取锁需要一定的时间，
	# 退出太快可能还没取到锁
	sleep(nsec)
	print'loop',nloop,'done at:',ctime()
	#解锁
	lock.release()
 
def main():
	print'starting at:',ctime()
	locks = []

	# 给每个线程加锁
	for i in loops:
		# 返回一个新的锁定对象
		lock = thread.allocate_lock()
		#锁定
		lock.acquire()
		# 把锁放到锁列表locks中
		locks.append(lock)

	#执行多线程
	for i in range(len(loops)):
		thread.start_new_thread(loop,(i,loops[i],locks[i]))

	# 只是一直等，达到暂停主线程的目的，
	# 直到两个锁都被解锁才继续运行
	for i in range(len(loops)):
		while locks[i].locked():
			pass

	print 'all end:',ctime()

if __name__ == '__main__':
	main()