# -*- coding:utf8 -*-

#用例封装
import unittest
import sys,os,traceback
from framework.browser_engine import BrowserEngine

class test_readget(unittest.TestCase):

    def setUp(self):
        browser = BrowserEngine()
        self.driver = browser.getdriver()
        self.driver.implicitly_wait(2)

    def test_employment(self):
        # 转正申请
        browser = BrowserEngine()
        browser.open_browser(0, 4, 0)
        self.driver.find_element_by_link_text("劳动关系").click()
        self.driver.find_element_by_xpath("//*[@class='o_sub_menu_content']/div[2]/ul[1]/li[1]/a").click()
        self.driver.find_element_by_class_name("o_list_button_add").click()
        dl = self.driver.find_element_by_xpath("//*[@name='assessment']")
        dl.send_keys("**++**")
        self.driver.find_element_by_class_name("o_form_button_save").click()
        # self.driver.find_element_by_link_text("劳动关系").click()
        # self.driver.find_element_by_xpath("//*[@class='o_sub_menu_content']/div[2]/ul[1]/li[1]/a").click()
        self.driver.find_element_by_xpath("//*[@class='table-responsive']/table/tbody")
        table = self.driver.find_elements_by_xpath("//*[@class='o_data_row']")
        print(table[0].text)
        # 断言
        self.assertTrue('xiaomiao' in table[0].text)

    def tearDown(self):
        test_method_name = self._testMethodName
        runlog_path = r'F:\python_autotest\runlog'
        os.chdir(runlog_path)
        method_path = runlog_path + test_method_name
        print(method_path)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()