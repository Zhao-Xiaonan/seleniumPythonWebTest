# -*- coding: utf-8 -*-

import baiduTest,youdaoTest,cloudTest,widgetTest
import unittest
import HTMLTestRunner
import time

testAll = unittest.TestSuite()

# makeSuite用于生产testsuite对象实例，把所有用例组装成TestSuite
# (py文件.类名)默认类下面所有以test开头的方法都会被执行
testAll.addTest(unittest.makeSuite(baiduTest.Baidu))
testAll.addTest(unittest.makeSuite(youdaoTest.YouDao))
testAll.addTest(unittest.makeSuite(cloudTest.webOperation))
testAll.addTest(unittest.makeSuite(widgetTest.WidgetTestCase))

# 最后把TestSuite传给TestRunner进行执行
# unittest.TextTestRunner().run(testAll)

# 定义报告
time = time.strftime("%Y-%m-%d %H-%M-%S",time.localtime(time.time()))
fileName = "../testResult/" + time + ' allTest.html'
fp = file(fileName,'wb')

runner = HTMLTestRunner.HTMLTestRunner(
        stream = fp,
        title = u"百度搜索测试报告",
        description = u"用例执行情况：")
runner.run(testAll)