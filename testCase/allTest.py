# -*- coding: utf-8 -*-

import baiduTest,youdaoTest,cloudTest,widgetTest
import unittest

testunit = unittest.TestSuite()

testunit.addTest(unittest.makeSuite(baiduTest.Baidu))
testunit.addTest(unittest.makeSuite(youdaoTest.YouDao))
testunit.addTest(unittest.makeSuite(cloudTest.webOperation))
testunit.addTest(unittest.makeSuite(widgetTest.WidgetTestCase))

runner = unittest.TextTestRunner()
runner.run(testunit)