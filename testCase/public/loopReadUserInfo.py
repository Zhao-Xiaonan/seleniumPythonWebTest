#!/usr/bin/python
#-*-coding:utf-8-*-

import userInfo
import csv

info = userInfo.zidian()
print info

for us,pw in info.items():
	print us
	print pw



my_file = '../../testData/userInfo.csv'
data = csv.reader(file(my_file,'rb'))

for user in data:
	print user[0]
	print user[1]
	print user[2]
	print user[3]