# -*- coding:utf-8 -*-

#用例封装
import unittest
import sys, os
from framework.browser_engine import BrowserEngine
import traceback

class test_readget(unittest.TestCase):
    #初始化
    def setUp(self):
        browser = BrowserEngine()
        self.driver = browser.getdriver()
        self.driver.implicitly_wait(2)

    # 具体测试用例
    def test_New_employee(self):
        # 正常创建新用户
        browser = BrowserEngine()
        browser.open_browser(0,1,0)
        self.driver.find_element_by_link_text("微核员工").click()
        self.driver.find_element_by_class_name("o_main_content")
        self.driver.find_element_by_xpath("//*[@class='o_cp_buttons']/div/button[1]").click()
        browser.New_Employee(1, 1, 0)
        self.driver.find_element_by_xpath("//*[@class='o_cp_buttons']/div/div[2]/button[1]").click()
        self.driver.find_element_by_link_text("微核员工").click()
        self.driver.find_element_by_xpath('//*[@class="btn-group-sm"]/button[1]').click()
        self.driver.find_element_by_xpath('//*[@class="table-responsive"]/table/tbody')
        table = self.driver.find_elements_by_class_name("o_data_row")
        # 断言
        self.assertTrue('xiaomiao'in table[0].text)
    # 退出
    def tearDown(self):
        test_method_name = self._testMethodName
        runlog_path = r'F:\python_autotest\runlog'
        os.chdir(runlog_path)
        method_path = runlog_path + test_method_name
        print(method_path)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
