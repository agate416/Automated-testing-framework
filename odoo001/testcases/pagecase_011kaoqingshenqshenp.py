# -*- coding:utf8 -*-

#用例封装
import unittest
import sys,os,traceback,time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from framework.browser_engine import BrowserEngine

class test_readget(unittest.TestCase):

    def setUp(self):
        browser = BrowserEngine()
        self.driver = browser.getdriver()
        self.driver.implicitly_wait(2)

    #  审批
    def test_leave_approved(self):
        # 请假审批
        browser = BrowserEngine()
        browser.open_browser(0, 3, 0)
        self.driver.find_element_by_link_text("微核考勤").click()
        self.driver.find_element_by_xpath("//*[@class='o_sub_menu_content']/div[3]/ul[4]/li[2]/a").click()
        self.driver.find_element_by_xpath("//*[@class='table-responsive']/table/tbody")
        lists = self.driver.find_elements_by_xpath("//*[@class='o_data_row']")
        len(lists)
        # self.driver.find_element_by_xpath("/html/body/nav/div[2]/ul[2]/li/a/span").click()
        # self.driver.find_element_by_xpath("/html/body/nav/div[2]/ul[2]/li/ul/li[6]/a").click()
        # browser.open_browser(0, 3, 0)
        # self.driver.find_element_by_link_text("微核考勤").click()
        self.driver.find_element_by_xpath("//*[@class='o_sub_menu_content']/div[3]/ul[4]/li[1]/a").click()
        self.driver.find_element_by_xpath("//*[@class='o_control_panel']/div[3]/div[3]/button[2]").click()
        self.driver.find_element_by_xpath("//*[@class='o_content']/div/div/div/div[1]").click()
        self.driver.find_element_by_xpath("//*[@class='o_form_button_edit']").click()
        self.driver.find_element_by_xpath("//*[@class='tab-pane']/table[1]/tbody/tr/td[2]/div/div[2]").click()
        opinion = self.driver.find_element_by_xpath("//*[@class='tab-pane']/table[2]/tbody/tr/td[2]/textarea")
        opinion.click()
        opinion.send_keys("同意")
        self.driver.find_element_by_xpath("//*[@class='o_cp_buttons']/div/div[2]/button[1]").click()
        self.driver.find_element_by_xpath("//*[@class='o_sub_menu_content']/div[3]/ul[4]/li[2]/a").click()
        self.driver.find_element_by_xpath("//*[@class='table-responsive']/table/tbody")
        lie = self.driver.find_elements_by_xpath("//*[@class='o_data_row']")
        len(lie)
        self.assertNotEqual(len(lie), len(lists))

    def tearDown(self):
        test_method_name = self._testMethodName
        runlog_path = r'F:\python_autotest\runlog'
        os.chdir(runlog_path)
        method_path = runlog_path + test_method_name
        print(method_path)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()