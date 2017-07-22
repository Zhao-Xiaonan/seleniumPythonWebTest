# -*- coding: utf-8 -*-
import unittest
import HTMLTestRunner
import time,os
import allCaseList

testAll = unittest.TestSuite()

allTestName = allCaseList.caseList()
# makeSuite用于生产testsuite对象实例，把所有用例组装成TestSuite
for test in allTestName:
	testAll.addTest(unittest.makeSuite(test))

# 使用discover方法，不需要列出全部测试文件，自动识别*Test.py文件执行
# listDir = './testCase/'
# def creatsuitel():
# 	discover = unittest.defaultTestLoader.discover(listDir,
# 		pattern = '*Test.py',
# 		top_level_dir = None)
# 	for test in discover:
# 		for testCase in test:
# 			testAll.addTest(testCase)
# 			print testAll
# 		return testAll
# allCaseName = creatsuitel()

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
runner.run(testAll)