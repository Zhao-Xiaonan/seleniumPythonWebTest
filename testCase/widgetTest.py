# -*- coding: utf-8 -*-

from widget import widget
import unittest

# 执行测试的类
class WidgetTestCase(unittest.TestCase):#TestCase对特定类进行测试的方法

	def setUp(self):
		self.widget = widget()

	def tearDown(self):
		self.widget.dispose()
		self.widget = None

	def testSize(self):
		u'''检查初始值'''
		self.assertEqual(self.widget.getSize(),(40,40))

	def testResize(self):
		u'''重新设置长和宽'''
		self.widget.resize(100,100)
		self.assertEqual(self.widget.getSize(),(100,100))

# def suite():
	# suite = unittest.TestCase()
	# suite.addTest(WidgetTestCase("testSize"))
	# suite.addTest(WidgetTestCase("testResize"))
	# return suite
	# 如果所有测试函数以test开头，可以直接调用makeSuite（）构造
	# return unittest.makeSuite(WidgetTestCase,"test")

if __name__ == '__main__':
	# 如果所有测试函数以test开头，可以不调用构造，这里可以直接执行
	unittest.main()
	# suite = unittest.TestSuite()
	# suite.addTest(WidgetTestCase("testSize"))
	# suite.addTest(WidgetTestCase("testResize"))
	
	# runner = unittest.TextTestRunner()
	# runner.run(suite)