# -*- coding:utf8 -*-

#用例封装
import unittest
import sys,os,time
from framework.browser_engine import BrowserEngine

class test_readget(unittest.TestCase):

    def setUp(self):
        browser = BrowserEngine()
        self.driver = browser.getdriver()
        self.driver.implicitly_wait(2)

    # 考勤统计
    def test_data_statistics(self):
        # 生成统计
        browser = BrowserEngine()
        browser.open_browser(0, 1, 0)
        self.driver.find_element_by_link_text("微核考勤").click()
        self.driver.find_element_by_xpath("//*[@class='table-responsive']/table/tbody")
        lists = self.driver.find_elements_by_xpath("//*[@class='o_data_row']")
        len(lists)
        self.driver.find_element_by_xpath("//*[@class='o_cp_buttons']/div/button[5]").click()
        self.driver.find_element_by_xpath("//*[@class='table-responsive']/table/tbody")
        lie = self.driver.find_elements_by_xpath("//*[@class='o_data_row']")
        len(lie)
        # 断言
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