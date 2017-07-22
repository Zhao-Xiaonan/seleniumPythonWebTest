#!/usr/bin/python
#-*-coding:utf-8-*-
from selenium import webdriver
import os,time

source = open("./data.rtf","r")
# 逐行读取
values = source.readlines()
source.close()

browser = webdriver.Firefox()
browser.get("http://www.baidu.com")

# 执行循环
for search in values:
	browser.find_element_by_id("kw").send_keys(search)
	browser.find_element_by_id("su").click()
	time.sleep(2)
	browser.back()
	
browser.quit()