#-*-coding:utf-8-*-
# 只能在*nix上运行
# 双向pipe，建立的时候返回一个含有两个元素的表，
# 每个元素代表pipe的一端（connection对象）。
# 对一端调用send发送，另一端recv接受
import multiprocessing

def proc1(pipe):
	pipe.send('hello')
	print('proc1 rec:',pipe.recv())

def proc2(pipe):
	print('proc2 rec:',pipe.recv())
	pipe.send('hello too')

pipe = multiprocessing.Pipe()
p1 = multiprocessing.Process(target = proc1,args = (pipe[0],))
p2 = multiprocessing.Process(target = proc2,args = (pipe[1],))

p1.start()
p2.start()
p1.join()
p2.join()