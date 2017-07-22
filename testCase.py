# -*- coding: utf-8 -*-
import os

# 列出所有case
caselist = os.listdir("./testCase")
for a in caselist:
	s = a.split('.')[0]

	if s == 'baiduTest':
		os.system("./testCase/\\%s 1>>log.txt 2>&1" %a)

	if s == 'cloudTest':
		os.system("./testCase/\\%s 1>>log.txt 2>&1" %a)

	if s == 'widgetTest':
		os.system("./testCase/\\%s 1>>log.txt 2>&1" %a)

	if s == 'youdaoTest':
		os.system("./testCase/\\%s 1>>log.txt 2>&1" %a)

