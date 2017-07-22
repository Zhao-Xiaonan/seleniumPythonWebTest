# -*- coding: utf-8 -*-
# allTest执行时先从当前路径（或指定sys.path）查找，
# 找不到就从安装设置的路径找
import sys
sys.path.append("/testCase")
# 添加文件夹下所有文件，测试用例文件在__init__.py中添加
from testCase import *

def caseList():
	# 添加文件夹下所有文件，测试用例文件在__init__.py中添加
	allTestList = [
		baiduTest.Baidu,
		youdaoTest.YouDao,
		cloudTest.webOperation,
		widgetTest.WidgetTestCase,
		collectTest.webCollect,
		]
	print "success read case list!"

	return allTestList

