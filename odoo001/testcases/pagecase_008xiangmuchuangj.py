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

    def test_project_establish(self):
        # 项目创建
        browser = BrowserEngine()
        browser.open_browser(0, 9, 0)
        sreach_window = self.driver.current_window_handle
        self.driver.find_element_by_link_text("微核项目").click()
        self.driver.find_element_by_xpath("//*[@class='o_cp_buttons']/div/button[1]").click()
        self.driver.find_element_by_xpath("//*[@class='o_form_sheet']")
        self.driver.find_element_by_xpath("//*[@name='name']").send_keys("feichuan")
        self.driver.find_element_by_xpath("//*[@class='modal-footer']/div/footer/button[1]").click()
        self.driver.find_element_by_xpath("//*[@class='o_content']/div/div/div/div[1]").click()
        self.driver.find_element_by_xpath("//*[@class='o_view_manager_content']/div/div/div").click()
        lie = self.driver.find_element_by_xpath("//*[@class='o_column_quick_create']")
        lie.send_keys("xuqiu")
        lie.send_keys(Keys.ENTER)
        renwu = self.driver.find_element_by_xpath("//*[@class='o_kanban_header']/div/span[4]/i")
        renwu.click()
        renwu.send_keys("需求分析")
        renwu.send_keys(Keys.ENTER)
        self.driver.find_element_by_xpath("//*[@class='o_content']/div/div/div/div[2]").click()
        self.driver.find_element_by_xpath("//*[@class='o_cp_buttons']/div/div/button[1]").click()
        self.driver.find_element_by_xpath("//*[@class='o_form_sheet']/div[5]/ul/li[2]a").click()
        plantime = self.driver.find_element_by_xpath("//*[@name='planned_hours']")
        plantime.clear()
        plantime.send_keys("10")

    def tearDown(self):
        test_method_name = self._testMethodName
        runlog_path = r'F:\python_autotest\runlog'
        os.chdir(runlog_path)
        method_path = runlog_path + test_method_name
        print(method_path)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()