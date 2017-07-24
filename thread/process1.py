#-*-coding:utf-8-*-
# multiprocessing可以充分利用硬件的多处理器来进行工作
from multiprocessing import Process

def f(name):
	print'Hello',name

if __name__ == '__main__':
	p = Process(target = f,args = ('bob',))
	p.start()
	p.join()