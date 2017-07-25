# -*- coding: utf-8 -*-
# 封装定位元素的方法
from selenium import webdriver

# 单个元素
def findId(driver,id):
	func = driver.find_element_by_id(id)
	return func

def findName(driver,name):
	func = driver.find_element_by_name(name)
	return func

def findClass(driver,classname):
	func = driver.find_element_by_class_name(classname)
	return func

def findTag(driver,tagname):
	func = driver.find_element_by_tag_name(tagname)
	return func

def findLink(driver,linktext):
	func = driver.find_element_by_link_text(linktext)
	return func

def findPLink(driver,plinktext):
	func = driver.find_element_by_partial_link_text(plinktext)
	return func

def findXpath(driver,xpath):
	func = driver.find_element_by_xpath(xpath)
	return func

def findCss(driver,css):
	func = driver.find_element_by_css_selector(css)
	return func

# 定位一组元素
def findsId(driver,id):
	func = driver.find_elements_by_id(id)
	return func

def findsName(driver,name):
	func = driver.find_elements_by_name(name)
	return func

def findsClass(driver,classname):
	func = driver.find_elements_by_class_name(classname)
	return func

def findsTag(driver,tagname):
	func = driver.find_elements_by_tag_name(tagname)
	return func

def findsLink(driver,linktext):
	func = driver.find_elements_by_link_text(linktext)
	return func

def findsPLink(driver,plinktext):
	func = driver.find_elements_by_partial_link_text(plinktext)
	return func

def findsXpath(driver,xpath):
	func = driver.find_elements_by_xpath(xpath)
	return func

def findsCss(driver,css):
	func = driver.find_elements_by_css_selector(css)
	return func