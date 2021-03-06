# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import unittest,time,re


class YouDao(unittest.TestCase):
	 
	def setUp(self):
	 	self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(3)
		self.base_url = "http://www.youdao.com"
		self.verificationErrors = []
		self.accept_next_alert = True

	def testSearch(self):
		u"""搜索功能"""
		driver = self.driver
		driver.get(self.base_url + '/')

		driver.find_element_by_id("translateContent").send_keys(u"虫师")
		driver.find_element_by_xpath(".//*[@id='form']/button").click()
		time.sleep(2)

	def tearDown(self):
		self.driver.quit()
		self.assertEqual([],self.verificationErrors)

if __name__ == '__main__':
	unittest.main()
