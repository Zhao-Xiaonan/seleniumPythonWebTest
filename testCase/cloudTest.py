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

class webOperation(unittest.TestCase):  #继承unittest.TestCase

	def setUp(self):
		self.driver = webdriver.Firefox()
		# self.driver.implicity_wait(30)
		self.base_url = "https://pan.baidu.com/"
		self.verificationErrors = []  #错误信息被打印的这个列表
		self.accept_next_alert = True  #是否接受下一个警告
		print 'set up'

	def test_login(self):
		driver = self.driver #在login方法中使用driver操作浏览器
		# driver.get(self.base url"/login/?...")
		driver.get(self.base_url)
		driver.find_element_by_class_name("account-title").click()
		print"login"
		# 调用登录模块
		login.login(self)
		time.sleep(2)

		# 获取用户名
		now_user = driver.find_element_by_class_name("user-name").text
		if now_user == u"笑笑724smile":
			print "登录成功"
		else:
			raise NameError("user name error!")

		# 退出
		logout.logout(self)
		time.sleep(2)

	def tearDown(self):  #清理工作，如退出浏览器等
		self.driver.quit()
		#self.verificationErrors不为空，则输出列表中的报错信息
		self.assertEqual([],self.verificationErrors)

if __name__ == '__main__':
	unittest.main()  #用来测试类中以test开头的用例