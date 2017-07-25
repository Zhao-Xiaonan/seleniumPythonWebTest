# -*- coding: utf-8 -*-
import unittest
import HTMLTestRunner
import time,os

# 使用discover方法，不需要列出全部测试文件，自动识别*Test.py文件执行
listDir = './testCase/'
def creatsuitel():
	testAll = unittest.TestSuite()
	discover = unittest.defaultTestLoader.discover(listDir,
		pattern = 'start*.py',
		top_level_dir = None)
	for test in discover:
		for testCase in test:
			testAll.addTest(testCase)
			print testAll
		return testAll
allCaseName = creatsuitel()

# 执行，不生成报告
# 把TestSuite传给TestRunner进行执行
# unittest.TextTestRunner().run(testAll)

# 执行并生成报告
time = time.strftime("%Y-%m-%d %H-%M-%S",time.localtime(time.time()))
fileName = "./testResult/" + time + ' allTest.html'
fp = file(fileName,'wb')

runner = HTMLTestRunner.HTMLTestRunner(
        stream = fp,
        title = u"百度搜索测试报告",
        description = u"用例执行情况：")

# 控制时间执行
k = 1
while k < 2:
	timing = time.strftime('%H_%M',time.localtime(time.time()))
	if timing == '12_00':
		print u"开始运行脚本："
		runner.run(alltestnames)
		print u"运行完成退出"
		break
	else:
		time.sleep(5)
		print timing