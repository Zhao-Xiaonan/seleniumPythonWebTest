#-*-coding:utf-8-*-
# 使用可调用的类
import threading
from time import sleep,ctime

loops = [4,2]
class ThreadFunc(object):
	def __init__(self,func,args,name=""):	
		self.func = func
		self.args = args
		self.name = name

	def __call__(self):
		apply(self.func,self.args)

def loop(nloop,nsec):
	print'start loop',nloop,'at:',ctime()
	sleep(nsec)
	print'loop',nloop,'done at:',ctime()
 
def main():
	print'starting at:',ctime()
	threads = []

	# 创建线程
	for i in range(len(loops)):
		# 调用ThreadFunc实例化对象，创建所有线程
		t = threading.Thread(
			target = ThreadFunc(loop,(i,loops[i]),loop.__name__))
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