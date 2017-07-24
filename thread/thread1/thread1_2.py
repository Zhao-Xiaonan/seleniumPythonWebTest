# -*-coding:utf-8-*-
import unittest,time,os,multiprocessing
import commands
from email.mime.text import MIMEText
import HTMLTestRunner
import sys
sys.path.append('../')

def EEEcreatsuite():
	casedir = []
	listaa = os.listdir('../')
	for xx in listaa:
		