#!/usr/bin/python
#-*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import unittest,time
import login,logout

class webCollect(unittest.TestCase):  #继承unittest.TestCase

	def setUp(self):
		self.driver = webdriver.Firefox()
		self.verificationErrors = []  #错误信息被打印的这个列表
		self.accept_next_alert = True  #是否接受下一个警告

		self.driver.get("https://pan.baidu.com/")
		self.driver.find_element_by_class_name("account-title").click()
		login.login(self)
		time.sleep(2)

	def test_collect(self):
		driver = self.driver
		inputs = driver.find_elements_by_tag_name("span")
		n = 0
		for i in inputs:
			if i.get_attribute("class") == "text":
				n += 1
		print u"当前列表文件为 %d" %n

		driver.find_element_by_class_name("g-button").click()

		time.sleep(2)

		inputs = driver.find_elements_by_tag_name("span")
		ns = 0
		for i in inputs:
			if i.get_attribute("class") == "text":
				ns += 1
		print u"当前列表文件为 %d" %ns

		logout.logout(self)



	def tearDown(self):  #清理工作，如退出浏览器等
		self.driver.quit()
		#self.verificationErrors不为空，则输出列表中的报错信息
		self.assertEqual([],self.verificationErrors)

if __name__ == '__main__':
	unittest.main()  #用来测试类中以test开头的用例
