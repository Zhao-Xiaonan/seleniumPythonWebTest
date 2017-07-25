#-*-coding:utf-8-*-
import unittest,time,os,multiprocessing
import commands
from email.mime.text import MIMEText
import HTMLTestRunner
import sys
sys.path.append('../')

def EEEcreatsuite():
	# 读取selenium目录下的文件，
	# 找到名字包含thread的文件夹（thread1/2），
	# 添加到casedir数据组
	casedir = []
	listaa = os.listdir('../')
	for xx in listaa:
		if 'thread' in xx:
			casedir.append(xx)
	print casedir

	# 定位suite数组，for循环读取casedir中的数据，
	# 发现文件夹下匹配start*.py的用例，添加到testunit测试条件中
	# 再讲测试套件追加到定义的suite数组中
	suite = []
	for n in casedir:
		testunit = unittest.TestSuite()
		discover = unittest.defaultTestLoader.discover(str(n),
			pattern = 'start*.py',
			top_level_dir = r'../../')
		for testSuite in discover:
			for testCase in testSuite:
				testunit.addTests(testCase)
				#print testunit
			suite.append(testunit)
		return suite,casedir

def EEEEEmultiRunCase(suite,casedir):
	now = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime(time.time()))
	filename = "" + now + " report.html"
	fp = file(filename,'wb')

	# 定义proclist函数把suite数组中的用例之心个结果写入THMLTestRunner报告，
	proclist = []
	s = 0
	for i in suite:
		runner = HTMLTestRunner.HTMLTestRunner(
			stream = fp,
			title = str(casedir[s]) + u'测试报告',
			description = u'用例执行情况:',
			)

	proc = multiprocessing.Process(target = runner.run,
		args = (i,))
	proclist.append(proc)
	s = s + 1
	for proc in proclist:proc.start()
	for pric in proclist:proc.join()
	fp.close()

if __name__ == '__main__':
	runtmp = EEEcreatsuite()
	EEEEEmultiRunCase(runtmp[0],runtmp[1])