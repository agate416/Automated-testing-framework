# -*- coding:utf8 -*-

#用例封装
import unittest
import sys,os,traceback,time
from selenium.webdriver.common.keys import Keys
import pageobjects.page_interface
from framework.browser_engine import BrowserEngine

class test_readget(unittest.TestCase):

    def setUp(self):
        browser = BrowserEngine()
        self.driver = browser.getdriver()
        self.driver.implicitly_wait(2)

    def test_Data_import(self):
        # 数据导入
        browser = BrowserEngine()
        browser.open_browser(0, 1, 0)
        self.driver.find_element_by_link_text("微核考勤").click()
        self.driver.find_element_by_xpath("//*[@class='o_sub_menu_content']/div[3]/ul[1]/li[2]/a").click()
        self.driver.find_element_by_xpath("//*[@class='table-responsive']/table/tbody")
        lists = self.driver.find_elements_by_xpath("//*[@class='o_data_row']")
        len(lists)
        self.driver.find_element_by_xpath("//*[@class='o_cp_buttons']/div/button[2]").click()
        self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/form/div[1]/div[2]/div/span[1]/label").click()
        pageobjects.page_interface.mouse_keyboard()
        self.driver.find_element_by_xpath("//*[@class='o_cp_buttons']/button[1]").click()
        self.driver.find_element_by_xpath("//*[@class='o_cp_buttons']/button[2]").click()
        lie = self.driver.find_elements_by_xpath("//*[@class='o_data_row']")
        len(lie)
        self.assertNotEqual(len(lists),len(lie))

    def tearDown(self):
        test_method_name = self._testMethodName
        runlog_path = r'F:\python_autotest\runlog'
        os.chdir(runlog_path)
        method_path = runlog_path + test_method_name
        print(method_path)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()