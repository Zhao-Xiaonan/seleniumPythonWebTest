#!/usr/bin/python
#-*-coding:utf-8-*-

from selenium import webdriver

try:
	open('abc.txt','r')
except IOError:
	print "No file"

try:
	print aa
except NameError,msg:
	print msg