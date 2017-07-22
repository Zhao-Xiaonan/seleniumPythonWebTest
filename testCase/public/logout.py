#!/usr/bin/python
#-*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import unittest,time

def logout(self):
	driver = self.driver
	# 退出
	quitIcon = driver.find_element_by_class_name("user-name")
	ActionChains(driver).move_to_element(quitIcon).perform()
	time.sleep(2)
	driver.find_element_by_link_text("退出").click()
	time.sleep(2)

	# 确认退出窗口
	driver.find_element_by_id("moduleHeadWitchLoginName").click()
	time.sleep(2)


