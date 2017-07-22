#!/usr/bin/python
#-*-coding:utf-8-*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest,time
# 导入函数
import userInfo 

# 输入正确的账号密码
us,pw = userInfo.correctInfo()
# 输入错误的账号密码
# us,pw = userInfo.wrongInfo()
print us,pw

def login(self):
	driver = self.driver
	driver.maximize_window()
	driver.find_element_by_id("TANGRAM__PSP_4__userName").clear()
	driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys(us)
	driver.find_element_by_id("TANGRAM__PSP_4__password").clear()
	driver.find_element_by_id("TANGRAM__PSP_4__password").send_keys(pw)
	driver.find_element_by_id("TANGRAM__PSP_4__submit").click()
	time.sleep(3)