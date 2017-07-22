# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import unittest,time
# import HTMLTestRunner

class Baidu(unittest.TestCase):
   
    def setUp(self):#初始化
        self.driver = webdriver.Firefox()
        # self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com"
        self.verificationErrors = []#错误信息被打印的这个列表
        self.accept_next_alert = True#是否接受下一个警告
    
    def testSearch(self):
        u"""百度搜索"""   #添加注释
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("selenium")
        driver.find_element_by_id("su").click()
        time.sleep(2)
    
    def testSet(self):
        u"""百度搜索"""   #添加注释
        driver = self.driver
        # 设置每页搜索即如果100条
        driver.get(self.base_url + "/cache/sethelp/help.html")
        time.sleep(2)

        # 保存设置
        driver.find_element_by_class_name("tt_icon").click()
        time.sleep(2)
        # driver.switch_to_alert().accept()


    # def is_element_present(self, how, what):#查找页面元素是否存在
    #     try: self.driver.find_element(by=how, value=what)
    #     except NoSuchElementException as e: return False
    #     return True
    
    # def is_alert_present(self):#对弹窗异常的处理
    #     try: self.driver.switch_to_alert()
    #     except NoAlertPresentException as e: return False
    #     return True
    
    # def close_alert_and_get_its_text(self):#关闭警告以及对得到文本框的处理
    #     try:
    #         alert = self.driver.switch_to_alert()
    #         alert_text = alert.text
    #         if self.accept_next_alert:
    #             alert.accept()
    #         else:
    #             alert.dismiss()
    #         return alert_text
    #     finally: self.accept_next_alert = True
    
    def tearDown(self):#清理工作，如退出浏览器等
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)#self.verificationErrors不为空，则输出列表中的报错信息

if __name__ == "__main__":
    # 定义一个单元测试容器
    # testunit = unittest.TestSuite()
    # # 添加用例
    # testunit.addTest(Baidu("testSearch"))
    # testunit.addTest(Baidu("testSet"))
    # # 定义报告存放路径
    # filename = "./result.html"
    # fp = file(filename,'wb')
    # # 定义测试报告
    # runner = HTMLTestRunner.HTMLTestRunner(
    #     stream = fp,
    #     title = u"百度搜索测试报告",
    #     description = u"用例执行情况：")
    # runner.run(testunit)
    unittest.main()#用来测试类中以test开头的用例
